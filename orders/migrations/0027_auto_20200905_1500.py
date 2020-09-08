# Generated by Django 3.0.8 on 2020-09-05 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0026_auto_20200905_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regpizcart',
            name='reg_piz',
        ),
        migrations.AddField(
            model_name='regpizcart',
            name='regular_pizza',
            field=models.ManyToManyField(blank=True, related_name='reg_pizza', to='orders.RegularPizza'),
        ),
        migrations.AlterField(
            model_name='regpizcart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_regcart', to=settings.AUTH_USER_MODEL),
        ),
    ]