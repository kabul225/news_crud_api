from django.urls import path
from . views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", NewsList.as_view(), name="news" ),
    path("news/<int:pk>/", NewsDetail.as_view(), name="news-detail"),
    path("news/create/", NewsCreate.as_view(), name="news-create"),
    path("news/update/<int:pk>/", NewsUpdate.as_view(), name="news-update"),
    path("news/delete/<int:pk>/", NewsDelete.as_view(), name="news-delete"),

]