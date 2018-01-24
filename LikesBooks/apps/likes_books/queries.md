#### Create user accounts
User.objects.create(first_name = 'John', last_name = 'Smith', email = 'john@smith.com')

#### Have the first user create/upload 2 books
Book.objects.create(name = 'Atlas Shrugged', uploader = User.objects.get(id=1))

#### Have the first user like the last book and the first book
User.objects.get(id=1).liked_books.add(Book.objects.first())
User.objects.get(id=1).liked_books.add(Book.objects.last())

#### Have the second user like the first book and the third book
User.objects.get(id=2).liked_books.add(Book.objects.first())
User.objects.get(id=2).liked_books.add(Book.objects.get(id=3))

#### Have the third user like all books
for object in Book.objects.all():
  User.objects.get(id=3).liked_books.add(object)

#### Display all users who like the first book
for object in Book.objects.get(id=1).liked_users.all():
  print object.id

You could have also printed object.first_name or any other attributes.

#### Display the user who uploaded the first book
Book.objects.get(id=1).uploader.first_name

#### Display all users who like the second book
for object in Book.objects.get(id=2).liked_users.all():
  print object.first_name

#### Display the user who uploaded the second book
Book.objects.get(id=2).uploader.first_name
