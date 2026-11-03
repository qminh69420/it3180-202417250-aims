def search_by_category(items, category):
    return [
        dvd for dvd in items
        if dvd.category.casefold() == category.casefold()
    ]


def search_by_title(items, keyword):
    return [dvd for dvd in items if keyword in dvd.title]

def search_by_title(items, keyword):
    return [
        dvd for dvd in items
        if keyword.lower() in dvd.title.lower()
    ]
