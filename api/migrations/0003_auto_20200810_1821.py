# Generated by Django 3.0 on 2020-08-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='books/default-image.jpg', upload_to='books'),
        ),
    ]
