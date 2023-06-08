from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join, name="join"),
    path('author/', views.author, name="author"),
    path('order/', views.order, name="order"),
    path('customer/', views.customer, name="customer"),
    path('staff/', views.staff, name="staff"),
    path('payment/', views.payment, name="payment"),
    path('address/', views.address, name="address"),
    path('book/', views.book, name="book"),
    path('store/', views.store, name="store"),
    path('newAuthor/', views.newAuthor, name="newAuthor"),
    path('newStaff/', views.newStaff, name="newStaff"),
    path('newCustomer/', views.newCustomer, name="newCustomer"),
    path('newPayment/', views.newPayment, name="newPayment"),
    path('newOrder/', views.newOrder, name="newOrder"),
    path('newAddress/', views.newAddress, name="newAddress"),
    path('newBook/', views.newBook, name="newBook"),
    path('newStore/', views.newStore, name="newStore"),
]
