# Generated by Django 3.1.2 on 2020-10-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_settimelimit'),
    ]

    operations = [
        migrations.AddField(
            model_name='settimelimit',
            name='marker',
            field=models.IntegerField(default=1),
        ),
    ]
