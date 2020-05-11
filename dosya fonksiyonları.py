with open("yeni.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0) #0. konuma cursorü gönderir yani içeriğin en başına
    print(file.tell()) #cursorun kaçımcı noktada olduğunu söyler
