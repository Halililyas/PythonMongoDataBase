import pymongo

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

result = mycollaction.find().sort('name') # Büyükten Kücüge Sıralama yapar
result2 = mycollaction.find().sort('name',-1) #  Kücüükten Büyüğe  Sıralama yapar
result3 = mycollaction.find().sort('price')
result4 = mycollaction.find().sort([('name',1),('price',-1)])
for i in result:
    print(i)