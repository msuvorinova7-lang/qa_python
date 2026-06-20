import pytest
from main import BooksCollector
from constants import (
    TEST_BOOKS, ALL_GENRES, GENRE_FANTASY, 
    GENRE_HORROR, GENRE_CARTOON, GENRE_COMEDY
)


@pytest.fixture
def collector():
    """
    Базовая фикстура, создающая новый экземпляр BooksCollector.
    Используется в тестах, где нужен пустой коллектор.
    """
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    """
    Фикстура, создающая коллектор с добавленными книгами (без жанров).
    Используется для тестирования методов, работающих со словарем книг.
    """
    for book_name in TEST_BOOKS.values():
        collector.add_new_book(book_name)
    return collector


@pytest.fixture
def collector_with_genres(collector_with_books):
    """
    Фикстура, создающая коллектор с книгами и установленными жанрами.
    Каждой книге присваивается жанр из списка ALL_GENRES по порядку.
    """
    # Получаем список книг
    books_list = list(TEST_BOOKS.values())
    
    # Устанавливаем жанры для каждой книги
    for i, book_name in enumerate(books_list):
        if i < len(ALL_GENRES):
            collector_with_books.set_book_genre(book_name, ALL_GENRES[i])
    
    return collector_with_books


@pytest.fixture
def collector_with_favorites(collector_with_genres):
    """
    Фикстура, создающая коллектор с книгами, жанрами и избранными книгами.
    В избранное добавляются первая и третья книги из TEST_BOOKS.
    """
    books_list = list(TEST_BOOKS.values())
    
    # Добавляем первую и третью книги в избранное (индексы 0 и 2)
    for i in [0, 2]:
        collector_with_genres.add_book_in_favorites(books_list[i])
    
    return collector_with_genres


@pytest.fixture
def collector_with_specific_genre_books(collector):
    """
    Фикстура, создающая коллектор с книгами определенных жанров.
    Используется для тестирования get_books_with_specific_genre.
    """
    # Добавляем книги
    collector.add_new_book('Книга1')
    collector.add_new_book('Книга2')
    collector.add_new_book('Книга3')
    collector.add_new_book('Книга4')
    
    # Устанавливаем жанры
    collector.set_book_genre('Книга1', GENRE_FANTASY)
    collector.set_book_genre('Книга2', GENRE_HORROR)
    collector.set_book_genre('Книга3', GENRE_FANTASY)
    collector.set_book_genre('Книга4', GENRE_CARTOON)
    
    return collector


@pytest.fixture
def collector_with_children_books(collector):
    """
    Фикстура, создающая коллектор с книгами для детей и с возрастным рейтингом.
    Используется для тестирования get_books_for_children.
    """
    # Книги для детей
    collector.add_new_book('Детская книга 1')
    collector.add_new_book('Детская книга 2')
    collector.set_book_genre('Детская книга 1', GENRE_FANTASY)
    collector.set_book_genre('Детская книга 2', GENRE_CARTOON)
    
    # Книги с возрастным рейтингом
    collector.add_new_book('Взрослая книга 1')
    collector.add_new_book('Взрослая книга 2')
    collector.set_book_genre('Взрослая книга 1', GENRE_HORROR)
    collector.set_book_genre('Взрослая книга 2', GENRE_DETECTIVE)
    
    return collector


@pytest.fixture
def collector_with_favorites_multiple(collector):
    """
    Фикстура, создающая коллектор с несколькими книгами в избранном.
    """
    books = ['Любимая книга 1', 'Любимая книга 2', 'Обычная книга']
    
    for book in books:
        collector.add_new_book(book)
    
    collector.add_book_in_favorites('Любимая книга 1')
    collector.add_book_in_favorites('Любимая книга 2')
    
    return collector


@pytest.fixture
def sample_book_names():
    """
    Фикстура с набором тестовых названий книг.
    """
    return ['Гарри Поттер', 'Властелин колец', 'Шерлок Холмс', 'Ну, погоди!']


@pytest.fixture
def collector_with_long_names(collector):
    """
    Фикстура, создающая коллектор с книгами разной длины названий.
    Используется для тестирования ограничений по длине.
    """
    # Короткое название
    collector.add_new_book('Книга')
    
    # Название из 40 символов (максимальная длина)
    max_length_name = 'А' * 40
    collector.add_new_book(max_length_name)
    
    return collector


@pytest.fixture
def collector_with_duplicates(collector):
    """
    Фикстура, создающая коллектор с дублирующимися книгами.
    Используется для тестирования предотвращения дубликатов.
    """
    collector.add_new_book('Дублирующаяся книга')
    collector.add_new_book('Дублирующаяся книга')
    collector.add_new_book('Уникальная книга')
    
    return collector


@pytest.fixture
def collector_with_favorites_operations(collector):
    """
    Фикстура для тестирования операций с избранным.
    Создает книги и добавляет одну из них в избранное.
    """
    collector.add_new_book('Избранная книга')
    collector.add_new_book('Неизбранная книга')
    collector.add_book_in_favorites('Избранная книга')
    
    return collector