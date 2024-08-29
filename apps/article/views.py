from django.shortcuts import render, redirect

from django.core.paginator import Paginator

from .models import Article, Comment


def home(request):
    page_number = request.GET.get('page')

    articles = Article.objects.filter(is_active=True).order_by('name')

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    return render(request, 'index.html', {'articles': selected_page})

def single(request, slug):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    query = request.POST.get("search")

    article = Article.objects.filter(is_active=True, slug__iexact=slug).first()

    article.views +=1

    article.save()

    comments = Comment.objects.filter(is_active=True, article_id=article.id).order_by("-id")

    if request.method == 'POST':
        comment = Comment.objects.create(
            article_id=article.id,
            user_id=request.user.id,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            web_site=request.POST.get('web_site'),
            )
        
        comment.save()

        return redirect('single', article.slug)

    context = {
        'article': article,
        'comments': comments,
    }

    return render(request, 'blog-single.html', context)

def home_2(request):
    page_number = request.GET.get('page')

    articles = Article.objects.filter(is_active=True).order_by('name')

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    return render(request, 'index-2.html', {'articles': selected_page})

def article(request):
    page_number = request.GET.get('page')

    articles = Article.objects.filter(is_active=True).order_by('id')

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    return render(request, 'blog.html', {'articles': selected_page})
