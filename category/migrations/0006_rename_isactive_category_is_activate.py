# Generated by Django 3.2.7 on 2022-05-06 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_isactive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='isactive',
            new_name='is_activate',
        ),
    ]