import subprocess,sys,socket,calibreServer


# Main Menu
def showMainOptionsMenu():
    print("-" * 50)
    print("Options Menu:")
    print("To search by author  PRESS <1>")
    print("To search by title   PRESS  <2>")
    print("To get all titles    PRESS <3>")
    print("To exit              PRESS <ANYTHING ELSE>")
    print("-" * 50)
    getMainQuery()

# Sub Menu
def showSubOptionsMenu(books):
    print("-" * 50)
    print("Options: ")
    print("Press < 1 > to read a book from the list")
    print("Press < ANYTHING ELSE > to return to Main Menu")
    print("-" * 50)
    choice = input("What does yee choose bruh?")
    print("-" * 50)

    if(choice is "1"):
        print("-" * 50)
        bookID = input("Enter Book ID: ")
        fileName=books[bookID].replace("\n","")+".txt"
        fr =open("c:\\users\\gabriel\\desktop\\batchbooks\\"+fileName,"r")
        text=fr.read()
        print(text)
        fr.close()
        print("-" * 50)



    showMainOptionsMenu()

# Gets user query
def getMainQuery():
    print("-" * 50)
    choicePressed = input("Enter option here:")
    print("-" * 50)

    if (choicePressed is "1"):
        author_search()
    elif (choicePressed is "2"):
        title_search()
    elif(choicePressed is "3"):
        title_upload_array()
    else:
        print("-" * 50)
        print("Thanks for visiting our library!\nSEE YA!")
        print("-" * 50)
        sys.exit(0)

# Gets title and limit of books to show
def title_search():
    print("-" * 50)
    bookTitle = input("What title would you like to search for? : ")
    limit = input("Max number of books to show: ")
    print("-" * 50)
    show_book_titles(bookTitle, limit)

def show_book_titles(bookTitle, limit):
    output = subprocess.check_output('calibredb list --limit ' + limit + ' --fields title --search title:' + bookTitle,
                                     shell=True)
    output = str(output.decode('UTF-8'))
    showSubOptionsMenu(print_books_dictionary(output))

# Gets author name and limit of titles to show
def author_search():
    print("-" * 50)
    authorName =input("What author would you like to search for? : ")
    limit = input("Max number of titles to show: ")
    print("-" * 50)
    show_author_titles(authorName,limit)

# Runs calibredb search protocol for given author and max inputs and displays results
def show_author_titles(author,max):
    output = subprocess.check_output('calibredb list --limit '+max+' --fields title --search author:' + author,
                                     shell=True)
    output = str(output.decode('UTF-8'))
    showSubOptionsMenu(print_books_dictionary(output))

def title_upload_array():
    output = subprocess.check_output('calibredb list --fields title', shell=True)
    output = str(output.decode('UTF-8'))
    books = make_books_dictionary(output)
    for key in books:
        print(books[key])
    showMainOptionsMenu()



##############################################################################################
# Look into making separate_lines and helper method work for titles more than two lines long #
# Run against titles:"unknown"                                                               #
##############################################################################################
# Turns calibredb search into a dictionary
# Input: output from subprocess call to calibredb
# Output: dictionary of books, where key=bookId value=book title
def make_books_dictionary(output):
    lines = separate_lines(output)
    books = {}
    for item in lines:
        books[item[0:item.find(" ")]] = item[item.find(" ") + 1:].strip() + "\n"
    return books


# Turns calibredb search into a dictionary and prints it
# Input: output from subprocess call to calibredb
# Output: dictionary of books, where key=bookId value=book title and prints dictionary to console
def print_books_dictionary(output):
    lines = separate_lines(output)
    books = {}
    for item in lines:
        books[item[0:item.find(" ")]] = item[item.find(" ") + 1:].strip() + "\n"
    # Prints out books dictionary
    for key in books:
        print(key+" "+books[key])

###############################################################################################
# Helper method for make_books_dictionary
# Puts every line into a separate list element
def separate_lines(output):
    books = []
    temp = ""
    # puts every thing up to a '\n' character into a spot in books
    for index in range(len(output)):
        temp+=output[index]
        if(output[index] is "\n"):
            books.append(temp)
            temp=""

    books.pop(0) # takes off first useless
    books=put_overflows_together(books)
    return books
##############################################################################################
# Helper method for separate_lines
# Some titles have to many characters and overflow into the next line and are counted as two books.
# This function puts those overflowed parts of titles into their corresponding title and removes the overflowed
# part from the list
def put_overflows_together(lines):
    # Puts lines that flow over into the next line on the same line and replaces the overflowed item in lines to "*"
    for index in range(len(lines)):
        if (lines[index][0] is " "):
            lines[index - 1] += lines[index].strip() + "\n"
            lines[index] = "*"
            # Removes marked lines, i.e. lines that are "*"
    for item in lines:
        if (item is "*"):
            lines.remove(item)
    return lines


def Main():
    print("Welcome to the our library!\nWe have books and you got eyes so lets go!\n")
    showMainOptionsMenu()

if __name__=='__main__':
    Main()