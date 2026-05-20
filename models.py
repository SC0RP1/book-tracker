from dataclasses import dataclass


@dataclass
class Book:
    author: str
    title: str
    rating: int
    date_read: str

    def to_dict(self):
        return {
            'author': self.author,
            'title': self.title,
            'rating': self.rating,
            'date_read': self.date_read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            author=data['author'],
            title=data['title'],
            rating=data['rating'],
            date_read=data['date_read']
        )

    def __str__(self):
        return f"{self.author} - {self.title} (Оценка: {self.rating}, Дата: {self.date_read})"