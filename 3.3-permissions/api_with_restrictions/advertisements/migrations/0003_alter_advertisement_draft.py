# Generated by Django 4.1.2 on 2022-10-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_advertisement_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
