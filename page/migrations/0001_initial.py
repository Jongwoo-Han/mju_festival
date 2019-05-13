# Generated by Django 2.2.1 on 2019-05-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('menu', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]