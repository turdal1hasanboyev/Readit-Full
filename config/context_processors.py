from apps.article.models import Article


def object(request):
    latest_news = Article.objects.filter(is_active=True).order_by('-id')

    return {
        'latest_news': latest_news[:2],
    }
