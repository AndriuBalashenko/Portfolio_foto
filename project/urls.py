from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import CategoryListView, PostByCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', PostByCategoryView.as_view(), name='post-by-category'),]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
