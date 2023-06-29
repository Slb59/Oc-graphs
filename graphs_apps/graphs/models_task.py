# import pandas as pd
from datetime import timedelta
from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from .models_project import Project


class Task(models.Model):

    class Category(models.TextChoices):
        ORGANIZATION = "1ORG", _('Organisation')
        FORUM = "2FRM", _('Forum')
        MENTORAT = "3MEN", _('Mentorat')
        DEVELOPMENT = "6DEV", _('Developpement')
        ANALYSE = "5ANA", _('Analyse')
        FORMATION = "4FOR", _('Formation')
        EVALUATION = "7EVL", _('Evaluation')

    date_task = models.DateField()
    subject = models.ForeignKey(
        to=Project, related_name="project_task",
        on_delete=models.CASCADE,
        blank=True, null=True
        )
    category = models.CharField(
        max_length=4, choices=Category.choices, default=""
        )
    description = models.CharField(max_length=512, default="", blank=True)
    estimate_time = models.DurationField(
        default=timedelta(hours=0)
        )
    real_time = models.DurationField(
        default=timedelta(hours=0)
        )

    def __str__(self):
        ch = str(self.date_task) + "- (" + self.subject.title + ")"
        ch += self.category + "\n"
        ch += self.description + "\n"
        ch += "Estimé : " + str(self.estimate_time)
        ch += " --- Réalisé : " + str(self.real_time)
        return ch
