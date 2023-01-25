from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import News


class CustomLoginView(LoginView):
    template_name = "news/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("news")

class RegisterPage(FormView):
    template_name = "news/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("news")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)

class NewsList(LoginRequiredMixin,ListView):
    model = News
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = context["news"].filter(user=self.request.user)
        return context

class NewsDetail(LoginRequiredMixin,DetailView):
    model = News
    context_object_name = "news_detail"

class NewsCreate(LoginRequiredMixin,CreateView):
    model = News
    fields = ['title','descriptiom']
    success_url = reverse_lazy("news")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(NewsCreate,self).form_valid(form)

class NewsUpdate(LoginRequiredMixin,UpdateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy("news")

class NewsDelete(LoginRequiredMixin,DeleteView):
    model = News
    context_object_name = "news_delete"
    success_url = reverse_lazy("news")