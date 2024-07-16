# Generated by Django 5.0.7 on 2024-07-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('stage', models.CharField(choices=[('in_progress', 'In Progress'), ('completed', 'Completed')], default='in_progress', max_length=20)),
                ('start_time', models.DateTimeField()),
                ('due_to', models.DateTimeField()),
            ],
        ),
    ]
