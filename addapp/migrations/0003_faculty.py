# Generated by Django 2.2.7 on 2020-02-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addapp', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('deptname', models.CharField(max_length=200)),
            ],
        ),
    ]