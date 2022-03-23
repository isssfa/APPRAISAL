# Generated by Django 4.0.1 on 2022-01-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisalapp', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_absenteeism_apcomment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_absenteeism_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_attrition_apcomment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_attrition_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_ebitda_apcomment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_ebitda_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_revenue_apcomment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_revenue_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_scheduleadherence_apcomment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_scheduleadherence_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='parta_appraisee',
            name='mangr_specialcomment',
            field=models.TextField(null=True),
        ),
    ]