from os import system
from pymongo import MongoClient
from time import sleep
client=MongoClient()
db=client.answer
def judge(answer,i):
    for j in answer:
        if j not in i['answer']:
            print("回答错误")
            print(i["answer"])
            sleep(5)
            db.生药学.update_one({"title":i["title"]},{ "$set": { "error":True}})
            system('clear')
            return True
    db.生药学.update_one({"title":i["title"]},{ "$set": { "error":False}})
    system("clear")

def test(db):
    for i in db:
        if i["options"].__len__()>3:
            print(i["title"])
            for item in i["options"]:
                print(item)
            answer=input("输入答案>>>")
            judge(answer,i)

def error(db):
    for i in db:
        print(i["title"])
        for item in i["options"]:
            print(item)
        answer=input("输入答案>>>")
        judge(answer,i)

def main(db):
    print("输入序号:\n1.做题:\n2.做错题:")
    choice=input(">>>")
    if choice=='1':
        test(db.find())
    elif choice=='2':
        error(db.find({"error":True}))

    

if __name__ == "__main__":
    while True:
        print("输入课程序号:\n1.生药学:\n2.药理学:\n3.药物化学:\n输入Q退出")
        choice=input(">>>")
        if choice=="1":
            main(db.生药学)
        elif choice=="2":
            main(db.药理学)
        elif choice=="3":
            main(db.药物化学)
        elif choice.lower()=="q":
            break
    
        