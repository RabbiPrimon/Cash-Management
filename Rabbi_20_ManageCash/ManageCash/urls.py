from django.urls import path
from ManageCash.views import *

urlpatterns = [
  path('',login_function,name="login"),
  path('register/',register_function,name="register"),
  path('logout/',logout_function,name="logout"),
  path('dashboard/',dashboard_function,name="dashboard"),
  path('add-cash/',add_cash_function,name="add_cash"),
  path('add-expense/',add_expense_function,name="add_expense"),
  path('profile/',profile_function,name="profile"),
  path('home/',home_function,name="home"),
]
