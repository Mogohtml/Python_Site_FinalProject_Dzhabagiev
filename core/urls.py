from django.urls import path

from core.views import home, create_post, post_detail, post_list, \
    rental_list, create_rental, transaction_list, transaction_detail, create_transaction, rental_detail, register, \
    user_login, user_logout, approve_post, clothes_list, clothes_detail, create_clothes

urlpatterns = [
    # Home
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
    # Authentication
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    # Post URLs
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('approve_post/', approve_post, name='approve_post'),
    # RentalRequest URLs
    path('rentals/', rental_list, name='rental_list'),
    path('rentals/<int:pk>/', rental_detail, name='rental_detail'),
    path('create_rental/', create_rental, name='create_rental'),
    # Transactions URLs
    path('transactions/', transaction_list, name='transaction_list'),
    path('transactions/<int:pk>/', transaction_detail, name='transaction_detail'),
    path('create_transaction/', create_transaction, name='create_transaction'),
    # Clothes URLs
    path('clothes/', clothes_list, name='clothes_list'),
    path('clothes/<int:pk>/', clothes_detail, name='clothes_detail'),
    path('create_clothes/', create_clothes, name='create_clothes'),
]
