# Generated by Django 5.0 on 2023-12-17 19:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(default=50),
            preserve_default=False,
        ),
    ]
