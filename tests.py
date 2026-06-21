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
    def test_add_new_book_success(self, books_collector):
        books_collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in books_collector.get_books_genre()

    def test_add_new_book_default_genre_is_empty(self, books_collector):
        books_collector.add_new_book('Гарри Поттер')
        assert books_collector.get_book_genre('Гарри Поттер') == ''

    @pytest.mark.parametrize('name_length', [1, 20, 40])
    def test_add_new_book_valid_name_length(self, books_collector, name_length):
        book_name = 'А' * name_length
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.books_genre

    @pytest.mark.parametrize('name_length', [41, 50, 100])
    def test_add_new_book_name_too_long(self, books_collector, name_length):
        too_long_name = 'А' * name_length
        books_collector.add_new_book(too_long_name)
        assert too_long_name not in books_collector.books_genre

    def test_add_new_book_empty_name(self, books_collector):
        books_collector.add_new_book('')
        assert '' not in books_collector.books_genre

    def test_add_new_book_duplicate_not_added(self, books_collector):
        books_collector.add_new_book('Война и мир')
        books_collector.add_new_book('Война и мир')
        assert len(books_collector.get_books_genre()) == 1

    # 2. Тесты для методов set_book_genre и get_book_genre
    def test_set_book_genre_valid_genre(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Фантастика')
        assert books_collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid_genre_remains_empty(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Роман')
        assert books_collector.get_book_genre('Книга') == ''

    def test_set_book_genre_nonexistent_book_returns_none(self, books_collector):
        books_collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert books_collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_default_empty_string(self, books_collector):
        books_collector.add_new_book('Книга без жанра')
        assert books_collector.get_book_genre('Книга без жанра') == ''

    def test_get_book_genre_nonexistent_book_returns_none(self, books_collector):
        assert books_collector.get_book_genre('Несуществующая книга') is None

    # 3. Тесты для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_matching_books(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.add_new_book('Книга3')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        books_collector.set_book_genre('Книга2', 'Ужасы')
        books_collector.set_book_genre('Книга3', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Книга1', 'Книга3']

    def test_get_books_with_specific_genre_empty_collection(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_no_match(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_specific_genre_invalid_genre_type(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Роман') == []

    # 4. Тесты для метода get_books_genre
    def test_get_books_genre_returns_correct_dict(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        expected_dict = {'Книга1': 'Фантастика', 'Книга2': ''}
        assert books_collector.get_books_genre() == expected_dict

    def test_get_books_genre_empty_collection(self, books_collector):
        assert books_collector.get_books_genre() == {}

    # 5. Тесты для метода get_books_for_children
    def test_get_books_for_children_includes_valid_genres(self, books_collector):
        books_collector.add_new_book('Детская книга1')
        books_collector.add_new_book('Детская книга2')
        books_collector.set_book_genre('Детская книга1', 'Фантастика')
        books_collector.set_book_genre('Детская книга2', 'Мультфильмы')
        children_books = books_collector.get_books_for_children()
        assert 'Детская книга1' in children_books
        assert 'Детская книга2' in children_books

    def test_get_books_for_children_excludes_horror(self, books_collector):
        books_collector.add_new_book('Ужасная книга')
        books_collector.set_book_genre('Ужасная книга', 'Ужасы')
        children_books = books_collector.get_books_for_children()
        assert 'Ужасная книга' not in children_books

    def test_get_books_for_children_excludes_detective(self, books_collector):
        books_collector.add_new_book('Детективная книга')
        books_collector.set_book_genre('Детективная книга', 'Детективы')
        children_books = books_collector.get_books_for_children()
        assert 'Детективная книга' not in children_books

    def test_get_books_for_children_returns_only_allowed_genres(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.add_new_book('Книга3')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        books_collector.set_book_genre('Книга2', 'Ужасы')
        books_collector.set_book_genre('Книга3', 'Комедии')
        assert books_collector.get_books_for_children() == ['Книга1', 'Книга3']

    def test_get_books_for_children_book_without_genre(self, books_collector):
        books_collector.add_new_book('Книга без жанра')
        assert books_collector.get_books_for_children() == []

    def test_get_books_for_children_empty_collection(self, books_collector):
        assert books_collector.get_books_for_children() == []

    # 6. Тесты для методов работы с избранным
    def test_add_book_in_favorites_success(self, books_collector):
        books_collector.add_new_book('Любимая книга')
        books_collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in books_collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        books_collector.add_book_in_favorites('Книга')
        assert len(books_collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_nonexistent_book(self, books_collector):
        books_collector.add_book_in_favorites('Несуществующая книга')
        assert books_collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_book_without_genre(self, books_collector):
        books_collector.add_new_book('Книга без жанра')
        books_collector.add_book_in_favorites('Книга без жанра')
        assert 'Книга без жанра' in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        books_collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.delete_book_from_favorites('Книга')
        assert books_collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_nonexistent_book(self, books_collector):
        books_collector.delete_book_from_favorites('Несуществующая книга')
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_empty(self, books_collector):
        assert books_collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('book_name,should_be_in_favorites', [
        ('Книга1', True),
        ('Книга2', False),
        ('Книга3', True)
    ])
    def test_get_list_of_favorites_books_selected_books(self, books_collector, book_name, should_be_in_favorites):
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.add_new_book('Книга3')
        books_collector.add_book_in_favorites('Книга1')
        books_collector.add_book_in_favorites('Книга3')
        
        if should_be_in_favorites:
            assert book_name in books_collector.get_list_of_favorites_books()
        else:
            assert book_name not in books_collector.get_list_of_favorites_books()

    # 7. Комплексные тесты (оставлены как сценарии использования)
    def test_complete_workflow_books_for_children_and_favorites(self, books_collector):
        # Добавляем книги
        books_collector.add_new_book('Книга1')
        books_collector.add_new_book('Книга2')
        books_collector.add_new_book('Книга3')
        
        # Устанавливаем жанры
        books_collector.set_book_genre('Книга1', 'Фантастика')
        books_collector.set_book_genre('Книга2', 'Ужасы')
        books_collector.set_book_genre('Книга3', 'Мультфильмы')
        
        # Проверяем книги для детей
        children_books = books_collector.get_books_for_children()
        assert 'Книга1' in children_books
        assert 'Книга2' not in children_books
        assert 'Книга3' in children_books
        
        # Добавляем в избранное
        books_collector.add_book_in_favorites('Книга1')
        books_collector.add_book_in_favorites('Книга3')
        
        # Проверяем избранное
        favorites = books_collector.get_list_of_favorites_books()
        assert 'Книга1' in favorites
        assert 'Книга3' in favorites
        
        # Удаляем из избранного
        books_collector.delete_book_from_favorites('Книга1')
        assert 'Книга1' not in books_collector.get_list_of_favorites_books()
        assert 'Книга3' in books_collector.get_list_of_favorites_books()

    def test_add_book_without_genre_can_be_favorited(self, books_collector):
        books_collector.add_new_book('Новая книга')
        books_collector.add_book_in_favorites('Новая книга')
        assert 'Новая книга' in books_collector.get_list_of_favorites_books()

    def test_set_genre_after_adding_to_favorites_preserves_favorite(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.add_book_in_favorites('Книга')
        books_collector.set_book_genre('Книга', 'Фантастика')
        assert 'Книга' in books_collector.get_list_of_favorites_books()

    def test_delete_from_favorites_does_not_remove_book(self, books_collector):
        books_collector.add_new_book('Книга')
        books_collector.set_book_genre('Книга', 'Ужасы')
        books_collector.add_book_in_favorites('Книга')
        books_collector.delete_book_from_favorites('Книга')
        assert books_collector.get_book_genre('Книга') == 'Ужасы'

    @pytest.fixture
    def books_collector(self):
        from books_collector import BooksCollector
        return BooksCollector()