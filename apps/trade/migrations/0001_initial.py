# Generated by Django 2.2.6 on 2019-11-01 03:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='goods_num')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'OrderGoods',
                'verbose_name_plural': 'OrderGoods',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='order_sn')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='trade_no')),
                ('pay_status', models.CharField(choices=[('TRADE_SUCCESS', 'TRADE_SUCCESS'), ('TRADE_CLOSED', 'TRADE_CLOSED'), ('PAYING', 'PAYING')], default='paying', max_length=30, verbose_name='pay_status')),
                ('post_script', models.CharField(max_length=200, verbose_name='post_script')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='order_mount')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='pay_time')),
                ('address', models.CharField(default='', max_length=100, verbose_name='address')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='signer_name')),
                ('singer_mobile', models.CharField(max_length=11, verbose_name='singer_mobile')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='nums')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='goods')),
            ],
            options={
                'verbose_name': 'ShoppingCart',
                'verbose_name_plural': 'ShoppingCart',
            },
        ),
    ]
