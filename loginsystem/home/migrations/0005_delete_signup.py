# Generated by Django 4.2.1 on 2023-05-31 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_signin_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signup',
        ),
    ]