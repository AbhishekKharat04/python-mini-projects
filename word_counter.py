try:
    with open("sample.txt","r") as f:
        text=f.read()
        words=text.split()
        print("Word count:",len(words))
except FileNotFoundError:
    print("File not found")
 