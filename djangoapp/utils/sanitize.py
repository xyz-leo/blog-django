import bleach

ALLOWED_TAGS = [
    'p', 'b', 'i', 'strong', 'em', 'u',
    'ul', 'ol', 'li', 'br', 'a', 'blockquote',
    'code', 'pre', 'h1', 'h2', 'h3', 'img'
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'img': ['src', 'alt'],
    'pre': ['data-language'] # Code mirror
}


def sanitize_html(html: str) -> str:
    """Sanitize Summernote HTML content to prevent XSS."""
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        strip=True
    )
