import time

class Library:
	
	def __init__(self,library_name,list_of_books):
		self.library_name=library_name
		self.list_of_books=list_of_books
	
	def display_book(self):
		return self.list_of_books
		
	def lend_book(self,book_name):
		if book_name in self.list_of_books:
			print(f"You can take {book_name} book.It's available now.")
			self.list_of_books.remove(book_name)
		else:
			print("The book is not available now. Please select another book.")
			
	def add_book(self,book_name):
		print("Thanks for give us book")
		return self.list_of_books.append(book_name)
		
	def return_book(self,book_name):
		print(f"Thanks for return {book_name} book")
		return self.list_of_books.append(book_name)
		
	def delete_book(self,book_name):
		return self.list_of_books.remove(book_name)
		
		
Harry= Library("Harry Library",["Bangla","English","Science","Math","BGS","Islam"])

print(f"Welcome to {Harry.library_name} \n \n")
while True:
	user_input=int(input("Entet 0 to Exit form program. \nEnter 1 for display all books. \nEnter 2 for add some books. \nEnter 3 for lend book. \nEnter 4 for return book. \nEnter 5 for delete book.\nEnter: "))
	if user_input==0:
		print("Good bye.🙂")
		break
	if user_input==1:
		print(Harry.display_book())
	elif user_input==2:
		book=input("Enter the book name: ")
		Harry.add_book(book)
	elif user_input==3:
		book=input("Enter the book name: ")
		Harry.lend_book(book)
	elif user_input==4:
		book=input("Enter the book name: ")
		Harry.return_book(book)
	elif user_input==5:
		password=12345
		passcode=int(input("Enter the 5 digit password: "))
		if password==passcode:
			book=input("Enter the book name: ")
			Harry.delete_book(book)
			print("Successfully deleted")
		else:
			print("Access Denied ✋✋✋")
	else:
		print("Inavlied Input")
	print("\n")
#	time.sleep(0.5)
		
		
	