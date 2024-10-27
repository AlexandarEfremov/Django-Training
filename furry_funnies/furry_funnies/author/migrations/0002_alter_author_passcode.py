# Generated by Django 5.1.2 on 2024-10-27 11:19

import django.core.validators
import furry_funnies.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='passcode',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6), furry_funnies.core.validators.validate_password]),
        ),
    ]