from django.contrib.auth import get_user_model
from django.db import models


DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая Техника')
)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар', null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY,
                                verbose_name='Категория', null=False, blank=False)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='product_pics', null=True, blank=True, verbose_name='Фото')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


RAITING_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey(Product, related_name='product_order', max_length=100, on_delete=models.CASCADE)
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст оьзыва')
    rating = models.CharField(max_length=50, choices=RAITING_CHOICES, default=None,
                                verbose_name='Рейтинг', null=False, blank=False)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

