# 4.3 Template system

[https://docs.djangoproject.com/en/3.2/ref/templates/](https://docs.djangoproject.com/en/3.2/ref/templates/)

## 4.3.1 템플릿 변수

`{{ variable }}`

일반 프로그래밍의 변수명과 같이 이름 지정

변수의 속성에 접근할 수 있는 도트(.) 사용시 탐색 과정 (ex. foo.bar)

1. foo가 사전 타입인지 확인 > foo['bar']로 해석
2. foo의 속성을 찾고 bar라는 속성이 있는지 확인 > foo.bar로 해석
3. foo가 리스트인지 확인 > foo[bar]로 해석

정의가 되어있지 않은 변수를 사용하고자 할 때 : 빈 문자열('')로 채워줌
settings.py에 `TEMPLATE_STRING_IF_INVALID` 속성 지정을 통해 변경 가능

---

---

## 4.3.2 템플릿 필터

필터는 파이프(|) 문자 이용

`{{ name|lower }}` : name 변수의 모든 문자를 소문자로 바꿔주는 필터

`{{ text|escape|linebreaks }}` : text 변수값 중에서 특수 문자 이스케이프하고(escape), 그 결과 스트링에 HTML `<p>` 태그를 붙임(linebreaks)

`{{ bio|truncatewords:30 }}` : bio 변수값 중에서 앞에 30개의 단어만 보여주고, 줄 바꿈 문자는 없앰

`{{ list|join:" //" }}` : 필터의 인자에 빈칸이 있는 경우 따옴표로 묶어줌. 인자가 리스트인 경우 각 값을 " // "로 구분하여 이어 연결함

`{{ value|default:"nothing" }}` : value의 변수값이 False이거나 없는 경우, "nothing"으로 보여줌

`{{ value|length }}` : value 변수값의 길이를 반환함

`{{ value|striptags }}` : value 변수값에서 HTML 태그를 모두 없애줌. 100% 작동하지 않을 수도 있음.

`{{ value|pluralize }}` : 복수 접미사 필터

`{{value|pluralize:"es" }}` / `{{ value|pluralize:"ies" }}` : es, ies를 이용하는 복수 접미사 필터

`{{ first|add:second }}` : 더하기 필터. integer 타입끼리의 덧셈, 문자열끼리의 덧셈, 리스트끼리의 덧셈 모두 가능함.

---

---

## 4.3.3 템플릿 태그

`{% for %}`

리스트에 담겨 있는 항목들을 순회하면서 출력

- for 태그에 사용되는 변수들

  `forloop.counter` : 현재까지 루프를 실행한 루프 카운트 (1부터 카운트함)

  `forloop.counter0` : 현재까지 루프를 실행한 루프 카운트 (0부터 카운트함)

  `forloop.revcounter` : 루프 끝에서 현재가 몇 번째인지 카운트한 숫자 (1부터 카운트함)

  `forloop.revcounter0` : 루프 끝에서 현재가 몇 번째인지 카운트한 숫자 (0부터 카운트함)

  `forloop.first` : 루프에서 첫 번째 실행이면 True 값을 가짐

  `forloop.last` : 루프에서 마지막 실행이면 True 값을 가짐

  `forloop.parentloop` : 중첩된 루프에서 현재의 루프 바로 상위의 루프를 의미함

---

`{% if %}`

변수를 평가하여 True면 아래의 문장 실행

태그에 필터와 연산자를 사용할 수 있으나, length를 제외한 대부분의 필터가 스트링을 반환하므로 산술 연산을 할 수 없음

boolean 연산자 사용 가능. (and, or, not, and not, ==, !=, <, >, <=, >=, in, not in)

---

`{% csrf_token %}`

CSRF(Cross Site Request Forgery) 공격을 방지하기 위해 사용. <form> 엘리먼트의 첫 줄 다음에 넣으면 됨

---

`{% url %}`

소스에 URL을 하드코딩하는 것을 방지하기 위해 사용

`{% url 'namespace:view-name' arg1 arg2 %}`

namespace : urls.py 파일의 include() 함수 또는 app_name 변수에 정의한 namespace명

view-name : urls.py 파일에서 정의한 URL 패턴명

argN : view 함수에서 사용하는 인자. 여러 개인 경우 빈칸으로 구분함

---

`{% with %}`

`{% with variable = value %}` / `{% with value as variable %}`

특정 값을 변수에 저장해두는 기능. 해당 변수의 유효 범위는 with 구문 내, 즉 {% with %}에서 {% endwith %}까지임.

---

`{% load %}`

사용자 정의 태그 및 필터 로딩

`{% load somelibrary package.otehrlibrary %}` : somelibrary.py 및 package/otehrlibary.py에 정의된 사용자 정의 태그 및 필터 로딩

---

---

## 4.3.4 템플릿 주석

`{# #}` : 한 줄 주석문

`{% comment %} - {% endcomment %}` : 여러 줄 주석문

---

---

## 4.3.5 HTML 이스케이프

`name = "<b>username"`인 상태에서, 템플릿 코드에 `Hello, {{ name }}` 을 사용하면 `Hello, <b>username` 으로 나타남. 엡 브라우저에 표시될 때, `<b>` 태그 이후의 문장을 모두 볼드체로 바꾸기 때문에 다른 결과가 나타남 ⇒ XSS(Cross Site Scripting) 공격이 이루어지는 방식

사용자가 입력한 데이터를 그대로 렌더링하는 것은 위험하므로 django는 자동 이스케이프 기능을 제공함.
< - &lt;, > - &gt;, ' - &#39;, " - &quot;, & - &amp;

- 자동 HTML 이스케이프 태그를 비활성화시켜야 하는 경우

  1. _safe필터를 사용 : `{{ date|safe }}`_
  2. **{% autoescape %} 태그 사용 : `{% autoescape off %} - {% endautoescape %}`**

> 필터의 인자에 사용되는 스트링 리터럴에는 자동 이스케이프 기능이 적용되지 않으므로 두번째 방법을 사용하는 것이 좋음.

---

---

## 4.3.6 템플릿 상속

`{% extends %}`

템플릿 전체의 모습을 구조화할 수 있어 코드의 재사용이나 변경이 용이하고, 사이트 UI의 룩앤필을 일관되게 가져갈 수 있음

```html
<!-- base.html - 부모 템플릿 -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}My amazing site{% endblock %}</title>
  </head>

  <body>
    <div id="sidebar">
      {% block sidebar %}
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/blob/">Blog</a></li>
      </ul>
      {% endblock %}
    </div>

    <div id="content">{% block content %}{% endblock%}</div>
  </body>
</html>
```

```html
<!-- base_site.html - 자식 템플릿 -->
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}
{%block content %}
{% for entry in blog_entries %}
  <h2>{{ entry.title}}</h2>
  <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```

```html
<!-- 출력 결과 -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="sytlesheet" href="sytle.css" />
    <!-- 부모 템플릿의 title 블록으로부터 상속받아 자식 템플릿에서 정의한 내용으로 오버라이딩 -->
    <title>My amazing blog</title>
  </head>

  <body>
    <div id="sidebar">
      <!-- 부모 템플릿의 sidebar 블록으로부터 상속받은 부분. 자식 템플릿에서 정의하지 않아 코드를 그대로 사용 -->
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/blog/">Blog</a></li>
      </ul>
    </div>

    <div id="content">
      <!-- 부모 템플릿의 content 블록으로부터 상속받아 자식 템플릿에서 정의한 내용으로 오버라이딩 -->
      <h2>Entry one</h2>
      <p>This is my first entry.</p>

      <h2>Entry two</h2>
      <p>This is my second entry.</p>
    </div>
  </body>
</html>
```

- 템플릿 상속의 단계

  1. 사이트 전체의 룩앤필을 담고 있는 base.html 생성
  2. 사이트 하위의 섹션별 스타일을 담고 있는 템플릿을 만듦. 2단계 템플릿들은 1단계의 base.html을 상속받음
  3. 개별 페이지에 대한 템플릿을 만듦. 3단계 템플릿은 2단계 템플릿 중 적절한 템플릿을 상속받음.
  <p>

- 템플릿 상속시 유의사항

  `{% extends %}` 태그는 사용하는 태그 중에서 가장 먼저 나와야 함.

  템플릿을 공통사항을 가능한 많이 뽑아 1단계 부모 템플릿에 {% block %} 태그가 많아질수록 좋음.

  부모 템플릿의 내용을 그대로 사용하면서 자식 템플릿에서 내용울 추가하는 경우 `{{ block.super }}` 변수를 사용하면 됨.

  가독성을 위해 `{% endblock content %}` 처럼 블록명을 기입해도 됨.
