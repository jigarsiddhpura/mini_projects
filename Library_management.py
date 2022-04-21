
class Library:

    def __init__(self, list, library_name):
        self.book_list = list
        self.library_name = library_name
        self.lend_dict = {}
    
    def Displaybook(self):
        print(self.book_list)

    def Lendbook(self, user, book):
        if book not in self.lend_dict.keys():
            print("Book avilable , take it.")
            self.lend_dict.update({book:user})
            print("Lender-Book database has been updated.")
            self.book_list.remove(book)
            # del self.lend_book[self.books_available]
        else:
            print(f"Book unavailable , Its already taken by {self.lend_dict[book]} ")

    def Addbook(self,book):
        self.book_list.append(book)
        print(f"Book successfully added in {self.library_name}")
    
    def Returnbook(self, book):
        self.lend_dict.pop(book)
        self.book_list.append(book)
        print(f"Book successfully returned in {self.library_name}")


jigarLibrary = Library(["Harry Potter","Naruto","Death Note","Asur","AOT"],"Jigar's Libary")
if __name__=="__main__":

    while(1):
        prompt = int(input("Enter 1 to display all books available.\nEnter 2 to lend a book.\nEnter 3 to donate a book.\nEnter 4 to return a book.\n"))
        if prompt == 1:
            jigarLibrary.Displaybook()

        elif prompt == 2:
            book = input("Which book do u wanna lend?\n")
            user = input("Your name Sir ?\n")
            jigarLibrary.Lendbook(user,book)
            
        elif prompt == 3:
            book = input("Enter the name of book u wanna donate\n")
            jigarLibrary.Addbook(book)
            
        elif prompt == 4:
            book = input("Enter the name of book u wanna return\n")
            jigarLibrary.Returnbook(book) 
            
        else:
            print("Invalid input , Try again")
            

        explore = ""
        while(explore !="c" and explore !="e"):
            explore = input("Enter c to continue and e to exit\n").lower()
            if explore == "c":
                continue
            elif explore == "e":
                exit()

