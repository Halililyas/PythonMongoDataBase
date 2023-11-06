import pymongo

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

for i in mycollaction.find():
    print(i)

print("*"*50)

mycollaction.delete_one({"name":"Iphone 10"})


for i in mycollaction.find():
    print(i)

print("*"*50)