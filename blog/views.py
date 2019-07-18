from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post #  'blog/models.py'에서 Post 가져오기
from .forms import PostForm, CommentForm # 'blog/forms.p' 에서 PostForm 가져오기

def main(request):
    return render(request, 'main.html')
    
def popup(request):
    return render(request, 'wangtise.html')


def intro(request):
    return render(request, 'intro.html')
    
def home(request):  #   'posts list' 페이지 
    posts = Post.objects # Post의 객체들을 posts 변수에 담아주기
    return render(request, 'postslist.html', {'posts':posts}) 
    # postslist.html을 가져오기, 'posts'를 호출하면 아까 posts에 담아준 Post의 object들을 가져오라. 

def post_create(request):   #생성

    if request.method == 'POST': #사용자가 form에 데이터를 적어서 POST 방식으로 제출할때
        form = PostForm(request.POST) # 그 값을 request에 저장하기
        if form.is_valid(): # 이때 form이 유효하다면
            form.save() # form을 저장하고
            return redirect('home') # url = 'home' 으로 오기
    
    else:
        form = PostForm() # POST 방식이 아닐때 == 저장하는게 아니고 form에 내용 입력하려고 처음 열 때
    return render(request, 'postcreate.html', {'form': form}) # form 생성


def post_detail(request, pk):  # pk=primary key: 게시물 고유번호
    post = get_object_or_404(Post, pk=pk) # get_object_or_404: object를 가져오거나 없으면 404 에러를 내기

    return render(request, 'postdetail.html', {'post': post})
    # 'postdetail.html'을 가져오기, 'post'를 호출하면 get_object_or_404 실행


def post_update(request, pk):   #수정하기

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST': 
        form = PostForm(request.POST, instance=post) # post 인스턴스를 받아서 그 안에 써있는 내용 불러오기
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'postupdate.html', {'form':form})


def post_delete(request, pk):   # 삭제 기능
    post = Post.objects.get(pk=pk)  # get방식으로 가져온 Post.objects를 post에 담기
    post.delete() # delete 함수 실행
    return redirect('home') # 완료되면 'home' 으로 가기

def comments(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'addcomment.html', {'form': form})
