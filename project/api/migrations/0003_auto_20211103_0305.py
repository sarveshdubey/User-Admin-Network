# Generated by Django 3.1.7 on 2021-11-02 21:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211102_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='advisor_name',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='advisor_pic_url',
            field=models.URLField(null=True),
        ),
    ]
