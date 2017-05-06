# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import viewsets

from fudge_api.models import Budget, Transaction, Category, Subcategory
from fudge_api.serializers import BudgetSerializer, TransactionSerializer, CategorySerializer, SubcategorySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'budgets': reverse('budget-list', request=request, format=format),
		'transactions': reverse('transaction-list', request=request, format=format),
		'categories': reverse('category-list', request=request, format=format),
		'subcategories': reverse('subcategory-list', request=request, format=format),
    })


class BudgetViewSet(viewsets.ModelViewSet):
    """
    Budget viewset which provides `list` and `detail` actions for budgets.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        serializer.save()

class TransactionViewSet(viewsets.ModelViewSet):
	"""
    Transaction viewset which provides `list` and `detail` actions for transactions.
    """
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	def perform_create(self, serializer):
		serializer.save()

class CategoryViewSet(viewsets.ModelViewSet):
	"""
    Category viewset which provides `list` and `detail` actions for categories.
    """
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def perform_create(self, serializer):
		serializer.save()


class SubcategoryViewSet(viewsets.ModelViewSet):
	queryset = Subcategory.objects.all()
	serializer_class = SubcategorySerializer

	def perform_create(self, serializer):
		serializer.save()


