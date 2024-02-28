from django.urls import path
from rest_framework.authtoken import views as auth_view
from . import views

urlpatterns=[
    # path('login', auth_view.ObtainAuthToken.as_view(), name='login-user'),
    # path('user', views.UserRegisterEndpoint.as_view(), name='create-users'),
    path('category', views.UpgradedCategoryEndpoint.as_view(), name='category'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category_single'),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name='category_delete'),
    # path('category', views.AddCategoryEndpoint.as_view(), name='category'),
    # path('products', views.ProductEndpoint.as_view(), name='products'),
    path('products', views.ProductEndpoint.as_view(), name='products'),
    path('products-list', views.ProductListEndpoint.as_view(), name='products-list'),
    path('products/<int:product_id>/', views.ProductDetailEndpoint.as_view(), name='products-detail'),
    
]