#$Author: ee364f03 $
#$Date: 2015-02-25 11:14:45 -0500 (Wed, 25 Feb 2015) $
#$Revision: 76798 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364f03/Lab06/parse_xml.py $
import re
def convertToAttrib():
    points = []
    Y = []
    X = []
    with open('points.xml','r') as f:
        lines = [x.strip('\n') for x in f.readlines()]
        for line in lines:
            m = re.search(r'(<.+?>)(\w+)', line)
            if(m):
                print (m.groups())
                points.append(m.groups()[1])
            m = re.search(r'(<.+?>)([+-.0-9]+)', line)
            if(m):
                print (m.groups())
                Y.append(m.groups()[1])
            m = re.search(r'([+-.0-9]+$)',line)
            if(m):
                print(m.groups())
                X.append(m.groups()[0])
        
    print(points)
    print (Y)
    print (X)

    FILEOUT = open('points_out.xml', 'wta')
    FILEOUT.write(lines[0] + '\n')
    FILEOUT.write('<coordinates>\n')
    for i in range(len(points)):
        FILEOUT.write('\t' + '<point ID="' + points[i] + '" X="' + X[i] + '" Y="' + Y[i] + '" />\n' )
    FILEOUT.write('</coordinates>\n')

def readBooks():
    with open('books.xml', 'r') as f:
        lines = [x.strip('\n') for x in f.readlines()]
        
    return lines

def getGenres():
    lines = readBooks()
    #print (lines)
    genres = []
    for line in lines:
        m = re.search(r'<genre>(.*)</genre>', line)
        if(m):
            if m.groups(0)[0] not in genres:
                genres.append(m.groups(0)[0]) 
    genres.sort()
    return genres

def getAuthorOf(bookName):
    lines = readBooks()
    authors = []
    title = []
    for line in lines:
        m = re.search(r'<author>(.*)</author>',line)
        if(m):
            authors.append(m.groups()[0])
        m = re.search(r'<title>(.*)</title>', line)
        if(m):
            title.append(m.groups()[0])
    #print (authors)
    #print (title)
    for i in range(len(title)):
        if title[i] == bookName:
            #print (authors[i])
            return authors[i]
    return None

def getBookInfo(bookID):
    lines = readBooks()
    authors = []
    title = []
    ID = []
    for line in lines:
        m = re.search(r'<book id="(.*)">',line)
        if(m):
            ID.append(m.groups()[0])
        m = re.search(r'<author>(.*)</author>',line)
        if(m):
            authors.append(m.groups()[0])
        m = re.search(r'<title>(.*)</title>', line)
        if(m):
            title.append(m.groups()[0])
    for i in range(len(ID)):
        if bookID == ID[i]:
            #print (title[i], authors[i])
            return (title[i], authors[i])
    return None

def getBooksBy(authorName):
    lines = readBooks()
    title = []
    authors_book = []
    for line in lines:
        m = re.search(r'<title>(.*)</title>', line)
        if(m):
            title.append(m.groups()[0])
    for book in title:
        if getAuthorOf(book) == authorName:
            authors_book.append(book)
    return authors_book

def getBooksBelow(bookPrice):
    lines = readBooks()
    title = []
    price = []
    below = []
    for line in lines:
        m = re.search(r'<title>(.*)</title>', line)
        if(m):
            #title.append(m.groups()[0])
            name = m.groups()[0]
        m = re.search(r'<price>(.*)</price>', line)
        if(m):
            #price.append(float(m.groups()[0]))
            if bookPrice > float(m.groups()[0]):
                below.append(name)
    return below
    #print (title)
    #print (below)

def searchForWord(word):
    lines = readBooks()
    title = []
    description = []
    description_string = ''
    for line in lines:
        
        m = re.search(r'<title>(.*)</title>', line)
        if(m):
            title.append(m.groups()[0])
            description.append(description_string)
            description_string = ''
        m = re.search(r'<description>(.*)', line)
        if(m):
            description_string = m.groups()[0]
        m = re.search(r'(<)', line)
        n = re.search(r'(.*)(</description>)',line)
        if(not m):
            #print line
            description_string = description_string + line
        if(n):
            #print n.groups()[0]
            description_string = description_string + n.groups()[0]
    #print (title)
    description = description[1:]
    #print (description)
    #print len(description)
    #print len(title)
    titlelist = []
    #print (description)
    for i in range(len(description)):
        if word in title[i] or word in description[i]:
            #print (title[i])
            titlelist.append(title[i])
    if word in title[-1]:
        titlelist.append(title[i])

    #print (titlelist)
    return titlelist


    
    

def main():
    #convertToAttrib()
    #getGenres()
    print (getAuthorOf('Maeve Ascendant'))
    print (getBookInfo('bk112'))
    print (getBooksBy("O'Brien, Tim"))
    print (getBooksBelow(15.00))
    print (searchForWord('in'))
    #readBooks()


if __name__ == "__main__":
    main()