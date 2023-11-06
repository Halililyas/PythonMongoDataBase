import pymongo

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

result = mycollaction.update_one(
    {"name":"Samsug s7"}, ## Güncellenecek olan kolondaki değer
    {"$set":{"name":"Xiomi"}} # Ve Yeni Ad Sadece Name Kolonu 
    
)
result = mycollaction.update_one(
    {"name":"Samsug s9"}, 
    {"$set":{"name":"Xiomi","price":4000}} 
    
)
query = {"name":"Samsug s8"}
newValues = {"$set":{"name":"Xiomi","price":4000}}
result = mycollaction.update_one(query,newValues)
    
     
    

for i in mycollaction.find():
    print(i)