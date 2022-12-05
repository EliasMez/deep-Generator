# Generated by Django 4.1.2 on 2022-10-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('url_image', models.URLField(max_length=500)),
                ('generating_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CodeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('code', models.TextField()),
                ('generating_date', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='ApiModel',
            new_name='FormModel',
        ),
        migrations.DeleteModel(
            name='BlogModel',
        ),
    ]
