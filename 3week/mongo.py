from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
# 데이터베이스 하나를 생성하는데 그 이름이 dbsparta

# 데이터 넣기(insert)
db.users.insert_one(
    {
        "name": "Bob",
        "age": 20
    }
)