from pymongo import MongoClient

client = MongoClient()
# 此处修改数据库名字
db = client['bbs']


def inii(*args):
    print(type(args))

if __name__ == '__main__':
    ds = db['Reply'].find({'user_id': 7})
    for i in ds:
        print(i)
    ds2 = db['Reply'].find({'user_id': 7})
    sort = ('created_time', -1)
    ds2 = ds2.sort(*sort).distinct('{"topic_id":true,"created_time":true}')
    print(ds2)
