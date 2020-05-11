with open("new2.txt","r+", encoding="utf-8") as file:
    content = file.read()
    dd = "içerik deneme"+ content
    #dd.insert eklemeyi sağlar
    print(dd)
