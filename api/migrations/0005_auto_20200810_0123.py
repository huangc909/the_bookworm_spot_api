# Generated by Django 3.0 on 2020-08-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200810_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='books/default.jpg', upload_to='books'),
        ),
    ]