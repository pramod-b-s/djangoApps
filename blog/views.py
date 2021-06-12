from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post, CreatePollForm

class PostsIndexView(generic.ListView):
    template_name = 'blog/userposts.html'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:5]


class AllPostsIndexView(generic.ListView):
    template_name = 'blog/allposts.html'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:5]


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def post_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreatePollForm(request.POST)

            if form.is_valid():    
                form.instance.date = timezone.now()        
                form.instance.author = request.user
                form.save()
                post_list = Post.objects.all()
                pcontext = { 'post_list' : post_list }
                return HttpResponseRedirect(reverse('blog:all_posts'))
        else:
            form = CreatePollForm()

        context = {'form' : form}
        return render(request, 'blog/create.html', context)
    else:
        HttpResponseRedirect(reverse('main:login'))
