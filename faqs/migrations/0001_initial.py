# Generated by Django 3.2.18 on 2023-06-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
