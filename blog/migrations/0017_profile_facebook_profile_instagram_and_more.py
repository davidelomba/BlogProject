# Generated by Django 4.2.1 on 2023-06-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
