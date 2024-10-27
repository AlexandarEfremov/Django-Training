from furry_funnies.author.models import Author


def get_profile():
    try:
        return Author.objects.first()
    except Author.DoesNotExist:
        return None