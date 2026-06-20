from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# 1. Тесты для метода add_new_book
    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_books_genre()
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_add_new_book_name_max_length(self):
        collector = BooksCollector()
        long_name = 'А' * 40
        collector.add_new_book(long_name)
        assert long_name in collector.books_genre

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        too_long_name = 'А' * 41
        collector.add_new_book(too_long_name)
        assert too_long_name not in collector.books_genre

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

    # 2. Тесты для методов set_book_genre и get_book_genre
    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.get_book_genre('Книга') == ''

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    # 3. Тесты для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        collector.set_book_genre('Книга3', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1', 'Книга3']

    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_no_matching_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []

    # 4. Тест для метода get_books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        expected_dict = {'Книга1': 'Фантастика', 'Книга2': ''}
        assert collector.get_books_genre() == expected_dict

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # 5. Тесты для метода get_books_for_children
    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга1')
        collector.add_new_book('Детская книга2')
        collector.set_book_genre('Детская книга1', 'Фантастика')
        collector.set_book_genre('Детская книга2', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert 'Детская книга1' in children_books
        assert 'Детская книга2' in children_books

    def test_get_books_for_children_excludes_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        collector.add_new_book('Детективная книга')
        collector.set_book_genre('Детективная книга', 'Детективы')
        children_books = collector.get_books_for_children()
        assert 'Ужасная книга' not in children_books
        assert 'Детективная книга' not in children_books

    def test_get_books_for_children_mixed_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        collector.set_book_genre('Книга3', 'Комедии')
        children_books = collector.get_books_for_children()
        assert children_books == ['Книга1', 'Книга3']

    def test_get_books_for_children_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    # 6. Тесты для методов работы с избранным
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.set_book_genre('Любимая книга', 'Фантастика')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        collector.add_book_in_favorites('Книга без жанра')
        assert 'Книга без жанра' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_multiple(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга3')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга1' in favorites
        assert 'Книга3' in favorites
        assert 'Книга2' not in favorites

    # 7. Комплексные тесты с использованием нескольких методов
    def test_complete_workflow(self):
        collector = BooksCollector()
        
        # Добавляем книги
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        
        # Устанавливаем жанры
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        collector.set_book_genre('Книга3', 'Мультфильмы')
        
        # Проверяем книги для детей
        children_books = collector.get_books_for_children()
        assert 'Книга1' in children_books
        assert 'Книга2' not in children_books
        assert 'Книга3' in children_books
        
        # Добавляем в избранное
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга3')
        
        # Проверяем избранное
        favorites = collector.get_list_of_favorites_books()
        assert 'Книга1' in favorites
        assert 'Книга3' in favorites
        assert 'Книга2' not in favorites
        
        # Проверяем книги с определенным жанром
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Книга1']
        
        # Удаляем из избранного
        collector.delete_book_from_favorites('Книга1')
        favorites_after_delete = collector.get_list_of_favorites_books()
        assert 'Книга1' not in favorites_after_delete
        assert 'Книга3' in favorites_after_delete

    def test_add_book_without_genre_and_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        collector.add_book_in_favorites('Новая книга')
        
        # Проверяем, что книга добавилась в избранное
        assert 'Новая книга' in collector.get_list_of_favorites_books()
        # Проверяем, что у книги нет жанра
        assert collector.get_book_genre('Новая книга') == ''

    def test_set_genre_after_adding_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        
        # Устанавливаем жанр после добавления в избранное
        collector.set_book_genre('Книга', 'Фантастика')
        
        # Проверяем, что жанр установился
        assert collector.get_book_genre('Книга') == 'Фантастика'
        # Проверяем, что книга осталась в избранном
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_after_genre_change(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        collector.add_book_in_favorites('Книга')
        
        # Меняем жанр
        collector.set_book_genre('Книга', 'Ужасы')
        
        # Удаляем из избранного
        collector.delete_book_from_favorites('Книга')
        
        # Проверяем, что книга удалилась из избранного
        assert 'Книга' not in collector.get_list_of_favorites_books()
        # Проверяем, что книга осталась в словаре с новым жанром
        assert collector.get_book_genre('Книга') == 'Ужасы'