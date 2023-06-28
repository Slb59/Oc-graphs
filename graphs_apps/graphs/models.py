import pandas as pd
from datetime import timedelta, datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

TOTAL_TIME = 800
NBH_BYDAY_ONPROJECT = 4
NBH_BYDAY = 7


class Project(models.Model):

    subject = models.CharField(max_length=124)
    title = models.CharField(max_length=124)
    description = models.CharField(max_length=512, default="")

    estimate_time = models.DurationField(
        default=timedelta(hours=0)
        )

    nb_days_affected = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )

    estimate_start_date = models.DateField()
    estimate_end_date = models.DateField()
    real_start_date = models.DateField()
    real_end_date = models.DateField()
    real_time = models.DurationField(
        default=timedelta(hours=0)
        )
    real_time_on_project = models.DurationField(
        default=timedelta(hours=0)
        )
    evaluate_date = models.DateField()

    # self.tasks = []
    # self.df = pd.DataFrame([task.__dict__ for task in self.tasks])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['subject'], name='unique_project')
        ]

    @property
    def pct_total_time(self):
        return self.estimate_time/TOTAL_TIME

    @property
    def nb_hours_on_project(self):
        return self.nb_days_affected*NBH_BYDAY_ONPROJECT

    @property
    def nb_hours_affected(self):
        return self.nb_days_affected*NBH_BYDAY

    @property
    def dataframe(self):
        return pd.DataFrame([task.__dict__ for task in self.project.tasks])

    def __str__(self):
        return self.subject

    def __repr__(self):
        line = self.title + ": " + self.description + "\n"
        line += f"Estimations : {str(self.estimate_time)} soit"
        line += f"{str(self.pct_total_time)}% du total\n"
        line += f"{str(self.nb_days_affected)} jours affectés "
        line += f"soit {str(self.nb_hours_on_project)} heures sur le projet "
        line += f"et {str(self.nb_hours_affected)} heures au total\n"
        line += f"Le projet est prévu de : {self.estimate_start_date} "
        line += f"au {self.estimate_end_date}"
        if self.real_start_date:
            line += f"Il s'est effectivement déroulé du {self.real_start_date}"
            line += f" au {self.real_end_date}\n"
            line += f"pour une durée de {self.real_time} "
            +"heure soit {self.real_time_on_project} "
            line += f"{self.real_time_on_project} sur le projet"
        now = datetime.date
        print(self.evaluate_date)
        print(type(self.evaluate_date))
        if len(self.evaluate_date) > 0:
            a_date = datetime.datetime.strptime(self.evaluate_date, "%d/%m/%Y")
            if now < a_date:
                line += f"La soutenance aura lieu le {self.evaluate_date}"
            else:
                line += f"La soutenance a eu lieu le {self.evaluate_date}"
        return line


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
