# Generated by Django 4.1.2 on 2022-11-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_formmodel_alter_articlemodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codemodel',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
