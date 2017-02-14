import mysql.connector

def main():
    File_to_DB()


def File_to_DB():
    """
    This script will take the file, transferFile.txt, which contains a text version of the database,
    and input all the book metadata into the database.

    When you run it make sure you switch the variables in the creation of conn and the path to the file transferFile
    :return:
    """
    conn = mysql.connector.connect(
        user='root',
        password='ginnyq0811',
        host='localhost',
        database='seniordesign'
    )
    cur = conn.cursor()
    fr = open("C:\\users\\gabriel\\desktop\\senior design\\transferFile.txt", 'r')
    count =0
    for line in fr:
        id = int(line[0:line.find("%")])
        title= line[line.find("%")+1:line.find("%%")]
        author = line[line.find("%%")+2:line.find("%%%")]
        genre = line[line.find("%%%")+3:line.find("%%%%")]
        length = int(line[line.find("%%%%")+4:line.find("%%%%%")])
        cur.execute("insert into example values(%s,%s,%s,%s,%s)",(id,title,author,genre,length))

    conn.commit()
    conn.close()
    fr.close()

if __name__ == '__main__':
    main()