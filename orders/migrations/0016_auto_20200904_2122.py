# Generated by Django 3.0.8 on 2020-09-04 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_cart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='orders.Order'),
        ),
    ]
