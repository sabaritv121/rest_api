# Generated by Django 4.0.4 on 2022-06-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='login',
            options={},
        ),
        migrations.AlterModelManagers(
            name='login',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='login',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='login',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='login',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='login',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='login',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='login',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='login',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='login',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='login',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='login',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=25),
        ),
    ]
