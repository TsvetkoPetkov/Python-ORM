import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    authors = Author.objects.all()

    if search_name is not None:
        authors = authors.filter(
            full_name__icontains=search_name
        )
    if search_email is not None:
        authors = authors.filter(
            email__icontains=search_email
        )

    ordered_authors = authors.order_by('-full_name')

    if not authors:
        return ""

    return '\n'.join(
        f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}"
        for author in ordered_authors
    )


def get_top_publisher():
    top_author = Author.objects.annotate(article_count=Count('article')).order_by('-article_count', 'email').first()

    if not top_author or top_author.article_count == 0:
        return ""
    else:
        return f"Top Author: {top_author.full_name} with {top_author.article_count} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(
        reviews_number=Count('review')
    ).order_by('-reviews_number', 'email').first()

    if not top_reviewer or top_reviewer.reviews_number == 0:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.reviews_number} published reviews."


def get_latest_article():
    all_articles = Article.objects.all()

    if not all_articles:
        return ""

    latest_article = Article.objects.prefetch_related('authors').annotate(average=Avg('review__rating')).last()

    authors = ', '.join(sorted([a.full_name for a in latest_article.authors.all()]))

    number_of_reviews = latest_article.review_set.count()

    return (f"The latest article is: {latest_article.title}. Authors: {authors}. "
            f"Reviewed: {number_of_reviews} times. Average Rating: {latest_article.average:.2f}.")


def get_top_rated_article():
    article = Article.objects.annotate(
        average_rating=Avg('review__rating')
    ).order_by(
        '-average_rating',
        'title'
    ).first()

    if article is not None and article.average_rating is not None:
        number_of_reviews = article.review_set.count()

        return (f"The top-rated article is: {article.title}, with an average rating of "
                f"{article.average_rating:.2f}, reviewed {number_of_reviews} times.")
    else:
        return ""


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author_to_ban = Author.objects.filter(email=email).first()

    if author_to_ban:
        reviews = author_to_ban.review_set.count()
        author_to_ban.is_banned = True
        author_to_ban.save()
        author_to_ban.review_set.all().delete()

        return f"Author: {author_to_ban.full_name} is banned! {reviews} reviews deleted."
    else:
        return "No authors banned."


