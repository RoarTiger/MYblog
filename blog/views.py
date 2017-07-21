from django.shortcuts import render

def blog(request):
    return render(request, 'blog.html', locals())

def article(request):
    return render(request, 'article.html', locals())

def editor(request):
    return render(request, 'markdownEditor.html', locals())

def test(request):
    return render(request, 'marktest.html', locals())