from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) #사용자가 직접 입력하지 않아도 자동으로 시간 받아오기
    content = models.TextField(default='') #default='', content에 아무것도 안써도 null 에러 안나게 하기

    def __str__(self): # title: 사용자가 입력한대로 string으로 불러오기
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    c_author = models.CharField(max_length=100, default="익명")
    c_content = models.TextField(default='')
    c_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

    

    

    