# Generated by Django 4.2 on 2023-04-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_equipment_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='equipment_type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]