from django.urls import path
#following line is for the function based view
from . import views
#following line is for the class based view
from .views import (    CategoryList, 
                        CompanyList, 
                        CompanyCreateView, 
                        CompanyDetailView, 
                        CompanyUpdateView,
                        CompanyDeleteView,
                        AboutView,
                        AboutUsView
                      
)
from django_filters.views import FilterView
from .filters import CompanyFilter

urlpatterns = [
    #the following path is for the test only
    # path('', views.home, name = 'home'),
    path('', CategoryList.as_view(), name = 'category_list'),
    path('company/create/', CompanyCreateView.as_view(), name = 'company_create'),
    #categories/bank/1
    path('<str:category>/<int:pk>/', CompanyDetailView.as_view(), name = 'company_detail'),
    #categories/bank/1/delete
    path('<str:category>/<int:pk>/delete/', CompanyDeleteView.as_view(), name = 'company_delete'),
    #categories/bank/1/update
    path('<str:category>/<int:pk>/update/', CompanyUpdateView.as_view(), name = 'company_update'),
    path('search/', FilterView.as_view(filterset_class=CompanyFilter, 
        template_name ='categories/company_search.html'), name='search'),
    path('about/', AboutView.as_view(), name = 'aboutknowhere'),
    path('aboutus/', AboutUsView.as_view(), name = 'aboutus'),
    # why should be this \
    # because create is taken as the string value for the category
  
    #categories/bank or categories/school
    path('<str:category>/', views.CompanyList.as_view(), name='company_list'),
    
    
]