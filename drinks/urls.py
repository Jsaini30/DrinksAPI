from cgitb import html
from django.contrib import admin
from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="TESTING JASHAN'S API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.jashan.com/policies/terms/",
        contact=openapi.Contact(email="contact@jashan.local"),
        license=openapi.License(name="JASHAN "),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', views.drink_list),
    path('drinks/<int:pk>', views.drink_detail),
    path('writers/', views.WritersAPI.as_view()),
    path('writers/<int:pk>', views.WriterAPI.as_view()),
    path('books/', views.BooksAPI.as_view()),
    path('books/<int:pk>', views.BookAPI.as_view()),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]


#urlpatterns = format_suffix_patterns(urlpatterns)
