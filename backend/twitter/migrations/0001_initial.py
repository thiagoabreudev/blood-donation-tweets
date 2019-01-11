# Generated by Django 2.1.5 on 2019-01-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Create date')),
                ('id_twitte', models.CharField(max_length=255, verbose_name='ID twitte')),
                ('text', models.TextField(verbose_name='Text')),
                ('screen_name', models.CharField(max_length=255, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
