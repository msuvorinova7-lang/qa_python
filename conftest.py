import pytest
from books_collector import BooksCollector


@pytest.fixture
def books_collector():
    """Фикстура для создания экземпляра BooksCollector."""
    return BooksCollector()


@pytest.fixture
def books_collector_with_books():
    """Фикстура для создания экземпляра BooksCollector с предустановленными книгами."""
    collector = BooksCollector()
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Властелин колец')
    collector.add_new_book('1984')
    collector.add_new_book('Мастер и Маргарита')
    collector.add_new_book('Дракула')
    return collector


@pytest.fixture
def books_collector_with_genres(books_collector_with_books):
    """Фикстура для создания экземпляра BooksCollector с книгами и жанрами."""
    collector = books_collector_with_books
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.set_book_genre('Властелин колец', 'Фантастика')
    collector.set_book_genre('1984', 'Фантастика')
    collector.set_book_genre('Мастер и Маргарита', 'Детективы')
    collector.set_book_genre('Дракула', 'Ужасы')
    return collector


@pytest.fixture
def books_collector_with_favorites(books_collector_with_genres):
    """Фикстура для создания экземпляра BooksCollector с книгами, жанрами и избранным."""
    collector = books_collector_with_genres
    collector.add_book_in_favorites('Гарри Поттер')
    collector.add_book_in_favorites('Властелин колец')
    return collector


@pytest.fixture
def empty_books_collector():
    """Фикстура для создания пустого экземпляра BooksCollector (альтернативное название)."""
    return BooksCollector()