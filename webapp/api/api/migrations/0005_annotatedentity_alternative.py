# Generated by Django 2.2.3 on 2019-09-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190925_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotatedentity',
            name='alternative',
            field=models.BooleanField(default=False),
        ),
    ]
