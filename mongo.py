from scrapy.http import HtmlResponse
import requests
from pprint import pprint
from pymongo import MongoClient
client=MongoClient()
db=client.answer
headers={"Cookie":"PHPSESSID=b8d06e9713804479bde8a5f7eaecf678", "User-Agent":"okhttp/3.11.0"}
course_dic={"药物化学":133816,
            "药理学":133815,
            #"毛中特":133471,
            "生药学":133780,
            #"临床医学概论":133763,
            #"天然药物化学":98799,
            #"15级药化":71676,
#            "药用高分子材料学":132904,
#            "药事管理学":98789
            }
#pprint(course_dic)
def convent(id):
    data={ "page":0, "size":30, "courseId":id}
    url=[i['link'] for i in requests.post('http://39.105.253.51:90//app/courseTest/list/history',headers=headers,data=data).json()['data']['list']]
    return url


def parse(url,name):
    result=[]
    for i in url:
        response=HtmlResponse(url=i,body=requests.get(i,headers=headers).content.decode('utf8').encode('utf8'))
        title = (i.strip() for i in response.css('span.item-title::text').extract() if i.strip())
        xuanxiang_a=(i.strip() for i in response.css('div.item-media::text').extract() if i.strip())
        xuanxiang=[i.strip() for i in response.css('div.item-title::text').extract()]
        daan=(i for i in response.xpath("//span[@style='color: #00B83F;']/text()").extract())     
        choice=(j+xuanxiang[i] for i,j in enumerate(xuanxiang_a))
        try:
            result.append(title.__next__())
            result.append(choice.__next__())
            for i in choice:
                result.append(i)
                if i[0]=="A":
                    result.insert(-1,daan.__next__())
                    result.insert(-1,title.__next__())
            result.append(daan.__next__())
        except StopIteration:
            pprint("error happend")
    pprint(result)
    ite=result.__iter__()
    b={}
    for i in ite:
        c=i
        b[c]=[]
        for j in ite:
            b[c].append(j)
            if j[0]=="正":
                break
    c=[{"title":i,"options":j[:-1],"answer":j[-1]} for i,j in b.items()]
    eval('db.{}.insert_many(c)'.format(name))


if __name__ == "__main__":
    for i,j in course_dic.items():
        print(i,j)
        parse(convent(j),i)
