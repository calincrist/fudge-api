# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Subcategory, Category, Budget, Transaction, Account


class SubcategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Subcategory
		fields = ('id', 'name', 'thumbnail', 'category', )


class CategorySerializer(serializers.ModelSerializer):
	subcategories = SubcategorySerializer(source='subcategory_list', many=True, read_only=True)
	class Meta:
		model = Category
		fields = ('id', 'name', 'thumbnail', 'subcategories', )

class TransactionSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=False, read_only=False)
	class Meta:
		model = Transaction
		fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
	transactions = TransactionSerializer(source='transaction_list', many=True, read_only=True)
	class Meta:
		model = Budget
		fields = '__all__'
