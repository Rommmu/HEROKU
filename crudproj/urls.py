from django.contrib import admin
from django.urls import path, include
import crudapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', crudapp.views.index, name='index'),
    path('', crudapp.views.main, name='main'),
    #작성한 글을 자세히 보여주는 페이지 글의 id값을 불러와야 함
    path('detail/<str:id>/', crudapp.views.detail, name='detail'),
    #글을 보여주는 페이지
    path('read/', crudapp.views.read, name = 'read'),
    #글을 작성하는 new 페이지랑 연결된 create함수
    path('new/create/', crudapp.views.create, name='create'),
    #글을 수정하는 페이지 글의 id값을 불러와야함
    path('edit/<str:id>/', crudapp.views.edit, name='edit'),
    #글을 삭제하는 페이지 글의 id값을 불러와야함
    path('delete/<str:id>/', crudapp.views.delete, name='delete'),
    path('crudapp/hashtag/', crudapp.views.hashtagform, name='hashtag'),
    path('crudapp/<int:hashtag_id>/search/', crudapp.views.search, name='search'),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)