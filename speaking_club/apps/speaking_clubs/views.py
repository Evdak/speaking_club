import json
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponseNotAllowed,
    HttpResponse,
    HttpResponseServerError,
    JsonResponse,
    HttpResponseBadRequest,
)
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db.models import Count

from robokassa.forms import RobokassaForm
from apps.speaking_clubs.helpers import MAX_SCORE, define_levels, define_total_level, calculate_levels
from apps.speaking_clubs.helpers import generate_success_form
from apps.speaking_clubs.answers_helpers import get_answers, register_answer
from speaking_club.settings import GC_SECRET_KEY
from speaking_clubs import models

import logging

from random import randint


def login(request: HttpRequest):
    print(f"yec {request.user.id=}")
    if request.user.id:
        return redirect("profile")
    return render(request, 'login.html')


def index(request: HttpRequest):
    offers = models.Offer.objects.all()
    return render(request, 'main.html', {"offers": offers})


def index_gc(request: HttpRequest):
    offers = models.Offer.objects.all()
    return render(request, 'main_from_gc.html', {"offers": offers})


@csrf_exempt
def order_from_gc(request: HttpRequest):
    weekdays: str = request.POST.get("weekdays")
    time: str = request.POST.get("time")
    offer_id: int = request.POST.get("offer_id")
    email: str = request.POST.get("email")
    name: str = request.POST.get("name")
    invoice_number: str = request.POST.get("invoice_number")

    invoice_number = "".join(re.findall(r"\d+", invoice_number))

    offer = models.Offer.objects.filter(
        id=offer_id
    ).first()

    print((weekdays, time, offer_id, email, offer, name))

    if not all((weekdays, time, offer_id, email, offer, name, invoice_number)):
        print("ERROR: 'if not all((weekdays, time, offer_id, email, offer, name))'")
        return render(request, "error.html")

    try:
        time = int(time.split(':')[0])

    except Exception as err:

        print(f"ERROR: {str(err)}")
        return render(request, "error.html")

    order_from_gc = models.OrderGC.objects.filter(
        invoice_number=invoice_number,
        email=email,
    ).first()

    if not order_from_gc:
        return JsonResponse({"status": "ERROR", "result": "?????????? ???? ????????????. Email ?????? ??? ???????????? ??????????????, ???????????????????? ?????? ??????"})

    try:
        order, _ = models.Order.objects.get_or_create(
            invoice_number=invoice_number,
            offer=offer,
            email=email,
            time=time,
            weekdays=weekdays,
            name=name,
            order_from_gc=order_from_gc,
        )
    except IntegrityError:
        pass

    request.session['InvId'] = invoice_number

    return JsonResponse({"status": "OK", "result": "/login"})


@csrf_exempt
def pay_with_robokassa(request: HttpRequest):
    weekdays: str = request.POST.get("weekdays")
    time: str = request.POST.get("time")
    offer_id: int = request.POST.get("offer_id")
    email: str = request.POST.get("email")
    name: str = request.POST.get("name")

    offer = models.Offer.objects.filter(
        id=offer_id
    ).first()

    print((weekdays, time, offer_id, email, offer, name))

    if not all((weekdays, time, offer_id, email, offer, name)):
        print("ERROR: 'if not all((weekdays, time, offer_id, email, offer, name))'")
        return render(request, "error.html")

    try:
        time = int(time.split(':')[0])

    except Exception as err:

        print(f"ERROR: {str(err)}")
        return render(request, "error.html")

    invoice_numbers = [el.invoice_number for el in models.Order.objects.all()] + [el.invoice_number for el in models.OrderGC.objects.all()]

    invoice_number = randint(1, (2**31) - 1)

    while invoice_number in invoice_numbers:
        invoice_number = randint(1, (2**31) - 1)

    order = models.Order.objects.create(
        invoice_number=invoice_number,
        offer=offer,
        email=email,
        time=time,
        weekdays=weekdays,
        name=name,
    )

    form = RobokassaForm(initial={
        'OutSum': order.offer.price,
        'InvId': order.invoice_number,
        # 'Desc': order.offer.description,
        'Email': order.email,
        # 'IncCurrLabel': '',
        # 'Culture': 'ru'
    })

    return JsonResponse({'url': form.get_redirect_url()})


