from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Hashtag
from .forms import PostForm, CommentForm, HashtagForm
from django.utils import timezone

# Create your views here.

#기본 부트스트랩 템플릿 페이지
def index(request):

    return render(request, 'crudapp/index.html')

#메인 페이지
def main(request):
    hashtags = Hashtag.objects
    return render(request, 'crudapp/main.html', {'hashtags':hashtags})

#글 작성하는 페이지
def new(request):
    return render(request, 'crudapp/new.html')

#글 작성하는 페이지랑 연결된 글 작성 페이지
def create(request, blog=None):
    if request.method == 'POST':
        #POST 형식으로 요청받은 form이 정보를 완전히 받았는 지 확인함
        form = PostForm(request.POST, request.FILES, instance=blog)
        #form이 다 정보를 받으면 read로 이동
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            form.save_m2m()
            return redirect('read')

    else:
        form = PostForm
        return render(request, 'crudapp/new.html',  {'form':form})

#글을 읽어오는 페이지
def read(request):
    #Post의 객체를 posts라는 변수에 담음
    posts = Post.objects
    return render(request, 'crudapp/read.html', {'posts': posts})

#글의 디테일한 부분을 보여주는 페이지
#특정 게시글을 불러오기 위해서는 글의  id값을 가져와야 하기 때문에 request, id를 써야함
def detail(request, id):
    #Post에서 id값을 잘 가져오지 못하면 404 에러를 일으킴
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)

    else:
        form=CommentForm()
        return render(request, 'crudapp/detail.html', {'post':post, 'form':form})
#글을 수정하는 페이지
#특정 게시글을  수정 하기 위해서는 글의 id값을 가져와야 하기 때문에 request, id를 써야함

def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'crudapp/edit.html',  {'form':form})

#글을 삭제하는 페이지
#특정 게시글을 삭제 하기 위해서는 글의 id값을 가져와야 하기 때문에 request, id를 써야함
def delete(request, id):
    #Post에서 id값을 잘 가져오지 못하면 404 에러를 일으킴
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'crudapp/hashtag.html', {'form':form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('index')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'crudapp/hashtag.html', {'form':form})
    
def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'crudapp/search.html', {'hashtag':hashtag})
