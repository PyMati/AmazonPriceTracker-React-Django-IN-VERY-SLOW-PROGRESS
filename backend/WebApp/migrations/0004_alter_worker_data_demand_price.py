# Generated by Django 4.1.3 on 2022-11-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_worker_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker_data',
            name='demand_price',
            field=models.IntegerField(),
        ),
    ]