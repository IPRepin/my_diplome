from django.contrib.auth.models import AbstractUser
from django.db import models

STATE_CHOICES = (
    ('basket', 'Статус корзины'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)

USER_TYPES = (
    ('seller', 'Продавец'),
    ('client', 'Клиент(Покупатель)')
)


class User(AbstractUser):
    type = models.CharField(max_length=50, null=False, blank=False, choices=USER_TYPES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(verbose_name='Ссылка', null=True, blank=True)
    file_name = models.OneToOneField(User, verbose_name='Пользователь',
                                     blank=True, null=True,
                                     on_delete=models.CASCADE)


class Category(models.Model):
    shops = models.ManyToManyField(Shop, related_name='category')
    name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()


class Parameter(models.Model):
    name = models.CharField(max_length=50)


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateField(auto_now=True)
    state = models.BooleanField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Contact(models.Model):
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
