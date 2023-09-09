from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from django.db.models import Count
from django.db.models.functions import TruncDate

from individual_lessons.forms import IndividualLessonCreateForm, IndividualLessonForm, ChangeTeacherForm
from individual_lessons.models import IndividualLesson, IndividualStudent
from individual_lessons.helpers import create_meeting

import logging


def index(request: HttpRequest, gc_user: str):
    student = IndividualStudent.objects.filter(
        gc_user=gc_user,
    ).first()
    form = None
    if student:
        if request.method == 'POST':
            if student.hours_paid > 0:
                form = IndividualLessonCreateForm(request.POST)

                if form.is_valid():
                    # form.save()
                    lesson = IndividualLesson.objects.filter(
                        date=form.cleaned_data.get('date'),
                        time=form.cleaned_data.get('time'),
                        teacher=student.teacher,
                        student=None,
                    ).first()
                    if not lesson:
                        logging.warning(f'add_lesson: error 1 {form.cleaned_data=}')
                        messages.error(request, 'Не удалось создать занятие')
                    else:
                        if IndividualLesson.objects.filter(
                            date=form.cleaned_data.get('date'),
                            student=student,
                        ).count() > 4:
                            logging.warning('add_lesson: error 2')
                            messages.error(request, f'Нельзя забронировать больше 4 занятий в день')
                        elif lesson.date == timezone.now().date() and lesson.time <= (timezone.now() + timezone.timedelta(minutes=15)).time():
                            logging.warning('add_lesson: error 3')
                            messages.error(request, 'Не удалось создать занятие')
                        else:
                            lesson.student = student
                            lesson.teacher = student.teacher
                            lesson.topic = form.cleaned_data.get('topic')
                            lesson.status = 'Забронирован'
                            meeting = create_meeting(student, lesson)
                            if meeting.get('status') != 1:
                                logging.warning(f"{meeting=}")
                                messages.error(request, 'Не удалось создать занятие в Zoom')
                            else:
                                lesson.zoom_url = meeting['meeting_url']
                                lesson.zoom_password = meeting['password']
                                # lesson.zoom_id = meeting['id']
                                lesson.save()

                                student.hours_paid -= 1
                                student.save()
                                messages.success(request, f'Занятие забронировано')
                else:
                    logging.warning(f'{form.errors}')
            else:
                messages.error(request, f'Оплатите еще занятия')

        if not form:
            form = IndividualLessonCreateForm(initial={
                'student': student,
                'teacher': student.teacher,
            })

        my_lessons = IndividualLesson.objects.filter(
            student=student,
            date__gte=timezone.now().date(),
        ).all()

        my_lessons = [el for el in my_lessons if el.datetime() >= timezone.now()]

        my_lessons = [IndividualLessonForm(instance=el) for el in my_lessons]

        change_teacher_form = ChangeTeacherForm(instance=student)

        today = timezone.now()
        day_of_week = today.weekday()
        start_of_week = today - timezone.timedelta(days=day_of_week)
        end_of_week = start_of_week + timezone.timedelta(days=21)

        date_list = (
            IndividualLesson.objects.filter(
                date__range=(start_of_week, end_of_week),
                student=None,
                teacher=student.teacher,
            )
            .values('date')
            .annotate(lesson_count=Count('id'))
            .order_by('date')
            .values_list('date', flat=True)
        )

        date_list = [el for el in date_list]

        calendar = []

        all_dates = [start_of_week.date() + timezone.timedelta(days=i) for i in range(21)]

        logging.warning(f"{date_list=}")

        for lesson_date in all_dates:
            lessons_on_date = []
            if lesson_date in date_list:
                lessons_on_date = IndividualLesson.objects.filter(
                    date=lesson_date,
                    student=None,
                    teacher=student.teacher,
                )
            calendar.append(
                {
                    "lesson_date": lesson_date,
                    "lessons_on_date": lessons_on_date,
                }
            )

        # logging.warning(f"{calendar=}")
        return render(
            request,
            'individual_lessons/index.html',
            {
                'form': form,
                'my_lessons': my_lessons,
                'gc_user': gc_user,
                'calendar': calendar,
                'now': timezone.now(),
                'change_teacher_form': change_teacher_form,
                'student': student,
            }
        )
    else:
        logging.error(f"{student=}")


def get_date(request: HttpRequest, gc_user: str):
    if request.method == 'GET':
        student = IndividualStudent.objects.filter(
            gc_user=gc_user,
        ).first()
        date = request.GET.get('date')
        try:
            date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
        except Exception as err:
            logging.error(err)
            date = None

        if all((student, date)) and student.teacher and (timezone.now().date() <= date <= timezone.now().date() + timezone.timedelta(days=14)):
            lessons = IndividualLesson.objects.filter(
                date=date,
                teacher=student.teacher,
                student=None,
            )
            if date == timezone.now().date():
                lessons.filter(
                    time__gt=((timezone.now() + timezone.timedelta(minutes=15)).time()),
                )
            lessons = lessons.all()
            available_time = [el.time.strftime("%H:%M") for el in lessons]

            return JsonResponse(
                {
                    'available_time': available_time,
                }
            )
        else:
            logging.error(
                f"{student=}, {date.isoformat()=}, {student.teacher=}, {timezone.now().date() <= date <= (timezone.now().date() + timezone.timedelta(days=14))}")
        student.teacher.photo.path
    return JsonResponse(
        {
            'available_time': [],
        }
    )


def change_teacher(request: HttpRequest, gc_user: str):
    if request.method == 'POST':
        student = IndividualStudent.objects.filter(
            gc_user=gc_user,
        ).first()

        form = ChangeTeacherForm(request.POST, instance=student)
        logging.warning(f"{form.data=}")
        if form.is_valid():
            form.save()
            messages.success(request, f'Учитель сменен')
        else:
            messages.error(request, 'Не удалось сменить учителя')

    return redirect("individual_lessons_index", gc_user)


def delete_lesson(request: HttpRequest, gc_user: str):
    if request.method == 'POST':
        student = IndividualStudent.objects.filter(
            gc_user=gc_user,
        ).first()

        form = IndividualLessonForm(request.POST)  # , instance=student)
        if form.is_valid():
            lesson = IndividualLesson.objects.filter(
                zoom_url=form.cleaned_data['zoom_url'],
            ).first()
            if not lesson:
                logging.warning(f'delete_lesson: error 1 {form.cleaned_data=}')
                messages.error(request, 'Не удалось отменить занятие')
            else:
                lesson.student = None
                lesson.topic = None

                lesson.zoom_url = None
                lesson.zoom_password = None
                lesson.zoom_id = None
                lesson.status = 'Создан'
                lesson.save()
                if timezone.now() <= lesson.datetime() - timezone.timedelta(hours=8):
                    student.hours_paid += 1
                elif lesson.datetime() - timezone.timedelta(hours=3) <= timezone.now() <= lesson.datetime():
                    lesson.status = 'Почти отменен'
                lesson.save()
                student.save()

                messages.success(request, f'Занятие отменено')
        else:
            logging.warning(f'delete_lesson: error 2 {form.errors=} {form.data=}')
            messages.error(request, 'Не удалось отменить занятие')

    return redirect("individual_lessons_index", gc_user)
