# Generated by Django 4.0.3 on 2022-04-06 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_address_author_addresh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='addresh',
            new_name='address',
        ),
    ]
