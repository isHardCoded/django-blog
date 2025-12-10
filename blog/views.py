from django.shortcuts import render

def home(request):
    news = [
        {'title': 'Первая новость', 'content': 'Содержимое первой новости.'},
        {'title': 'Вторая новость', 'content': 'Содержимое второй новости.'},
        {'title': 'Третья новость', 'content': 'Содержимое третьей новости.'}
    ]
    
    context = {
        'news_list': news  # ключ - имя переменной в шаблоне, значение - данные
    }
    
    return render(request, 'blog/home.html', context)
