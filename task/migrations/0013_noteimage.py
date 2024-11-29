# Generated by Django 5.1.2 on 2024-10-25 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0012_task_isflagged_alter_task_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoteImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="note/images/")),
                (
                    "note",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="task.note",
                    ),
                ),
            ],
        ),
    ]