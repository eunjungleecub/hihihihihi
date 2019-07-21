{% extends "base.html" %}

{% block content %}

<div class="container">
    <h1> 회원가입 </h1>

    <form action="{% url 'signup' %}">

        {% csrf_token %}
        
        사용자 이름:
        <input name="username" type="text" value="">
        <br>
        비밀번호:
        <br>
        <input name="password1" type="password" value="">
        <br>
        비밀번호 확인:
        <br>
        <input name="password2" type="password" value="">
        <br>
        <br>
        <input class="btn btn-primary" type="submit" value="회원가입!">
    </form>

</div>

{% endblock content %}
