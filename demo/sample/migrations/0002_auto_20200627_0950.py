# Generated by Django 3.0 on 2020-06-27 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20200627_0950'),
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchensink',
            name='linked_foreign_key',
            field=models.ForeignKey(limit_choices_to={'continent__name': 'Europe'}, on_delete=django.db.models.deletion.CASCADE, related_name='foreign_key_linked', to='world.Country'),
        ),
        migrations.AlterField(
            model_name='kitchensink',
            name='raw_id_field',
            field=models.ForeignKey(blank=True, help_text='Regular raw ID field', null=True, on_delete=django.db.models.deletion.SET_NULL, to='world.Country'),
        ),
    ]
