# Generated by Django 4.2.3 on 2023-07-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_student_file_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
