def takeUrl(url):
    link = url
    
    if not link:
            print ("please enter a valid url")
    
    id=link.split('=')
    return id[1]
if __name__=="__main__":
    a=input("enter the url ")
    print(takeUrl(a))