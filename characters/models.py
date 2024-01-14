from django.db import models

class Characters(models.Model):
    id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField("Имя", max_length=40)
    last_name = models.CharField("Фамилия", max_length=40)
    image_preview = models.ImageField("Превью")
    image = models.ImageField("Изображение")
    description = models.TextField("Описание")
    short_description = models.TextField("Краткое описание")
    work = models.CharField("Произведение", max_length=100)

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"