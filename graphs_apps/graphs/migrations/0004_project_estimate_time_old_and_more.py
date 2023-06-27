# Generated by Django 4.2.2 on 2023-06-27 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("graphs", "0003_alter_project_estimate_time_alter_project_real_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="estimate_time_old",
            field=models.TimeField(default="00:00:00"),
        ),
        migrations.AlterField(
            model_name="project",
            name="estimate_time",
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name="project",
            name="real_time",
            field=models.TimeField(default="00:00:00"),
        ),
        migrations.AlterField(
            model_name="project",
            name="real_time_on_project",
            field=models.TimeField(default="00:00:00"),
        ),
    ]