import re


def normalize_text(value: str) -> str:
    """Remove all non-alphanumeric characters and lowercase the text."""
    if not value:
        return ''
    return re.sub(r'\W+', '', value).lower()
