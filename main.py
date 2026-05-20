from datetime import datetime
from models import Book
from storage import add_book, get_all_books, delete_book, find_book
from stats import calculate_average_rating, get_statistics_by_author


def get_valid_rating():
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print('Оценка должна быть от 1 до 5')
        except ValueError:
            print("Пожалуйста, введите целое число!")


def get_valid_date():
    while True:
        date_str = input("Введите дату прочтения (ГГГГ-ММ-ДД): ")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Неверный формат даты! Используйте ГГГГ-ММ-ДД")


def add_book_menu():
    print("\n--- Добавление новой книги ---")
    author = input("Введите автора: ").strip()
    title = input("Введите название: ").strip()

    if not author or not title:
        print("Автор и название не могут быть пустыми!")
        return

    rating = get_valid_rating()
    date_read = get_valid_date()

    book = Book(author, title, rating, date_read)

    if add_book(book):
        print(f"Книга '{title}' успешно добавлена!")
    else:
        print(f"Ошибка: Книга '{title}' автора {author} уже существует!")


def show_all_books():
    books = get_all_books()

    print("\n--- Список всех книг ---")
    if not books:
        print("Список книг пуст")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")


def show_average_rating():
    books = get_all_books()
    avg = calculate_average_rating(books)

    print("\n--- Средняя оценка всех книг ---")
    if avg == 0:
        print("Нет книг для оценки")
    else:
        print(f"Средняя оценка: {avg}")


def show_author_statistics():
    books = get_all_books()
    stats = get_statistics_by_author(books)

    print("\n--- Статистика по авторам ---")
    if not stats:
        print("Нет книг для статистики")
    else:
        for author, data in stats.items():
            print(f"{author}: {data['count']} книг(а), средняя оценка: {data['average_rating']}")


def delete_book_menu():
    print("\n--- Удаление книги ---")
    author = input("Введите автора: ").strip()
    title = input("Введите название: ").strip()

    book = find_book(author, title)
    if not book:
        print(f"Книга '{title}' автора {author} не найдена!")
        return

    print(f"Найдена книга: {book}")
    confirm = input("Удалить? (д/н): ").lower()

    if confirm == 'д' and delete_book(author, title):
        print(f"Книга '{title}' успешно удалена!")
    else:
        print("Удаление отменено или не выполнено.")


def main():
    while True:
        print("\n" + "=" * 40)
        print("   ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("=" * 40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        print("-" * 40)

        choice = input("Выберите действие (1-6): ").strip()

        if choice == '1':
            add_book_menu()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_statistics()
        elif choice == '5':
            delete_book_menu()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите 1-6")


if __name__ == "__main__":
    main()