# Generated by Django 3.0.7 on 2020-07-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('check', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
