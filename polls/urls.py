from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entry/<int:entry_id>/results/', views.entry_results, name='entry_results'),
    path('entry/<int:entry_id>/vote/', views.entry_vote, name='entry_vote'),

    path('invest/<int:investment_id>/', views.investment_detail, name='investment_detail'),
    path('invest/<int:investment_id>/results/', views.investment_results, name='investment_results'),
    path('invest/<int:investment_id>/vote/', views.investment_vote, name='investment_vote'),
]
