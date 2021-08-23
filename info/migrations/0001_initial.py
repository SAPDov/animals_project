# Generated by Django 3.2.6 on 2021-08-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('legs', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('family', models.IntegerField()),
            ],
        ),
    ]
