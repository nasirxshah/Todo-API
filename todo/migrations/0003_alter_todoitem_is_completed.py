# Generated by Django 4.2.3 on 2023-07-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todoitem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
