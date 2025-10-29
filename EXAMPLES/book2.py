from book import Book


library = [
    Book('Горе от ума', 'А.Грибоедов'),
    Book('Муму', 'И.Тургенев'),
    Book('Тихий дон', 'М.Шолохов')
]

for book in library:
    print(f'{book.title} - {book.author}')