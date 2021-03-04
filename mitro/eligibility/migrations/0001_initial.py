# Generated by Django 2.2.10 on 2021-02-25 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=55)),
                ('mobile_number', models.CharField(max_length=55)),
                ('address', models.CharField(max_length=55)),
                ('age', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=144)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eligibility.Area')),
            ],
        ),
    ]