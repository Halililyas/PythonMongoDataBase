import pymongo
from bson.objectid import ObjectId

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

filter = {"name":"Samsug s6"}
#result = mycollaction.find({"name":"Samsung s6"})
result2 = mycollaction.find(filter)
result3 = mycollaction.find_one({"_id": ObjectId("653a891279f3a92a3bdf75c4")})
result4 = mycollaction.find(
    {
        "name":{
            "$in":["Samsug s6","Samsug s7"] #3 Burdaki in $in verilen name kolonundan belirtilen ler getir demiş olduk 
        }
    }
)
result5 = mycollaction.find(
    {
        "price":{
            "$gt":2000 #Burda price kolonu içerisinde 2000 den buyuk olanları getir demiş olduk 
        }
    }
)
result6 = mycollaction.find(
    {
        "price":{
            "$gte":2000 # $gte Burda price kolonu içerisinde 2000 den buyuk ve eşit olanları getir demiş olduk 
        }
    }
)
result6 = mycollaction.find(
    {
        "price":{
            "$eq":7000 # $eq Burda price kolonu içerisinde 7000  eşit olanları getir demiş olduk 
        }
    }
)
result7 = mycollaction.find(
    {
        "price":{
            "$lt":7000 # $lt Burda price kolonu içerisinde 7000 den küçük olanları getir demiş olduk 
        }
    }
)
result8 = mycollaction.find(
    {
        "price":{
            "$lte":7000 # $lt Burda price kolonu içerisinde 7000 den küçük ve eşit olanları getir demiş olduk 
        }
    }
)
result9 = mycollaction.find(
    {
        "name":{
            "$regex":"^S" # $regex  name kolonu içerisinde Baş harfi S olanları getir  
        }
    }
)

#print(result3)
for i in result9:
    print(i)
