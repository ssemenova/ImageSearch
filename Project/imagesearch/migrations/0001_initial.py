# Generated by Django 3.0.3 on 2020-03-20 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Address1', models.CharField(max_length=200, null=True)),
                ('Address2', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('State', models.CharField(max_length=2)),
                ('Zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Filename', models.CharField(max_length=200)),
                ('EventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesearch.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField(null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('IsInvisible', models.BooleanField(default=False)),
                ('AddressID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='imagesearch.Address')),
                ('TemplatePhoto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='imagesearch.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Content', models.CharField(max_length=100000)),
                ('From', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='message_from', to='imagesearch.Person')),
                ('To', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='message_to', to='imagesearch.Person')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='CityID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='imagesearch.City'),
        ),
        migrations.CreateModel(
            name='PhotoOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesearch.Person')),
                ('PhotoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesearch.Photo')),
            ],
            options={
                'unique_together': {('PersonID', 'PhotoID')},
            },
        ),
        migrations.CreateModel(
            name='EventAttended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesearch.Event')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagesearch.Person')),
            ],
            options={
                'unique_together': {('PersonID', 'EventID')},
            },
        ),
    ]
