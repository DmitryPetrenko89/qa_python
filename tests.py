import pytest
from fixtures.conftest import collector
from fixtures.conftest import horror_book
from fixtures.conftest import some_valid_length_book
from fixtures.conftest import invalid_genre


class TestBooksCollector:
    books_list = [
        ["Война миров", "Фантастика"],
        ["Шерлок", "Детективы"],
        ["Три поросенка", "Мультфильмы"]
    ]

    books_list_without_age_rating = [
        ["Война миров", "Фантастика"],
        ["Три поросенка", "Мультфильмы"],
        ["Тупой и еще тупее", "Комедии"]
    ]

    favorite_books_list = [
        "Война миров", "Шерлок", "Три поросенка"
    ]

    def test_add_new_book_add_one_book_positive_result(self, some_valid_length_book, collector):
        collector.add_new_book(some_valid_length_book[0])
        assert some_valid_length_book[0] in collector.get_books_genre()

    @pytest.mark.parametrize("name, genre", books_list)
    def test_set_book_genre_set_valid_value_genre_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_set_invalid_value_genre_is_empty(self, some_valid_length_book, invalid_genre, collector):
        collector.add_new_book(some_valid_length_book[0])
        collector.set_book_genre(some_valid_length_book[0], invalid_genre[0])
        assert collector.get_book_genre(some_valid_length_book[0]) is ""

    @pytest.mark.parametrize("name, genre", books_list)
    def test_get_book_genre_valid_name_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("name, genre", books_list)
    def test_get_books_with_specific_genre_valid_genre_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    @pytest.mark.parametrize("name, genre", books_list)
    def test_get_books_genre_return_glossary_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name: genre}

    @pytest.mark.parametrize(
        "name, genre", books_list_without_age_rating)
    def test_get_books_for_children_return_books_for_children_list_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [name]

    def test_get_books_for_children_genre_age_rating_returned_list_is_empty(self, horror_book, collector):
        collector.add_new_book(horror_book[0])
        collector.set_book_genre(horror_book[0], horror_book[1])
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize("name", favorite_books_list)
    def test_add_book_in_favorites_add_valid_value_positive_result(self, name, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_duplicate_quantity_not_increased(self, some_valid_length_book, collector):
        collector.add_new_book(some_valid_length_book[0])
        collector.add_book_in_favorites(some_valid_length_book[0])
        collector.add_book_in_favorites(some_valid_length_book[0])
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_in_favorites_positive_result(self, some_valid_length_book, collector):
        collector.add_new_book(some_valid_length_book[0])
        collector.add_book_in_favorites(some_valid_length_book[0])
        collector.delete_book_from_favorites(some_valid_length_book[0])
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_favorites_list_not_empty_positive_result(self, some_valid_length_book,
                                                                                  collector):
        collector.add_new_book(some_valid_length_book[0])
        collector.add_book_in_favorites(some_valid_length_book[0])
        assert collector.get_list_of_favorites_books() == [some_valid_length_book[0]]

    def test_get_list_of_favorites_books_empty_list_positive_result(self, collector):
        assert collector.get_list_of_favorites_books() == []
