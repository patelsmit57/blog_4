from django.shortcuts import render
from .models import BlogModel, CommentModel
from .forms import CommentForm
from django.http import HttpResponseRedirect, request
from django.urls import reverse

# Create your views here.

def index(request):
    blog = BlogModel.objects.all().order_by('-date')[:3]
    return render(request, 'posts/index.html', {'blog' : blog})

def all_blog(request):
    blog = BlogModel.objects.all().order_by('-date')
    return render(request, 'posts/all_blog.html', {'blog' : blog})


def session_check(request, blog, key_value):
    stored_posts = request.session.get(key_value)
    # is_true = False
    if stored_posts:
        is_true = str(blog.id) in stored_posts
    else:
        is_true = False
    return is_true


def blog_detail(request, slug):
    blog = BlogModel.objects.get(slug=slug)
    # co = CommentModel.objects.filter(post=blog)
    co = blog.commentmodel_set.all().order_by('-id')

    session = session_check(request, blog, 'stored_posts')
    # print(session)

    favorited = session_check(request, blog, 'favrite1')
    # favorited = False
    # if request.session['favrite1'] == str(blog.slug):
    #     favorited = True

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # user_name = request.POST['user_name']
            # text = request.POST['text']
            # post = blog
            # comm = CommentModel(user_name=user_name, text=text, post=post)
            # comm.save()
            
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()

            return HttpResponseRedirect(reverse('blog_detail', args=[slug]))
        return render(request, 'posts/blog_detail.html', {'blog' : blog, 'forms' : form, 'comment' : co, 'is_favorite' : favorited, 'session': session})
    form = CommentForm()
    return render(request, 'posts/blog_detail.html', {'blog' : blog, 'forms' : form, 'comment' : co, 'is_favorite' : favorited, 'session': session})


def favorite(request):
    if request.method == 'POST':
        stored_favrite = request.session.get('favrite1')
        if stored_favrite is None:
            stored_favrite = []
        
        hidden = request.POST['blog_id_favorite']

        if hidden not in stored_favrite:
            stored_favrite.append(hidden)
        else:
            stored_favrite.remove(hidden)
        
        request.session['favrite1'] = stored_favrite
        print(request.session['favrite1'])
        b = BlogModel.objects.get(id=hidden)
        return HttpResponseRedirect(reverse('blog_detail', args=[b.slug]))


def read_later(request):
    if request.method == 'POST':
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []

        post_id = request.POST['blog_id']
        # print(post_id)
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session['stored_posts'] = stored_posts
    
        return HttpResponseRedirect('/blog/')
    
    stored_posts = request.session.get('stored_posts')
    has_post = True
    if stored_posts is None or len(stored_posts) == 0:
        posts = []
        has_post = False
    else:
        posts = BlogModel.objects.filter(id__in = stored_posts)
    # print(posts)
    return render(request, 'posts/stored_post.html', {'post':posts, 'has_post':has_post})
