import os
import time
from github import Github
import webbrowser

os.system("cls")
username="your username"                    #Your GitHub username  
code="your password"                        #Your GitHub password
path= "C:/Users/yourUsername/Programs"      #Your projects folder
ext="py"                                    #Chanage here for your most used extension

JP="      ## ########  \n      ## ##     ## \n      ## ##     ## \n      ## ########  \n##    ## ##        \n##    ## ##        \n ######  ##        "
print("Reporaptor by:\n\n"+JP+"\n\nDefault extesion: '"+ext+"' \nChange it in line 10 or user <name ext> when naming your project\nExample: WebTest js\nDo not use spaces in name\n")

def SecondAsk(a,ne):    
    n=input("What now?\n1. Open Folder\n2. Open "+a+"."+ne+"\n3. Open README.md\n4. New project\n5. Exit\nAny other close program\n")
    if n.isnumeric():
        if int(n):
            os.system("cls")
            if int(n)==1:
                os.startfile(path+"/"+a)
                SecondAsk(a,ne)
            elif int(n)==2:
                os.startfile(path+"/"+a+"/"+a+"."+ne)
                SecondAsk(a,ne)
            elif int(n)==3:

                os.startfile(path+"/"+a+"/README.md")
                SecondAsk(a,ne)
            elif int(n)==4:
                ask()
            elif int(n)==5:
                print("Thanks for using me. \n\n"+JP)
                exit()
            else:
                ask()
        else:
            ask()
    else:
        os.system("cls")
        print("Thanks for using me. \n\n"+JP)
        exit()

def ask():
    a=input("Insert your new project's name:             <E-Exit> <R-Restart>\n")
    if a=="r" or a=="R":
        os.system("cls") 
        ask()
    elif a=="e" or a=="E":
        os.system("cls")
        print("Thanks for using me. \n\n"+JP)
        exit()
    elif len(a)>1:
        pn = a.split(" ")
        ne = ext
        if len(pn) > 1:
            ne = pn[1] 
        a=pn[0]
        if os.path.isfile(path+"/"+a+"/"+a+".py"):
            os.system("cls") 
            print("The project: "+a+" already exists")
            ask()
        else:
            if not os.path.isdir(path+"/"+a):
                os.mkdir(path+"/"+a)
                print("Creating: "+path+"/"+a)
                open(path+"/"+a+"/"+a+"."+ne, 'a')
                print("Creating: "+path+"/"+a+"/"+a+"."+ne)
                open(path+"/"+a+"/README.md", 'a')
                print("Creating: "+path+"/"+a+"/README.md")
                Git = Github(username,code)
                User=Git.get_user()
                if User:
                    print("\nLogging in...")
                    c=0
                    try:
                        for repo in Git.get_user().get_repos():
                            c=c+1
                            print(str(c)+". "+repo.name)
                        print("Uploading to GitHub...")
                        desc=input("Enter description, press enter to skip\n")
                        rep=Git.get_user().create_repo(a,desc)
                        print("Repository created...")
                        rep.create_file(a+"."+ext, "commit message", "")
                        rep.create_file("README.md", "commit message", desc)
                        print("Files created...")
                        last=input("Open repository in GitHub? (y)\n")
                        if last=="y"or last=="Y":
                            webbrowser.open("https://github.com/"+username+"/"+a)
                    except:
                        print("Wrong credentials... The project was created locally")
                time.sleep(0.5)
                SecondAsk(a,ne)
            else:
                os.system("cls") 
                print("Invalid name")
                ask()           
    else:
        print("Name must contain at least 2 characters")
        ask()
ask()
