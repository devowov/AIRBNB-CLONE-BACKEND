# Generated by Django 5.1.1 on 2024-10-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='payload',
            field=models.TextField(max_length=280),
        ),
    ]
