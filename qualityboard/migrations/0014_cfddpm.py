# Generated by Django 4.0.1 on 2022-08-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualityboard', '0013_cfd_cfdccpriorityh_cfd_cfdccpriorityl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CFDDPM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DPMCFDtotalJiras', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalFixed', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalMRT', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalNotClosed', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalCurrentFix', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalNoise', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalPriorityH', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalPriorityM', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalPriorityL', models.CharField(blank=True, max_length=150)),
                ('DPMCFDtotalPriorityU', models.CharField(blank=True, max_length=150)),
                ('DPMCFDLastUpdate', models.CharField(blank=True, max_length=60)),
            ],
        ),
    ]
