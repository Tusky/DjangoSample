from blog.models import Category


def get_categories(request):
    return {
        'categories': Category.objects.filter(post__active=True).distinct()
    }
