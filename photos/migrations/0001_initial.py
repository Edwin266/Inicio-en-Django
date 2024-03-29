# Generated by Django 2.2.1 on 2019-05-07 02:30User

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('license', models.CharField(choices=[('RIG', 'Copyright'), ('LEF', 'Copyleft'), ('CC', 'Creative Commons')], max_length=3)),
            ],
        ),
    ]
