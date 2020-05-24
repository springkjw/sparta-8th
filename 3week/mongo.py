from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
# 데이터베이스 하나를 생성하는데 그 이름이 dbsparta

# 데이터 넣기(insert)
# db.users.insert_one(
#     {
#         "name": "Bob",
#         "age": 20
#     }
# )

# 데이터 조회
all_users = list(db.users.find())
# list() => python list로 변환

# 데이터 필터 조회
some_users = list(db.users.find({'age': 99}))
# print(some_users)

# 데이터 조회, 특정 key만 조회
some_key_users = list(db.users.find({}, {'_id': False}))
print(some_key_users)

# 데이터 수정
# db.users.update_many(
#     {'age': 20},
#     {'$set': {'name': 'vincent'}}
# )
# update_many: 필터 조건에 만족하는 모든 데이터를 수정
# update_one: 필터 조건에 만족하는 첫번째 데이터만 수정
# db.users.update_one(
#     {'age': 20},
#     {'$set': {'name': 'vincent'}}
# )

# 데이터 삭제
# db.users.delete_one({})
db.users.delete_many({})


# CRUD
# Create - Retreive - Update - Delete