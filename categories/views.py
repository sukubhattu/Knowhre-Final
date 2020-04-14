from django.shortcuts import render, get_object_or_404
from .models import Category, Company
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import CommentForm
from django.views.generic.edit import FormMixin
# Create your views here.
def home(request):
    return HttpResponse("<H1> Hello welcome to my page </H1>")

class CategoryList(ListView):
    model = Category
    context_object_name = 'companies'
    template_name = 'categories/category_list'
    paginate_by = 3

class CompanyList(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'categories/company_list.html'

    def get_queryset(self):
        category = get_object_or_404(Category, name = self.kwargs.get('category'))
        return Company.objects.filter(category = category)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["category"] = self.category
    #     return context
        
class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'categories/company_create.html'
    fields = ['name', 'description', 'latitude', 'longitude', 'category']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Company
    template_name = 'categories/company_update.html'
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        company = self.get_object()
        if self.request.user == company.owner:
            return True
        return False


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    template_name = 'categories/company_delete.html'
    success_url = '/categories'
    def test_func(self):
    	company = self.get_object()
    	if self.request.user == company.owner:
    		return True
    	return False



class CompanyDetailView(DetailView):
    model = Company
    template_name = 'categories/company_detail.html'



def search(request):
    company_list = Company.objects.all()
    company_filter = CompanyFilter(request.GET, queryset=company_list)
    return render(request, 'categories/category_list.html', {'filter': company_filter})


class AboutView(TemplateView):
    template_name = 'categories/aboutknowhere.html'

class AboutUsView(TemplateView):
    template_name = 'categories/aboutus.html' 
