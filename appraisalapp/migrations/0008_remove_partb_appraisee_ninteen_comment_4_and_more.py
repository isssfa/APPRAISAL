# Generated by Django 4.0.1 on 2022-01-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appraisalapp', '0007_partb_appraisee_eighteen_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partb_appraisee',
            name='ninteen_comment_4',
        ),
        migrations.AddField(
            model_name='partb_appraisee',
            name='nineteen_comment_4',
            field=models.TextField(null=True),
        ),
    ]