@csrf_exempt
def update_session(request: HttpRequest):
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    try:
        invid = int(request.POST.get('InvId'))
        if invid:
            request.session['InvId'] = invid
    except:
        return HttpResponseServerError('???????????? ?????? ?????????????????? ??????????????, ???????????????????? ?? ??????????????????')
    return HttpResponse('ok')


@login_required
def profile(request: HttpRequest):
    logger = logging.getLogger('profile')
    student = models.Student.objects.filter(
        user=request.user
    ).first()
    logger.warning(f'{student=}')
    if student:
        if student.chat.first():
            return redirect("result")
        else:
            return redirect("test")

    invoice_number = request.session.get("InvId")
    logger.warning(f"{request.session.items()=}")
    logger.warning(f"{invoice_number=}")
    logger.warning(f"{request.user=}")
    if not invoice_number:
        order = models.Order.objects.filter(
            user=request.user,
        ).first()

    else:
        order = models.Order.objects.filter(
            invoice_number=invoice_number,
        ).first()

    if not order:
        logger.error("if not order")
        return render(request, "error.html", {'text': '?????? ?????????????? ???? ???????????? ?????????? ?????????? ??????????????????'})

    if not order.user:
        order.user = request.user

        order.save()

        try:
            models.Student.objects.create(
                user=request.user,
                email=order.email,
                name=order.name,
            )
        except IntegrityError:
            pass
    elif order.user != request.user:
        return render(request, "error.html", {'text': '?? ?????????????? ???????????? ???????????????? ???????????? Telegram ??????????????'})

    return redirect("test")


@login_required
def test(request: HttpRequest):
    return render(request, "test.html")


# @login_required
# @csrf_exempt
# def register_answer(request: HttpRequest):
#     student = models.Student.objects.filter(
#         user=request.user
#     ).first()
#     if not student:
#         return JsonResponse(
#             {
#                 "msg": "error"
#             }
#         )

#     nav = request.POST.get('nav')
#     answer = request.POST.get('answer')
#     position = request.POST.get('position')
#     is_true = request.POST.get('is_true')

#     if not all([nav, answer, is_true, position]):
#         return JsonResponse(
#             {
#                 "msg": "error"
#             }
#         )

#     _test: dict = student.test

#     if _test.get(nav) is None:
#         return JsonResponse(
#             {
#                 "msg": "error"
#             }
#         )

#     result = _test.get(nav)

#     if len(result) >= MAX_SCORE.get(nav):
#         return JsonResponse(
#             {
#                 "msg": "OK",
#                 "func": "close",
#                 "data": nav,
#             }
#         )

#     _test.get(nav).append(
#         [int(position), answer, is_true]
#     )

#     student.test = _test
#     student.save()

#     return JsonResponse(
#         {
#             "msg": "OK",
#             "func": "next",
#             "data": len(result) + 1,
#         }
#     )


@login_required
@csrf_exempt
def get_answer(request: HttpRequest):
    student = models.Student.objects.filter(
        user=request.user
    ).first()
    if not student:
        return JsonResponse(
            {
                "msg": "error"
            }
        )

    nav = request.POST.get('nav')

    if not all([nav]):
        return JsonResponse(
            {
                "msg": "error"
            }
        )

    _test: dict = student.test

    if _test.get(nav) is None:
        return JsonResponse(
            {
                "msg": "error"
            }
        )

    result = _test.get(nav)

    if len(result) >= MAX_SCORE.get(nav):
        return JsonResponse(
            {
                "msg": "OK",
                "func": "close",
                "data": nav,
            }
        )

    return JsonResponse(
        {
            "msg": "OK",
            "func": "next",
            "data": result,
            "max_score": MAX_SCORE.get(nav),
            "current_score": len(result),
        }
    )


