# Generated by Django 3.2.20 on 2023-08-28 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230821_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomments',
            options={'ordering': ['created_on'], 'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AlterModelOptions(
            name='userposts',
            options={'ordering': ['-posted_on'], 'verbose_name_plural': 'User Posts'},
        ),
    ]
