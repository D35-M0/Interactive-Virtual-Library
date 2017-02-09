import mysql.connector
conn = mysql.connector.connect(
    user='root',
    password='ginnyq0811',
    host='localhost',
    database='seniorproject'
)
cur=conn.cursor()

def main():
    #authorsDownload()
    #matchedbooksDownload()
    authorsUpload()
    matchedBooksUpload()
    return(0)

def matchedBooksUpload():
    # Comments
    # key=book_id values in order(author_id,title,tags)
    matchedbooks = {}

    fr = open('C:\\users\\gabriel\\desktop\\dbtransfer\\matchedbooks.txt', 'r')

    for line in fr:
        matchedbooks[line[0:line.find('%')]] = (
        line[(line.find('%') + 1):line.find('%%')], line[(line.find('%%') + 2):line.find('%%%')],
        line[(line.find('%%%') + 3):line.find('%%%%')])

    for key in matchedbooks:
       cur.execute("insert into mm values(%s,%s,%s,%s)",(key, matchedbooks[key][0], matchedbooks[key][1], matchedbooks[key][2]))
    conn.commit()

def authorsUpload():
    # key=author_id value=author_name
    authors = {}
    fr = open('C:\\users\\gabriel\\desktop\\dbtransfer\\authors.txt', 'r')

    for line in fr:
        authors[line[0:line.find('%')]] = line[(line.find('%') + 1):(len(line) - 2)]

    # cur.execute("create table aa(author_id int unique,author_name varchar(150) unique,primary key(author_id))")
    # cur.execute("show tables")
    # print(cur.fetchall())
    for key in authors:
        cur.execute("insert into autor values(%s,%s)", (key, authors[key]))
    conn.commit()

def authorsDownload():
    fw = open("authors.txt", 'w')
    cur.execute("select * from authors")
    authors = cur.fetchall()

    for item in authors:
        fw.write(str(item[0]) + "%" + item[1] + "%\n")
    fw.close()

def matchedbooksDownload():
    fw = open("matchedbooks.txt", 'w')
    cur.execute("select * from matchedbooks")
    authors = cur.fetchall()

    for item in authors:
        fw.write(str(item[0]) + "%" + str(item[1]) + "%%" + item[2] + "%%%" + item[3] + "%%%%\n")
    fw.close()

if __name__=='__main__':
    main()