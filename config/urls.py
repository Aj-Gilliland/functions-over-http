from django.contrib import admin
from django.urls import path
from app.views import heyDude, ageCal, orderUp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hey/<name>", heyDude),
    path("age-in/<int:end>/<int:birthyear>", ageCal),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", orderUp),
]
