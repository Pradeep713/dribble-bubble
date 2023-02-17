# Generated by Django 4.1.6 on 2023-02-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Normal User'), (2, 'Admin User'), (1, 'Super Admin User')], default=3, verbose_name='user_type'),
        ),
    ]
