from django.urls import path
from.import views
app_name='app7'
urlpatterns=[
    path('',views.index,name='index'),
    path('show_form/',views.show_form,name='show_form'),
    path('login/',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('update/<int:id>',views.update,name='update'),
]
