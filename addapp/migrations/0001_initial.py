# Generated by Django 2.2.7 on 2020-01-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
            ],
        ),
    ]
