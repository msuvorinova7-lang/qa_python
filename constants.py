# Константы для жанров книг
GENRE_FANTASY = 'Фантастика'
GENRE_HORROR = 'Ужасы'
GENRE_DETECTIVE = 'Детективы'
GENRE_COMEDY = 'Комедии'
GENRE_CARTOONS = 'Мультфильмы'

# Допустимые жанры
VALID_GENRES = [
    GENRE_FANTASY,
    GENRE_HORROR,
    GENRE_DETECTIVE,
    GENRE_COMEDY,
    GENRE_CARTOONS
]

# Жанры с возрастным рейтингом (не для детей)
ADULT_GENRES = [
    GENRE_HORROR,
    GENRE_DETECTIVE
]

# Жанры для детей
CHILDREN_GENRES = [
    GENRE_FANTASY,
    GENRE_COMEDY,
    GENRE_CARTOONS
]

# Константы для книг
BOOK_NAME_HARRY_POTTER = 'Гарри Поттер'
BOOK_NAME_LORD_OF_THE_RINGS = 'Властелин колец'
BOOK_NAME_1984 = '1984'
BOOK_NAME_MASTER_AND_MARGARITA = 'Мастер и Маргарита'
BOOK_NAME_DRACULA = 'Дракула'

# Константы для тестирования граничных значений
MAX_BOOK_NAME_LENGTH = 40
MIN_BOOK_NAME_LENGTH = 1

# Константы для тестовых данных
TEST_BOOK_NAMES = [
    BOOK_NAME_HARRY_POTTER,
    BOOK_NAME_LORD_OF_THE_RINGS,
    BOOK_NAME_1984,
    BOOK_NAME_MASTER_AND_MARGARITA,
    BOOK_NAME_DRACULA
]

# Константы для параметризации
BOOK_NAME_LENGTHS_VALID = [1, 20, 40]
BOOK_NAME_LENGTHS_INVALID = [41, 50, 100]