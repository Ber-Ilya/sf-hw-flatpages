from django.db import models

class Index(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Абстрактный класс"
        verbose_name_plural = "Абстрактные классы"


class Home(Index):
    pass

    class Meta:
        abstract = True
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страницы"


class AddStr(Index):
    pass

    class Meta:
        abstract = True
        verbose_name = "Дополнительная страница"
        verbose_name_plural = "Дополнительные страницы"


class Kontakti(Index):
    phone = models.IntegerField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = "Дополнительная страница"
        verbose_name_plural = "Дополнительные страницы"