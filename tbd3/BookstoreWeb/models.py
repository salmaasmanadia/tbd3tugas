from django.db import models

class Gender(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'

class Rating(models.TextChoices):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

class Genre(models.TextChoices):
    MYSTERY = 'Mystery'
    SCIENCE_FICTION = 'Science Fiction'
    FANTASY = 'Fantasy'
    ROMANCE = 'Romance'
    HISTORICAL_FICTION = 'Historical Fiction'
    THRILLER = 'Thriller'
    HORROR = 'Horror'
    LITERARY_FICTION = 'Literary Fiction'
    YOUNG_ADULT = 'Young Adult'
    CONTEMPORARY_FICTION = 'Contemporary Fiction'
    BIOGRAPHY = 'Biography'
    HISTORY = 'History'
    MEMOIR = 'Memoir'
    SELF_HELP = 'Self-help'
    SCIENCE = 'Science'
    BUSINESS = 'Business'
    PSYCHOLOGY = 'Psychology'
    PHILOSOPHY = 'Philosophy'
    TRAVEL = 'Travel'
    COOKBOOKS = 'Cookbooks'
    PICTURE_BOOKS = 'Picture Books'
    EARLY_READERS = 'Early Readers'
    CHAPTER_BOOKS = 'Chapter Books'
    MIDDLE_GRADE = 'Middle Grade'
    TEXTBOOKS = 'Textbooks'
    RESEARCH_PAPERS = 'Research Papers'
    JOURNALS = 'Journals'
    ACADEMIC_MONOGRAPHS = 'Academic Monographs'
    REFERENCE_BOOKS = 'Reference Books'
    CONTEMPORARY_POETRY = 'Contemporary Poetry'
    CLASSIC_POETRY = 'Classic Poetry'
    EPIC_POETRY = 'Epic Poetry'
    SONNETS = 'Sonnets'
    PERSONAL_DEVELOPMENT = 'Personal Development'
    RELATIONSHIPS = 'Relationships'
    MOTIVATION = 'Motivation'
    MINDFULNESS = 'Mindfulness'
    TRAVEL_GUIDES = 'Travel Guides'
    ADVENTURE_TRAVEL = 'Adventure Travel'
    TRAVEL_MEMOIRS = 'Travel Memoirs'
    TRAVEL_ESSAYS = 'Travel Essays'
    ENTREPRENEURSHIP = 'Entrepreneurship'
    MANAGEMENT = 'Management'
    MARKETING = 'Marketing'
    FINANCE = 'Finance'
    LEADERSHIP = 'Leadership'
    ELSE = 'else'

class BookCategory(models.TextChoices):
    FICTION = 'Fiction'
    NON_FICTION = 'Non fiction'
    CHILDRENS_BOOKS = 'Childrens Books'
    ACADEMIC_BOOKS = 'Academic Books'
    POETRY = 'Poetry'
    SELF_HELP = 'Self-help'
    TRAVEL = 'Travel'
    BUSINESS = 'Business'
    ELSE = 'else'

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=7)
    last_update = models.DateTimeField(auto_now=True)

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    birthdate = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50, choices=Genre.choices)
    category = models.CharField(max_length=50, choices=BookCategory.choices)
    publication_date = models.DateField()
    rating = models.CharField(max_length=1, choices=Rating.choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

