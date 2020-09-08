# Generated by Django 3.0.8 on 2020-09-05 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_auto_20200905_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaladsOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sal_order', to='orders.Cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salads', to='orders.Salads')),
            ],
        ),
        migrations.CreateModel(
            name='DinnerPlattersOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('size', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='din_order', to='orders.Cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner_platters', to='orders.DinnerPlatters')),
            ],
        ),
    ]
