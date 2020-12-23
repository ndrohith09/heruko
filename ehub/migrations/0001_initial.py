# Generated by Django 3.1.1 on 2020-11-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=300)),
                ('productdetails', models.TextField()),
                ('productprize', models.FloatField()),
            ],
            options={
                'ordering': ['-productprize'],
            },
        ),
    ]
