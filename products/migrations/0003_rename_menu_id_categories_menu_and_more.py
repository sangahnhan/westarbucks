# Generated by Django 4.0.3 on 2022-03-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_drinks_allergies_drinks_allergies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='drinks',
            old_name='categories_id',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='drinks_id',
            new_name='drinks',
        ),
        migrations.RenameField(
            model_name='nutritions',
            old_name='drinks_id',
            new_name='drinks',
        ),
        migrations.RenameField(
            model_name='nutritions',
            old_name='size_id',
            new_name='size',
        ),
    ]