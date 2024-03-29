# Generated by Django 2.2.10 on 2021-03-17 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0001_initial'),
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=34)),
                ('buyer_name_cleaned', models.CharField(help_text='Please, write the email of buyer', max_length=55)),
                ('merchant_name_cleaned', models.CharField(help_text='Please, write the email of associate merchant', max_length=55)),
                ('image_primary', models.ImageField(default='default.jpg', upload_to='media/product')),
                ('image_secondary', models.ImageField(blank=True, default='default.jpg', upload_to='media/product')),
                ('image_extra', models.ImageField(blank=True, default='default.jpg', upload_to='media/product')),
                ('image_chart', models.ImageField(blank=True, default='default.jpg', upload_to='media/chart')),
                ('description', models.CharField(max_length=34)),
                ('composition', models.CharField(max_length=55)),
                ('gauge', models.CharField(max_length=13)),
                ('size', models.CharField(max_length=13)),
                ('weight', models.CharField(max_length=89)),
                ('time', models.CharField(max_length=21)),
                ('moq', models.CharField(blank=True, max_length=21, null=True)),
                ('fob', models.PositiveIntegerField(blank=True, null=True)),
                ('date_order', models.DateField()),
                ('date_shipment', models.DateField()),
                ('season', models.CharField(max_length=21)),
                ('order_no', models.CharField(max_length=34)),
                ('lc_or_pi', models.CharField(max_length=55)),
                ('shipment_quantity', models.PositiveIntegerField()),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.Buyer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Gender')),
                ('merchant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant.Merchant')),
            ],
        ),
    ]
