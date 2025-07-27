def takeUrl():
    link = input("youtube video link : ")
    try :
        if not link:
            print ("please enter a valid url")
    except Exception as e:
        print(e)
    id=link.split('=')
    return id[1]
