# Generated by Django 3.1.8 on 2021-10-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validators', '0002_auto_20201204_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validator',
            name='ip_address',
            field=models.URLField(max_length=100, unique=True),
        ),
    ]