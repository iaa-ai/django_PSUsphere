# Generated by Django 5.1.2 on 2024-10-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
