from django.contrib import admin
from django.urls import path, include
from todo_app.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include("core.urls"), name="to-do"),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]
