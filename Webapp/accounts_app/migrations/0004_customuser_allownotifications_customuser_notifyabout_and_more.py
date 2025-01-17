# Generated by Django 5.0 on 2024-03-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts_app", "0003_alter_customuser_employee_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="allowNotifications",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="notifyAbout",
            field=models.CharField(
                choices=[
                    ("EVENTS", "Events"),
                    ("TASKS", "Tasks"),
                    ("MESSAGES", "Messages"),
                ],
                default="Messages",
                max_length=9,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="notifyThrough",
            field=models.CharField(
                choices=[("EMAIL", "Email"), ("SMS", "Text"), ("MESSAGES", "Messages")],
                default="Messages",
                max_length=9,
            ),
        ),
    ]
