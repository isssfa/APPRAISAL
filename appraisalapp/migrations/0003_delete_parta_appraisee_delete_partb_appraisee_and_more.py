# Generated by Django 4.0.1 on 2022-01-11 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appraisalapp', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PartA_Appraisee',
        ),
        migrations.DeleteModel(
            name='PartB_Appraisee',
        ),
        migrations.DeleteModel(
            name='PartC_Appraisee',
        ),
        migrations.DeleteModel(
            name='PartD_Appraisee',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]