from django.utils.text import slugify

def make_slug(text):
    if not text:
        return text
    return slugify(text, allow_unicode=True)