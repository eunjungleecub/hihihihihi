from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):    #   ModelForm

    class Meta: 

        model = Post # model에 정의된 class Post에서
        fields = ['title', 'author', 'content'] # 사용자로부터 여기에 적어준 field 데이터를 직접 입력받는다. 
        labels = {
            'title':'제목',
            'author':'글쓴이',
            'content':'내용',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields=['c_author', 'c_content']
        labels={
            'c_author':'글쓴이',
            'c_content':'내용',
        }