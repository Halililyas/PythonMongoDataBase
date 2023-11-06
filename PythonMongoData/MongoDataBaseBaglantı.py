import pymongo

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

# result = mycollaction.find_one() # Bulduğu İlk ürünü getirir sadece tek bir ürün getirir
# print(result)

result = mycollaction.find() # collection içerisinde bulunan bütün ürünleri getirir 
result2 = mycollaction.find({},{"_id":0})# Bu şekilde tanım yapıldığında id: 0 dediğimizde id kolonunu getirme demiş olduk 
for i in result2:
    print(i)