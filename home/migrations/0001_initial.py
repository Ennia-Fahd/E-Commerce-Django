# Generated by Django 2.2.6 on 2020-10-19 08:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [ 
        migrations.CreateModel(
            name='SliderContent',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Heading', models.CharField(max_length=200)),
                ('Content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
