def takeUrl():
    link = input("youtube video link : ")
    
    if not link:
            print ("please enter a valid url")
    
    id=link.split('=')
    return id[1]
