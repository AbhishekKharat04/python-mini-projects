import json
try:
    with open("tasks.json","r") as f:
        tasks=json.load(f)
except:
    tasks=[]
    print("1 Add  2 View  3 Delete  4 Done")
choice=input("Choose: ")
with open("tasks.json","w") as f:
    json.dump(tasks,f)