from apps.article.models import Article, Category, Tag


def object(request):
    latest_news = Article.objects.filter(is_active=True).order_by('-id')
    tags = Tag.objects.filter(is_active=True).order_by("name")
    categories = Category.objects.filter(is_active=True).order_by("name")
    recent_blogs = latest_news.order_by('id')

    return {
        'latest_news': latest_news[:2],
        'tags': tags,
        'categories': categories,
        'recent_blogs': recent_blogs[:3],
    }
