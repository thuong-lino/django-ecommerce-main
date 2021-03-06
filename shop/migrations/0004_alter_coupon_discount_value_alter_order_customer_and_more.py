# Generated by Django 4.0.5 on 2022-06-06 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_client_ip'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_order_user_orderdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price',
            field=models.IntegerField(blank=True, default=50000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
