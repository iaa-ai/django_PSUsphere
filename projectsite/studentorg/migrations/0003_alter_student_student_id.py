# Generated by Django 5.1.2 on 2024-10-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0002_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=15),
        ),
    ]
