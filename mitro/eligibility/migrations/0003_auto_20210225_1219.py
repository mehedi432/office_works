# Generated by Django 2.2.10 on 2021-02-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eligibility', '0002_auto_20210225_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eligibility',
            name='date',
            field=models.DateField(),
        ),
    ]
