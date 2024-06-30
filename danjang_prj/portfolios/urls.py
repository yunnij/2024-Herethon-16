from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views
from .views import PortfolioViewSet

portfolio_router = SimpleRouter()
portfolio_router.register('portfolios', PortfolioViewSet, basename='portfolio')

urlpatterns = [
    path('', include(portfolio_router.urls)), # /portfolios/
    # Mixin
    path('portfolio/list', views.PortfolioListMixins.as_view()),
    path('portfolio/<int:pk>/', views.PortfolioDetailMixins.as_view()),
]

