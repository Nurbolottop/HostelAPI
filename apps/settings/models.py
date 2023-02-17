from django.db import models

# Create your models here.
from django.db import models
# from django_resized.forms import ResizedImageField

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank = True, null = True
    )
    logo = models.ImageField(
        upload_to="logos/",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank = True, null = True
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank = True, null = True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    address_url = models.URLField(
        max_length=1000,
        verbose_name="Ссылка на адрес",
        blank = True, null = True
    )
    backround_image = models.ImageField(
        upload_to="backround_image/",
        verbose_name="Изображение на заднем плане в главной странице",
        null = True
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram",
        blank = True, null = True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на WhatsApp",
        blank = True, null = True
    )
    telegram = models.URLField(
        verbose_name="Ссылка на Telegram",
        blank = True, null = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"