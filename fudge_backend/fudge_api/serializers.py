# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Subcategory, Category, Budget, Transaction, Account


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('id', 'budget', 'amount', 'category', 'subcategory', 'created_date', )


class SubcategorySerializer(serializers.ModelSerializer):
	transactions = TransactionSerializer(source='transaction_list', many=True, read_only=True)
	class Meta:
		model = Subcategory
		exclude = ('transactions', )


class CategorySerializer(serializers.ModelSerializer):
	subcategories = SubcategorySerializer(source='subcategory_list', many=True, read_only=True)
	transactions = TransactionSerializer(source='transaction_list', many=True, read_only=True)
	class Meta:
		model = Category
		exclude = ('transactions', )


class BudgetSerializer(serializers.ModelSerializer):
	transactions = TransactionSerializer(source='transaction_list', many=True, read_only=True)
	class Meta:
		model = Budget
		fields = '__all__'
