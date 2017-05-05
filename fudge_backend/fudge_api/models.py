# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def upload_to(instance, filename):
    return 'thumbnail/{}/{}'.format(instance.id, filename)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        abstract = True
        ordering = ('created_date',)


class Budget(BaseModel):
	"""Budget is the object that manages incomes/expenses/accounts"""
	name = models.CharField(max_length=100, blank=True, default='')
	balance = models.FloatField(default=0.0)
	total_income = models.FloatField(default=0.0)
	total_expenses = models.FloatField(default=0.0)


class Transaction(BaseModel):
	amount = models.FloatField(default=0.0)
	notes = models.CharField(max_length=300, blank=True, default='')
	budget = models.ForeignKey(Budget, related_name='transactions')


class Category(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)
	transaction = models.ForeignKey(Transaction, related_name='category')


class Subcategory(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)
	category = models.ForeignKey(Category, related_name='subcategories')
	transaction = models.ForeignKey(Transaction, related_name='subcategory')


class Account(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)
	budget = models.ForeignKey(Budget, related_name='accounts')

