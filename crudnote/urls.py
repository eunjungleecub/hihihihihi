from django.contrib import admin
from django.urls import path, include #    import include --> 앱 blog의 urls.py 안으로 url 정리

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('blog.urls')),    #    blog/urls.py 안에 url 작성 --> '/blog/~~~~~'
    path('accounts/', include('accounts.urls')),

]
