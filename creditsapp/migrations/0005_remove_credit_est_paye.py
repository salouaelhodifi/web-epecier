# Generated by Django 4.1.5 on 2023-02-22 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creditsapp', '0004_remove_credit_paid_credit_est_paye_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='est_paye',
        ),
    ]
