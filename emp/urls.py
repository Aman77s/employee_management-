
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.emp_home , name='home'),
    path("add_emp/", views.add_emp, name='add_emp'),
    path("delete-emp/<int:emp_id>", views.delete_emp, name='delete_emp'),
    path("update-emp/<int:emp_id>", views.update_emp, name='update_emp'),
    path("do-update-emp/<int:emp_id>", views.do_update_emp, name='do_update_emp'),
    path('search_results/', views.search , name='search_results'),
]
