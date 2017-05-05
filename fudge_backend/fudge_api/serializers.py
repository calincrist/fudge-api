# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Subcategory, Category, Budget, Transaction, Account


class BudgetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Budget
		fields = '__all__'
