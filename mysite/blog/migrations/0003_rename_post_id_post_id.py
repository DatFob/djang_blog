# Generated by Django 4.2.1 on 2023-05-22 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_id_post_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_id',
            new_name='id',
        ),
    ]
