# Generated by Django 3.0.8 on 2020-09-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_regpizcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='regpizcart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='regpizcart',
            name='size',
            field=models.BooleanField(default=False),
        ),
    ]
