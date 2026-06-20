# Доступные жанры
GENRE_FANTASY = 'Фантастика'
GENRE_HORROR = 'Ужасы'
GENRE_DETECTIVE = 'Детективы'
GENRE_CARTOON = 'Мультфильмы'
GENRE_COMEDY = 'Комедии'

# Жанры с возрастным рейтингом
GENRE_AGE_RATING = [GENRE_HORROR, GENRE_DETECTIVE]

# Все доступные жанры (список для параметризации)
ALL_GENRES = [GENRE_FANTASY, GENRE_HORROR, GENRE_DETECTIVE, GENRE_CARTOON, GENRE_COMEDY]

# Тестовые данные для книг
TEST_BOOKS = {
    'book1': 'Гарри Поттер',
    'book2': 'Война и мир',
    'book3': 'Мастер и Маргарита',
    'book4': '1984',
    'book5': 'Маленький принц',
}

# Тестовые данные для проверки книг с определенным жанром
# Формат: (жанр, ожидаемый_список_книг)
SPECIFIC_GENRE_TEST_DATA = [
    (GENRE_FANTASY, ['Книга1', 'Книга3']),
    (GENRE_HORROR, ['Книга2']),
    (GENRE_DETECTIVE, []),
    (GENRE_CARTOON, []),
]

# Тестовые данные для проверки книг для детей
# Формат: (жанр, ожидается_в_детском_списке)
BOOKS_FOR_CHILDREN_TEST_DATA = [
    (GENRE_FANTASY, True),
    (GENRE_CARTOON, True),
    (GENRE_COMEDY, True),
    (GENRE_HORROR, False),
    (GENRE_DETECTIVE, False),
]

# Тестовые данные для проверки установки жанров
# Формат: (название_книги, жанр)
BOOKS_WITH_GENRES = [
    ('Книга1', GENRE_FANTASY),
    ('Книга2', GENRE_HORROR),
    ('Книга3', GENRE_DETECTIVE),
    ('Книга4', GENRE_CARTOON),
    ('Книга5', GENRE_COMEDY),
]

# Невалидные жанры для тестирования
INVALID_GENRES = ['Роман', 'Поэзия', 'Драма', 'Триллер', 'Вестерн']

# Длинные названия для тестирования
MAX_LENGTH_NAME = 'А' * 40
TOO_LONG_NAME = 'А' * 41
EMPTY_NAME = ''

# Тестовые книги для комплексных тестов
COMPLEX_TEST_BOOKS = ['Книга1', 'Книга2', 'Книга3']