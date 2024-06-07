import pytest
from main import BooksCollector


# Фикстура для создания экземпляра BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()


# Фикстура для создания книги с валидным именем
@pytest.fixture
def some_valid_length_book():
    return "Война миров"


# Фикстура для создания невалидного жанра
@pytest.fixture
def invalid_genre():
    return "Приключения"


# Фикстура для создания книги с возрастным ограничением
@pytest.fixture
def horror_book():
    return "Кошмар на улице Вязов", "Ужасы"
