# Generated by Django 2.2.9 on 2020-02-08 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200204_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotatedentity',
            name='icdCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ICDCode'),
        ),
        migrations.AddField(
            model_name='annotatedentity',
            name='opcsCode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.OPCSCode'),
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='clinical_coding_project',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='ProjectMetaAnnotate',
        ),
    ]
