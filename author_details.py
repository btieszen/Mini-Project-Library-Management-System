#gets authors details


def details(author):
    detail_author =input("Who is the author you are searching for: ")
    if detail_author in author:
        print (author[detail_author])
    else:
        print("Author does not exist")