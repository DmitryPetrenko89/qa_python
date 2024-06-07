# qa_python

- `test_add_new_book_add_one_book_positive_result`

тест проверяет добавление одной книги с валидным названием в словарь books_genre

- `test_set_book_genre_set_valid_value_genre_positive_result`

тест проверяет установление валидного жанра для книги по ее имени, добавленной в словарь books_genre

- `test_set_book_genre_set_invalid_value_genre_is_empty`

тест проверяет установление невалидного жанра для книги по ее имени

- `test_get_book_genre_valid_name_positive_result`

тест проверяет получение жанра книги по ее имени

- `test_get_books_with_specific_genre_valid_genre_positive_result`

тест проверяет вывод списка книг с определенным жанром

- `test_get_books_genre_return_glossary_positive_result`

тест проверяет получение словаря books_genre

- `test_get_books_for_children_return_books_for_children_list_positive_result`

тест проверяет вывод списка книг подходящих детям

- `test_get_books_for_children_genre_age_rating_returned_list_is_empty`

тест проверяет, что в список не попадают книги с возрастным ограничением

- `test_add_book_in_favorites_add_valid_value_positive_result`

тест проверяет добавление книги в Избранное

- `test_add_book_in_favorites_add_duplicate_quantity_not_increased`

тест проверяет, что повторно добавленная книга не добавляется в Избранное 

- `test_delete_book_from_favorites_book_in_favorites_positive_result`

тест проверяет удаление книги из Избранного

- `test_get_list_of_favorites_books_favorites_list_not_empty_positive_result`

тест проверяет получение списка Избранных книг после добавления книги в Избранное

- `test_get_list_of_favorites_books_empty_list_positive_result`

тест проверяет возможность получения пустого списка Избранных книг
