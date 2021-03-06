# Generated by Django 3.0.8 on 2020-09-05 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0016_auto_20200904_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegPizCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_pizza', models.ManyToManyField(blank=True, related_name='reg_pizza', to='orders.RegularPizza')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_regcart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
