from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='contacts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('categories/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('export/', views.export_contacts, name='export_contacts'),
    path('import/', views.import_contacts, name='import_contacts'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
