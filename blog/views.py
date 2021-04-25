from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone
from django.views.generic import (TemplateView,DetailView,ListView,
                                  UpdateView,DeleteView,CreateView)


# Create your views here.


def user_login(request):
    # print('k')
    if request.method == 'POST':
        # print('k1')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)

        user = authenticate(username=username,password=password)
        print(user)
        if user:
            print('k2')
            if user.is_active:
                print('k7')
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('blog/post_list.html')
        else:
            # print('k3')
            print('error')
            return render(request,'registeration/login.html',{})
    else:
        # print('k4')
        return render(request,'registeration/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:post_list'))

@login_required
def publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    post.save()
    return HttpResponseRedirect('/draft')

class AboutView(TemplateView):
    template_name = 'blog/post_about.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'ListL'
    template_name = 'blog/post_list.html'


    def get_queryset(self):

        return Post.objects.all().order_by('published_date')
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog:post_detail'
    form_class = PostForm
    model = Post
    template_name = 'blog/post_create.html'

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/post_update.html'

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class DraftView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'DraftL'
    template_name = 'blog/post_draft_list.html'

    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('published_date')

#######################################################################
######################  COMMENTS  #####################################


def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user.username
            comment.save()

            return redirect('blog:post_detail',pk=post.pk)

    else:
        form = CommentForm()
        return render(request,'blog/post_detail.html',{'form1':form,'post':post})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    pks=comment.post.pk
    return redirect('blog:post_detail',pk=pks)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)







