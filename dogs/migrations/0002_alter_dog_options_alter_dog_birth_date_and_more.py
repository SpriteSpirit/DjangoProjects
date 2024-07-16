# Generated by Django 5.0.6 on 2024-05-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dog",
            options={"verbose_name": "собака", "verbose_name_plural": "собаки"},
        ),
        migrations.AlterField(
            model_name="dog",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="dog",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="dogs/", verbose_name="Фото"
            ),
        ),
    ]
