from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='janken'),
    path('janken',views.janken2, name="janken2"),
    path("result",views.result, name="result"),
    path("ranking",views.RankingListView.as_view(), name='ranking'),
    path("register",views.register, name="register"),
    path("result2",views.result2, name="result2"),
]