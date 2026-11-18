class Publisher:
   def __init__(self,name):
     self.name=name
class Book(Publisher):
  def __init__(self,name,title,author):
     super().__init__(name)
     self.title=title
     self.author=author
class Python(Book):
   def __init__(self,name,title,author,price,pages):
      super().__init__(name,title,author)
      self.price=price
      self.pages=pages
   def display(self):
     print("Publication:",self.name)
     print("Book Title:",self.title)
     print("Author:",self.author)
     print("price:",self.price)
     print("Total Pages of Book:",self.pages)
p=Python("ABC Publication","Python programming","Guido Van Rossum",450,350)
p.display()
    
    
