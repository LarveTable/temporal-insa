# Generated by Django 5.1.6 on 2025-03-10 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_experiment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values', models.JSONField(verbose_name='Values')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.experiment')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.method')),
            ],
        ),
    ]
