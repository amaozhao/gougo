from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Item(models.Model):
    name = models.CharField(_('name'), max_length=255)
    image = FilerImageField(null=True, blank=True, related_name='item_images')
    price = models.IntegerField(_('price'))
    description = models.TextField(_('description'))
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        db_table = 'item'
        ordering = ['-created']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Order(models.Model):
    item = models.ForeignKey(
        Item,
        related_name='orders',
        verbose_name=_('item')
    )
    user = models.ForeignKey(
        User,
        related_name='orders',
        verbose_name=_('item')
    )
    money = models.IntegerField(_('money'))
    created = models.DateTimeField(_('created time'), auto_now_add=True)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        db_table = 'order'
        ordering = ['-created']

    def __str__(self):
        return '%s: %s' % (self.user.username, self.item.name)


@python_2_unicode_compatible
class ItemInt(models.Model):
    item = models.ForeignKey(
        Item,
        related_name='itemInts',
        verbose_name=_('item')
    )
    user = models.ForeignKey(
        User,
        related_name='itemInts',
        verbose_name=_('user')
    )

    class Meta:
        verbose_name = _('itemInts')
        verbose_name_plural = _('itemInts')
        db_table = 'item_int'

    def __str__(self):
        return '%s: %s' % (self.user.username, self.item.name)


@python_2_unicode_compatible
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='carts',
        verbose_name=_('cart')
    )
    item = models.ForeignKey(
        Item,
        related_name='carts',
        verbose_name=_('item')
    )
    created = models.DateTimeField(_('created time'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        db_table = 'cart'
        ordering = ['-created']

    def __str__(self):
        return '%s: %s' % (self.user.username, self.item.name)


@python_2_unicode_compatible
class Profile(models.Model):

    GENDER = (
        (1, _('man')),
        (0, _('woman')),
    )
    user = models.OneToOneField(
        User,
        related_name='profile',
        verbose_name=_('profile')
    )
    nickname = models.CharField(_('nickname'), max_length=100)
    gender = models.IntegerField(_('gender'), choices=GENDER)
    phone = models.CharField(_('phone'), max_length=20)
    qq = models.CharField(_('qq'), max_length=20)
    weixin = models.CharField(_('weixin'), max_length=50)
    address = models.CharField(_('address'), max_length=200)

    def __str__(self):
        return self.nickname
