import subprocess
import sys



def showMainOptionsMenu():
    print("-" * 50)
    print("Options Menu:")
    print("To search by author  PRESS <1>")
    print("To search by title  PRESS  <2>")
    print("To exit              PRESS <3>")
    print("-" * 50)

def getUserQuery():
    print("-" * 50)
    choicePressed = input("Enter option here:")
    print("-" * 50)

    if (choicePressed is "1"):
        author = getAuthorName()
        authorSearch(author)
    elif (choicePressed is "2"):
        title = getTitleName()
        titleSearch(title)
    else:
        print("-" * 50)
        print("Thanks for visiting our library!\nSEE YA!")
        print("-" * 50)

        sys.exit(0)





def getAuthorName():
    print("-" * 50)
    authorName =input("What author would you like to search for? :")
    print("-" * 50)
    return authorName

def getTitleName():
    print("-" * 50)
    titleName =input("What title would you like to search for? :")
    print("-" * 50)
    return titleName

def showSubOptionsMenu(listOfBooks):
    print("-" * 50)
    print("Options: ")
    print("Press < 1 > to read a book from the list")
    print("Press < ANYTHING ELSE > to return to Main Menu")
    print("-" * 50)


    choice = input("What does yee choose bruh?")
    print("-" * 50)
    if(choice is "1"):
        print("-" * 50)
        bookNum = input("What book yee choose bruh?")
        print(listOfBooks[int(bookNum)-1])
        print("-" * 50)

    showMainOptionsMenu()
    getUserQuery()


def authorSearch(authorName):
    output = subprocess.check_output('calibredb list --limit 25 --fields title --search author:' + authorName,
                                     shell=True)
    output = output.replace(bytes("\n", 'UTF-8'), bytes("*", 'UTF-8'))
    firstMark = -1
    bookTitles = []
    for index in range(len(output)):
        if (chr(output[index]) == "*"):
            if (firstMark == -1):
                firstMark = index + 1
            elif (index + 1 < len(output) and chr(output[index + 1]) is not " "):
                bookTitles.append(output[firstMark:index])
                firstMark = index + 1

        for item in bookTitles:
            item = item.replace(bytes("\n", 'UTF-8'), bytes("", 'UTF-8'))


    optionNum = 1
    print("-" * 50)
    for item in bookTitles:
        print("Book Number " + str(optionNum), end=" :")
        print(item)
        optionNum += 1

    if(optionNum is 1):
        print("Author not found!\nTry Again!")
        showMainOptionsMenu()
        getUserQuery()
    else:
        showSubOptionsMenu(bookTitles)





def titleSearch(titleName):
    output = subprocess.check_output('calibredb list --limit 25 --search title:' + titleName, shell=True)
    output = output.replace(bytes("\n", 'UTF-8'), bytes("*", 'UTF-8'))
    firstMark = -1
    books = []
    for index in range(len(output)):
        if (chr(output[index]) == "*"):
            if (firstMark == -1):
                firstMark = index + 1
            elif (index + 1 < len(output) and chr(output[index + 1]) is not " "):
                books.append(output[firstMark:index])
                firstMark = index + 1

        for item in books:
            item = item.replace(bytes("\n", 'UTF-8'), bytes("", 'UTF-8'))

    optionNum = 1
    for item in books:
        print("Book Number " + str(optionNum), end=" :")
        print(item)
        optionNum += 1

    if (optionNum is 1):
        print("Book not in our database!\nTry Again!")
        showMainOptionsMenu()
        getUserQuery()
    else:
        showSubOptionsMenu(books)




def Main():
    print("Welcome to the our library!\nWe have books and you got eyes so lets go!")
    showMainOptionsMenu()
    getUserQuery()

if __name__=='__main__':
    Main()