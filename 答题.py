from os import system
from time import sleep

from pymongo import MongoClient

client = MongoClient()
db = client.answer


def judge(answer, i, db):
    for j in answer:
        if j not in i['answer'] or len(j) != i['answer'].replace(" ", "")[6:].__len__():
            print("\033[1;31;44m回答错误\033[0m")
            print(i["answer"])
            sleep(3)
            db.update_one({"title": i["title"]}, {"$inc": {"error": 1}})
            system('clear')
            return True
    if i.get('error'):
        if i['error'] > 0:
            db.update_one({"title": i["title"]}, {"$inc": {"error": -1}})
        else:
            db.update_one({"title": i["title"]}, {"$set": {"error": 0}})
    else:
        db.update_one({"title": i["title"]}, {"$set": {"error": 0}})
    system("clear")


def test(db):
    res = list(db.find())
    for j, i in enumerate(res, 1):
        if i["options"].__len__() > 3:
            print("\033[1;36;42m当前第{}题,共{}题\033[0m".format(j, len(res)))
            print(i["title"])
            for item in i["options"]:
                print(item)
            answer = input("输入答案>>>")
            judge(answer, i, db)


def error(db):
    res = list(db.find({"error": {"$gt": 0}}, sort=[('error', -1)]))
    for j, i in enumerate(res, 1):
        print("\033[1;36;42m当前第{}题,共{}题\033[0m".format(j, len(res)))
        print(i["title"])
        for item in i["options"]:
            print(item)
        print("\033[1;31;44m{}\033[0m".format(
            '这道题回答错误了{}次'.format(i['error'])))
        answer = input("输入答案>>>")
        judge(answer, i, db)


def main(db):
    print("输入序号:\n1.做题:\n2.做错题:")
    choice = input(">>>")
    if choice == '1':
        test(db)
    elif choice == '2':
        error(db)


if __name__ == "__main__":
    while True:
        print("输入课程序号:\n1.生药学:\n2.药理学:\n3.药物化学:\n输入Q退出")
        choice = input(">>>")
        if choice == "1":
            main(db.生药学)
        elif choice == "2":
            main(db.药理学)
        elif choice == "3":
            main(db.药物化学)
        elif choice.lower() == "q":
            break
