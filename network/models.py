from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'Завод {self.title} - {self.country}, {self.city}, {self.address}, {self.phone_number}'

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Product(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Завод')
    name = models.CharField(max_length=200, verbose_name='Название')
    model = models.CharField(max_length=200, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    release_date = models.DateField(verbose_name='Дата выхода на рынок')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.model}) - Завод: {self.factory.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Retail(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Завод')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    arrears = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Название розничной сети: {self.title} \
                 Завод - изготовитель: {self.factory.title} \
                 Продукт: {self.product.name}'

    class Meta:
        verbose_name = 'Розничный магазин'
        verbose_name_plural = 'Розничные магазины'


class Individual(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='Завод')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона')
    arrears = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Индивидуальное предприятие: {self.title} \
                 Завод - изготовитель: {self.factory.title} \
                 Продукт: {self.product.name}'

    class Meta:
        verbose_name = 'Индивидуальное предприятие'
        verbose_name_plural = 'Индивидуальные предприятия'
