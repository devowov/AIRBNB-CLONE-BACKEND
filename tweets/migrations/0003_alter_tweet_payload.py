# Generated by Django 5.1.1 on 2024-10-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_alter_tweet_payload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='payload',
            field=models.TextField(max_length=180),
        ),
    ]
