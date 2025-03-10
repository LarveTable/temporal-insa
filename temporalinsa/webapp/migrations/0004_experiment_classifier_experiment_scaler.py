# Generated by Django 5.1.6 on 2025-03-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='classifier',
            field=models.CharField(max_length=20, null=True, verbose_name='Classifier'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='scaler',
            field=models.CharField(max_length=20, null=True, verbose_name='Scaler'),
        ),
    ]
