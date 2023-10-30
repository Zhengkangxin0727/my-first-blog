from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import JsonResponse
from .models import Keyword


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#前端向后端传参

def get_keywords(request):
    term = request.GET.get('term')  # jQuery UI Autocomplete会发送名为'term'的GET参数
    if ',' in term:
        term = term.split(',')[-1].strip()  # 如果输入包含逗号，取最后一个逗号后的字符串作为搜索关键词
    keywords = Keyword.objects.filter(name__icontains=term)  # 假设你的关键词存储在Keyword模型的name字段
    results = []
    for keyword in keywords:
        keyword_dict = {
            'id': keyword.id,
            'label': keyword.name,
            'value': keyword.name
        }
        results.append(keyword_dict)
    return JsonResponse(results, safe=False)

def g(request):
    g = 'a'
    if request.method == 'POST':
        g = request.POST.get('g')
        keywords = g.split(',')  # 分割关键词
        # 在这里你可以对关键词进行进一步的处理
        return render(request, 'blog/g.html', {'keywords': keywords})
    return render(request, 'blog/g.html', locals())