# Generated by Django 3.0.8 on 2020-09-05 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200905_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regpizcart',
            name='reg_piz',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reg_pizza', to='orders.RegularPizza'),
        ),
    ]