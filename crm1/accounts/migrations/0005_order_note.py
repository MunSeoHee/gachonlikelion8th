# Generated by Django 3.0.7 on 2020-08-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
