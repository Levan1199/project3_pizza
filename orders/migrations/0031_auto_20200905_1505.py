# Generated by Django 3.0.8 on 2020-09-05 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20200905_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regpizcart',
            name='reg_piz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_pizza', to='orders.RegularPizza'),
        ),
    ]