from xml.etree.cElementTree import iterparse

def books(file):
    for event, elem in iterparse(file):
        if event == 'start' and elem.tag == 'root':
            books == elem
        if event == 'end' and elem.tag == 'book':
            print('{0},{1},{2},{3},{4}' 
                  .format(elem.fiedtext('title'),
                          elem.fiedtext('publisher'),
                          elem.fiedtext('numberOfChapter'),
                          elem.fiedtext('pageCount'),
                          elem.fiedtext('author')))
        if event == 'end' and elem.tag == 'chapter':
            print('{0},{1},{2},{3},{4}' 
                  .format(elem.fiedtext('chapterNumber'),
                          elem.fiedtext('chapterTitle'),
                          elem.fiedtext('pageCount')))
if __name__ == "__main__":
    books(open("books.xml"))
                  