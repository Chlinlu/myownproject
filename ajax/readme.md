# Django with ajax

## 一.环境

创建虚拟环境

```python
python -m venv venv
```

使用虚拟环境

```python
.\venv\Scripts\activate
```

镜像

```python
 pip packgename -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

安装django包

```python
>pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 二.创建工程和APP

新建工程

```python
django-admin startproject backend
```

创建APP

```python
python manage.py startapp appname
```

## 三.模板与视图

创建model

models.py

```python
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)

```

注册到admin

admin.py

```python
from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)

```

view.py

```python
from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles": list(profiles.values())})


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']

        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()
        return HttpResponse('New Profile Created Successfully')
```

templates

```html
##index.html

{% extends 'base.html' %}
{% block content %}
    <h1>Submit Form</h1>
    <Form id="post-form" method="POST">
        {% csrf_token %}  
        <p>Name</p><input type="text" name="name" id="name"/><br>
        <p>Email</p><input type="text" name="email" id="email"/><br>
        <p>Bio</p><input type="text" name="bio" id="bio"/><br>
        <input type="submit" />
    </form>
{% endblock %}

{% block script %}
$(document).on('submit','#post-form',function(e){
    e.preventDefault();
        $.ajax({
            type:'POST',
            url : "{% url 'create' %}",  
            data:{
                name:$('#name').val(),
                email:$('#email').val(),
                bio:$('#bio').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            }, 
            success: function(data){
              alert(data); 
            },
        });
});
{% endblock %}


```

```html
##base.html
<!DOCTYPE html>
<html>

<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

    {% if title %}
    <title>Ajax - {{ title }}</title>
    {% else %}
    <title>Ajax</title>
    {% endif %}
</head>

<body>
    <main role="main" class="container">
        <div class="row">
            <div class="col-md-8">
                {% if messages %}
                {% for message in messages %}
                <div class="alert-{{ message.tags}}">
                    {{ message }}
                </div>
                {% endfor%}
                {% endif %}
                {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
                <div class="content-section">
                    <h3>Our Sidebar</h3>
                    <p class='text-muted'>You can put any information here you'd like.
                    <ul class="list-group">
                        <li class="list-group-item list-group-item-light">Latest Posts</li>
                        <li class="list-group-item list-group-item-light">Announcements</li>
                        <li class="list-group-item list-group-item-light">Calendars</li>
                        <li class="list-group-item list-group-item-light">etc</li>
                    </ul>
                    </p>
                </div>
            </div>
        </div>
    </main>
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js" integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ" crossorigin="anonymous"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
    <script>{%block script %}{%endblock%}</script>
    
</body>

</html>
```

