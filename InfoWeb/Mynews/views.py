from django.views.generic import ListView, DetailView
from django.shortcuts import render

from Mynews.forms import PostSearchForm, RefreshForm
from Mynews.models import Post
from django.views.generic.edit import FormView
from django.db.models import Q
import os
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = "Mynews/post_all.html"
    context_object_name = "posts" #object_list 
    
    paginate_by = 10
class PostDV(DetailView):
    model = Post
    template_name = "Mynews/post_detail.html"
class SearchFormView(FormView):
    form_class = PostSearchForm # forms.py에 생성
    template_name = "Mynews/post_search.html"

    def form_valid(self, form):
        schword = self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schword) | Q(article__icontains=schword) | Q(writer__icontains=schword)).distinct()

        # 검색된 결과 
        context = {}
       
        context['form'] = form
        context['search_keyword'] = schword
        context['search_list'] = post_list

        return render(self.request, self.template_name, context)

class RefreshFormView(FormView):
    template_name = "Mynews/post_all.html"
    form_class = RefreshForm
    success_url = 'post/'
    context_object_name = "posts" 

    paginate_by = 10

    def form_valid(self, form):
        print(self.request)
        os.chdir('C:/Users/user/Desktop/자연어처리과정/WebProject/webcrawler')
        os.system('scrapy crawl newscrawl')
        return super().form_valid(form)