# Generated by Django 3.0.3 on 2020-03-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesearch', '0003_auto_20200320_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='TemplatePhoto',
        ),
        migrations.AddField(
            model_name='person',
            name='TemplateEncoding',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
