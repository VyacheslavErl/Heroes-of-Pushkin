# Generated by Django 4.2.7 on 2023-12-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_rename_disctions_characters_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characters',
            options={'verbose_name': 'Персонаж', 'verbose_name_plural': 'Персонажи'},
        ),
        migrations.AddField(
            model_name='characters',
            name='image_preview',
            field=models.ImageField(default=1, upload_to='', verbose_name='Превью'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='characters',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='short_description',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='work',
            field=models.CharField(max_length=100, verbose_name='Произведение'),
        ),
    ]