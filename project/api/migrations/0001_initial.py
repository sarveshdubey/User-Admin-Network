# Generated by Django 3.1.7 on 2021-11-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor_name', models.CharField(blank=True, max_length=50, null=True)),
                ('advisor_pic_url', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
