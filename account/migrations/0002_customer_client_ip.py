# Generated by Django 4.0.5 on 2022-06-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='client_ip',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
