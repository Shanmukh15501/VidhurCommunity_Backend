# Generated by Django 4.2.9 on 2024-01-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_alter_users_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, 'Male'), (1, 'Fe-Male'), (2, 'Other')], default=0, null=True),
        ),
    ]
