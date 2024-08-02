from django.urls import path
from blog.views import BlogView, index, LoginView, RegisterView, MyblogsView, BlogcredView, LogoutView

urlpatterns=[
  path("", index),
  path("allblog", BlogView.as_view()),
  path("login", LoginView.as_view()),
  path("register", RegisterView.as_view()),
  path("logout", LogoutView.as_view()),
  path("myblogs", MyblogsView.as_view()),
  path("myblogs/<int:pk>", BlogcredView.as_view())
]