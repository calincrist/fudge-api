# -*- coding: utf-8 -*-s
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from fudge_api.views import BudgetViewSet, TransactionViewSet, CategoryViewSet, SubcategoryViewSet, api_root, TransactionByBudget
from rest_framework import renderers
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'budgets', BudgetViewSet)
# router.register(r'transactions', BudgetViewSet)
# router.register(r'categories', BudgetViewSet)
# router.register(r'subcategories', BudgetViewSet)

# urlpatterns = router.urls
# urlpatterns += format_suffix_patterns([
#     url(r'^$', api_root),
# ])


resource_methods = {
    'get': 'list',
    'post': 'create'
}

resource_details_methods = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

budget_list = BudgetViewSet.as_view(resource_methods)
budget_detail = BudgetViewSet.as_view(resource_details_methods)

transaction_list = TransactionViewSet.as_view(resource_methods)
transaction_detail = TransactionViewSet.as_view(resource_details_methods)
transactionbybudget = TransactionByBudget.as_view(resource_methods)

subcategory_list = SubcategoryViewSet.as_view(resource_methods)
subcategory_detail = SubcategoryViewSet.as_view(resource_details_methods)

category_list = CategoryViewSet.as_view(resource_methods)
category_detail = CategoryViewSet.as_view(resource_details_methods)



urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^budgets/$', budget_list, name='budget-list'),
    url(r'^budgets/(?P<pk>[0-9]+)/$', budget_detail, name='budget-detail'),
    url(r'^budgets/(?P<budget_pk>.+)/transactions/$', transactionbybudget, name='transactionbybudget-list'),

    url(r'^transactions/$', transaction_list, name='transaction-list'),
    url(r'^transactions/(?P<pk>[0-9]+)/$', transaction_detail, name='transaction-detail'),

    url(r'^categories/$', category_list, name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', category_detail, name='category-detail'),

    url(r'^subcategories/$', subcategory_list, name='subcategory-list'),
    url(r'^subcategories/(?P<pk>[0-9]+)/$', subcategory_detail, name='subcategory-detail'),
])
