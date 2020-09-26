from django.contrib import admin
from django.urls import path

from webapp.views.product_view import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.review_view import ReviewCreateView, ReviewUpdateView, ReviewDeleteView
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_view/add/<int:pk>/', ReviewCreateView.as_view(), name='review_add'),
    path('product_view/<int:pk>/update_review', ReviewUpdateView.as_view(), name='review_update'),
    path('product_view/<int:pk>/delete_review', ReviewDeleteView.as_view(), name='review_delete')
]