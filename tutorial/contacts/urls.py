from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='index'),
    path('add/', views.ContactList.post, name="add_contact"),
    path('update/<int:contact_id>', views.ContactDetail.put),
    path('delete/<int:contact_id>', views.ContactDetail.delete)
    #path('contacts/<int:pk>/', views.ContactDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)