from data import books
from dfs import dfs

#tree node
class BookRec:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
    def traverse(self):
        nodes_to_search = [self]
        while len(nodes_to_search) > 0:
            choice = input("Type 1 or 2?")
            if choice not in ["1", "2"]:
                print("Try again. ")
            else:
                choice_index = int(choice)
                choice_index -= 1
                choice_child = nodes_to_search.children[choice_index]
                print(choice_child.value)
                nodes_to_search = choice_child

#root
book_search_root = BookRec("""
Welcome to the Book Recommendation service!
You can search by 1. Author or 2. Genre!
""")

#child: author and genre
authors = BookRec("""
You have choosen to search by author!
Here is the list of accepted authors!
                  1. Brandon Sanderson
                  2. Isaac Asimov
                  3. Jane Austen
                  4. Sarah J. Maas
                  5. Shirley Jackson
                  6. Stephen King
                  7. Ursula K. Le Guin
1. Start Search 2. End
""")

book_search_root.add_child(authors)

genres = BookRec("""
You have choosen to search by Genre!
Here is the list of Genres!
                 1. Science Fiction
                 2. Fantasy
                 3. Romance
                 4. Horror
1. Start Search 2. End
""")

book_search_root.add_child(genres)

#leaf: Author
#functions that enable searching
def author_name():
    name = input("Type Author Number.")
    match name:
        case "1":
            print(dfs("Brandon Sanderson", "Mistborn"))
        case "2":
            print(dfs("Isaac Asimov", "Foundation"))
        case "3":
            print(dfs("Jane Austen", "Pride and Prejudice"))
        case "4":
            print(dfs("Sarah J. Maas", "A Court of Thorns and Roses"))
        case "5":
            print(dfs("Shirley Jackson", "The Haunting of Hill House"))
        case "6":
            print(dfs("Stephen King", "The Shining"))
        case "7":
            print(dfs("Ursula K. Le Guin", "A Tale of Earthsea"))
        case _:
            print("Try again.")
            author_name()

def end():
    print("Thank you for using the Book Recomendation service!")

search_author = BookRec(author_name())
author_end = BookRec(end())
authors.add_child(search_author)
authors.add_child(author_end)
    
 

#leaf: Genre
#genre functions that enable searching
def genre_name():
    name = input("Type Genre Number.")
    match name:
        case "1":
            print(dfs("Sci-fi", "Dune"))
        case "2":
            print(dfs("Fantasy", "The Hobbit"))
        case "3":
            print(dfs("Romance", "The Song of Achilles"))
        case "4":
            print(dfs("Horror", "Dracula"))
        case _:
            print("Try again.")
            author_name()

search_genre = BookRec(genre_name())
genre_end = BookRec(end())
genres.add_child(search_genre)
genres.add_child(genre_end)


