from django.contrib import admin
from django.urls import path
from src.my_app.views import MyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', MyView.as_view()),
    path('test-post/', MyView.as_view())
]
