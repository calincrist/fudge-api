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
	"""
	Budget is the object that manages incomes/expenses/accounts
	"""
	name = models.CharField(max_length=100, blank=True, default='')
	balance = models.FloatField(default=0.0)
	total_income = models.FloatField(default=0.0)
	total_expenses = models.FloatField(default=0.0)

	def __unicode__(self):
		return '%s: %s' % (self.name, str(self.balance))

	def transaction_list(self):
		return Transaction.objects.filter(budget=self)


class Category(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)

	def __unicode__(self):
   		return '%s' % (self.name)   

	def subcategory_list(self):
		return Subcategory.objects.filter(category=self)

	def transaction_list(self):
		return Transaction.objects.filter(category=self)



class Transaction(BaseModel):
	amount = models.FloatField(default=0.0)
	notes = models.CharField(max_length=300, blank=True, default='')
	budget = models.ForeignKey(Budget, related_name='transactions', null=True)
	category = models.ForeignKey(Category, related_name='transaction', null=True)

	def __unicode__(self):
		return '%s: %s' % (str(self.amount), self.notes)


class Subcategory(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)
	category = models.ForeignKey(Category, related_name='subcategories')
	transaction = models.ForeignKey(Transaction, related_name='subcategory', null=True)

	def __unicode__(self):
		return '%s' % (self.name)


class Account(BaseModel):
	name = models.CharField(max_length=100, blank=True, default='')
	email = models.CharField(max_length=100, blank=True, default='')
	thumbnail = models.ImageField(blank=True, null=True, upload_to=upload_to)
	budget = models.ForeignKey(Budget, related_name='accounts', null=True)

