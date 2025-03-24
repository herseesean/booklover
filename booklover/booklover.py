import pandas as pd

class BookLover():

    def __init__(self, name, email, fav_genre):
        self.name=str(name)
        self.email=str(email)
        self.fav_genre=str(fav_genre)
        self.numbooks=0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self,book_name,rating):
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
        })
        if book_name in self.book_list.values:
            print(f'{book_name} is already in list')
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self,book_name):
        if book_name in self.book_list.values:
            return True
        else:
            return False
    
    def num_books_read(self):
        print('You have read',len(self.book_list),'books.')
    
    def fav_books(self):
        result=self.book_list[self.book_list['book_rating']>3]
        result=result.sort_values(by='book_rating',ascending=False)
        print(result)


if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 5)
    test_object.has_read('Fight Club')
    test_object.num_books_read()
    test_object.fav_books()

