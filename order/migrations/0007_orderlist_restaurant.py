# Generated by Django 2.0.1 on 2018-09-29 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_option_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='restaurant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.Restaurant'),
        ),
    ]
