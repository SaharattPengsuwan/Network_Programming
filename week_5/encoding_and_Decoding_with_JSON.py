import json
books = ['book1','book2','book3']
json.dumps(books)
'["book1","book2","book3"]'

string_books = json.dumps(['["book1","book2","book3"]'])


type(string_books)

books = '["book1","book2","book3"]'
list = json.loads(books)
list
["book1","book2","book3"]