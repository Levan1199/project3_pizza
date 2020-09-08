# Generated by Django 3.0.8 on 2020-09-05 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20200905_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToppingsOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_order', to='orders.Cart')),
                ('sicilian_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='orders.Toppings')),
            ],
        ),
        migrations.CreateModel(
            name='SubsOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('size', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_order', to='orders.Cart')),
                ('sicilian_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.Subs')),
            ],
        ),
    ]