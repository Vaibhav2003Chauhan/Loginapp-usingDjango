# Generated by Django 4.2.1 on 2023-05-30 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_signup_signin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='name',
            new_name='username',
        ),
    ]
