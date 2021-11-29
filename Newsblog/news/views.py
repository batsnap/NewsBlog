from django.db.models.base import Model
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from .models import Post
from .form import CommentForm

def main(request):
    return render(request,'news/base.html')

def category_post_list(request,slug):
    posts=Post.objects.all().filter(categorys=slug)
    return render(request,'news/post/list.html',{'posts':posts})

def category_one_post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'news/post/news.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})
