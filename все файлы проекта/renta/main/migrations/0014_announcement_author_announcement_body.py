# Generated by Django 4.1.7 on 2023-04-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_announcement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name='Автор публикации'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='body',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
