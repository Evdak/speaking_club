from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import IndividualLesson, IndividualStudent, IndividualTopic
from datetime import datetime
from django.utils import timezone

import logging


class IndividualLessonCreateForm(forms.ModelForm):
    # time = forms.CharField(
    #     widget=forms.Select(),
    #     label='Время',
    #     disabled=True,
    #     required=True,
    # )

    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "date",
                "min": timezone.now().date(),
                "max": (timezone.now() + timezone.timedelta(days=14)).date(),
            },
        ),
        label="Дата",
        required=True,
    )

    # teacher = forms.CharField(
    #     disabled=True,
    #     label='Преподаватель',
    #     required=True,
    # )

    class Meta:
        model = IndividualLesson
        exclude = (
            "status",
            "zoom_id",
            "zoom_url",
            "zoom_password",
        )
        widgets = {
            "student": forms.HiddenInput(),
            "time": forms.Select(),
            # "teacher": forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(IndividualLessonCreateForm, self).__init__(*args, **kwargs)
        self.fields["topic"].required = True
        self.fields["student"].required = True

        self.fields["teacher"].disabled = True

        instance = kwargs.get("instance")
        if instance:
            self.fields["teacher"].initial = str(instance.teacher)

        self.fields["topic"].queryset = IndividualTopic.objects.filter(
            level=self.fields["student"]._queryset.first().level
        )


class IndividualLessonForm(forms.ModelForm):
    class Meta:
        model = IndividualLesson
        exclude = (
            "status",
            "zoom_id",
            "zoom_password",
        )
        widgets = {
            "id": forms.HiddenInput(),
            "student": forms.HiddenInput(),
            "zoom_url": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(IndividualLessonForm, self).__init__(*args, **kwargs)
        self.fields["student"].disabled = True
        self.fields["date"].disabled = True
        self.fields["time"].disabled = True
        self.fields["teacher"].disabled = True
        self.fields["topic"].disabled = True

        self.fields["student"].required = False
        self.fields["date"].required = False
        self.fields["time"].required = False
        self.fields["teacher"].required = False
        self.fields["topic"].required = False
        self.fields["zoom_url"].required = True

        instance = kwargs.get("instance")
        if instance:
            self.fields["teacher"].initial = str(instance.teacher)


class IndividualLessonTeacherForm(IndividualLessonForm):
    class Meta:
        model = IndividualLesson
        exclude = (
            "zoom_id",
            "zoom_password",
        )
        widgets = {
            "id": forms.HiddenInput(),
            "teacher": forms.HiddenInput(),
            "zoom_url": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(IndividualLessonTeacherForm, self).__init__(*args, **kwargs)
        self.fields["status"].disabled = True

        self.fields["status"].required = True


class ChangeTeacherForm(forms.ModelForm):
    class Meta:
        model = IndividualStudent
        fields = ("teacher",)
        widgets = {
            # "student": forms.HiddenInput(),
        }
