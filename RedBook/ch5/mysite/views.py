from django.views.generic.base import TemplateView
from django.apps import apps

# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # app name 이용
        # context['app_list'] = ['polls', 'books']
        
        # context['app_list'] 대신 apps.py의 verbose_name 이용
        dictVerbose = {}
        for app in apps.get_app_configs():
            # app.path : 각 설정 클래스의 path 속성으로 app dir의 물리적 경로 (books - ..\ch5\books)
            # 물리적 경로에 site-packages 문자열이 들어있다 == 외부 라이브러리 앱 >> 제외
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
                # ex. label - books, verbose_name - Book-Author-Publisher App
        context['verbose_dict'] = dictVerbose

        return context