@login_required
@csrf_exempt
def get_result(request: HttpRequest):
    student = models.Student.objects.filter(
        user=request.user
    ).first()
    if not student:
        print("ERROR: 'if not student'")
        return render(request, "error.html")

    if not student.test:
        return redirect('test')

    _test: dict = student.test

    levels, total_level = calculate_levels(_test)

    level = models.Level.objects.filter(
        name=total_level.get('total')
    ).first()
    if not level:
        print("ERROR: 'if not level'")
        return render(request, "error.html", {'text': '???????????? ?????? ?????????????????? ??????????????????????, ???????????????????? ?? ??????????????????'})

    order = models.Order.objects.filter(
        user=request.user,
    ).first()

    if not order:
        print("ERROR: 'if not order'")
        return render(request, "error.html")

    group = models.Group.objects.filter(
        level=level,
        weekdays=order.weekdays,
        time=order.time
    ).first()

    if not group:
        print("ERROR: 'if not group'")
        return render(request, "error.html", {'text': '???? ?????????????? ?????????? ?????????????????? ????????????, ???????????????????? ?? ??????????????????'})

    student = models.Student.objects.filter(
        user=request.user,
    ).first()

    if not student:
        print("ERROR: 'if not student'")
        return render(request, "error.html")

    if not student.chat.first():
        chat = models.Chat.objects.annotate(
            students_count=Count('students')
        ).order_by(
            "-students_count",
        ).filter(
            students_count__lt=3,
            group=group,
        ).first()
        if not chat:
            print("ERROR: 'if not chat'")
            return render(request, "error.html")
        chat.students.add(student)
        chat.save()

    levels.update(total_level)

    return render(
        request,
        "result.html",  {
            "levels": levels,
            "chat": student.chat.first(),
            "user_name": student.name,
        }
    )


def my_order(request: HttpRequest):
    request.GET.get('InvId')
    order = models.Order.objects.filter(
        invoice_number=request.GET.get("InvId")
    ).first()

    if order:
        form = generate_success_form(
            cost=request.GET.get("OutSum"),
            number=request.GET.get("InvId"),
            signature=request.GET.get("SignatureValue"),
        )

        return render('email.html', {'form': form})
    else:
        return render(request, "error.html")


@csrf_exempt
def create_order_from_gc(request: HttpRequest):
    try:
        invoice_number = int(request.GET.get('invoice_number'))
        email = request.GET.get('email')
        key = request.GET.get('key')

        logging.warning((invoice_number, email, key))

        if all((invoice_number, email, key == GC_SECRET_KEY)):
            models.OrderGC.objects.get_or_create(
                email=email,
                invoice_number=invoice_number,
            )
            return JsonResponse({"status": "OK"})
    except Exception as err:
        logging.critical(err)
    return HttpResponseBadRequest()


@login_required
@csrf_exempt
def register_answer_view(request: HttpRequest):
    _request = json.loads(request.body)
    quiz_id = _request.get('quiz_id')
    answer = _request.get("answer")

    if all((quiz_id, answer)):
        try:
            register_answer(request.user, quiz_id=quiz_id, answer=answer)
            return JsonResponse(
                {
                    "status": "OK",
                }
            )
        except Exception as err:
            logging.error(err)
    return JsonResponse(
        {
            "status": "ERROR",
            "msg": "?????????????????? ????????????, ???????????????????? ?????? ?????? ?????? ???????????????????? ?? ??????????????????",
        }
    )


@login_required
@csrf_exempt
def get_answers_view(request: HttpRequest):
    quiz_ids = request.POST.get('quiz_ids')

    try:
        quiz_ids = quiz_ids.split(';;')
    except:
        quiz_ids = None

    if all((quiz_ids)):
        try:
            answers = get_answers(request.user, quiz_ids=quiz_ids)

            return JsonResponse({
                "status": "OK",
                "answers": answers,
            })
        except Exception as err:
            logging.error(err)

    return JsonResponse(
        {
            "status": "ERROR",
            "msg": "?????????????????? ????????????, ???????????????????? ?????? ?????? ?????? ???????????????????? ?? ??????????????????",
        }
    )


@login_required
@csrf_exempt
def register_results_view(request: HttpRequest):
    logger = logging.getLogger('register_results_view')
    _request = json.loads(request.body)
    logger.warning(_request)
    try:
        if all([_request.get(el) != None for el in models.TEST]):
            student = models.Student.objects.filter(
                user=request.user
            ).first()
            logger.warning(student)
            logger.warning(student.test)
            student.test = _request
            logger.warning(student.test)
            student.save()
            logger.warning(student.test)
            return JsonResponse(
                {
                    "status": "OK",
                    "msg": "",
                }
            )
        else:
            logger.warning(all([_request.get(el) for el in models.TEST]))
            logger.warning([_request.get(el) for el in models.TEST])
    except Exception as err:
        logger.error(err)

    return JsonResponse(
        {
            "status": "ERROR",
            "msg": "?????????????????? ????????????, ???????????????????? ?????? ?????? ?????? ???????????????????? ?? ??????????????????",
        }
    )
