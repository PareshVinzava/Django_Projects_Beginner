# Generated by Django 4.0.3 on 2022-04-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_rename_is_bestsellingg_book_is_bestselling'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', null=b'I00\n'),
            preserve_default=b'I00\n',
        ),
    ]
