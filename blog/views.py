from django.shortcuts import render
from django.views import generic

from .models import Post

class PostsIndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:5]

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def writepost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    try:
        selected_choice = post.choice_set.get(pk=request.POST['title'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'post': post,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Vote.objects.create(user=request.user, question=question)
        return HttpResponseRedirect(reverse('blog:posts', args=(question.id,)))
