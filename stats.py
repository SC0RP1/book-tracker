from typing import List, Dict
from models import Book


def calculate_average_rating(books: List[Book]) -> float:
    if not books:
        return 0.0

    total_rating = sum(book.rating for book in books)
    return round(total_rating / len(books), 2)


def get_statistics_by_author(books: List[Book]) -> Dict[str, Dict]:
    stats = {}

    for book in books:
        if book.author not in stats:
            stats[book.author] = {'count': 0, 'total_rating': 0}

        stats[book.author]['count'] += 1
        stats[book.author]['total_rating'] += book.rating

    for author in stats:
        stats[author]['average_rating'] = round(
            stats[author]['total_rating'] / stats[author]['count'], 2
        )

    return stats