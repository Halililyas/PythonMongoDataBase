import pymongo

#mycilent = pymongo.MongoClient("mongodb://localhost:27017")
mycilent = pymongo.MongoClient("mongodb+srv://ilyas:Ljc8IA52rgTzn1J1@cluster0.j4csb30.mongodb.net/node-app?retryWrites=true&w=majority")
mydb = mycilent["node-app"]
mycollaction = mydb["products"]

product = {"name":"Samsug s7","price":4000}
# result = mycollaction.insert_one(product) # products collection içerisinde yukarıda yazdığımız dic yapıyı yolluyoruz 
# Burda dikkat edilmesi hususunda insert_one demek sadece bir kayıt ekleneceği olması gerekir 
# print(result)
# print(type(result))
# print(result.inserted_id)## Eklenecek olan ürünün IDsını oğrenmiş olduk 


productlist =[
    {"name":"Samsug s7","price":4000},
    {"name":"Samsug s8","price":5000},
    {"name":"Samsug s9","price":6000},
    {"name":"Samsug s10","price":7000},
    {"name":"Samsug s6","price":3000},
    {"name":"Samsug s23","price":9000}
]
# id sini bu şekilde bizede verebiliriz 
productlist2 =[
    {"_id":1,"name":"Iphone 7","price":4000},
    {"_id":2,"name":"Iphone 8","price":5000},
    {"_id":3,"name":"Iphone 9","price":6000},
    {"_id":4,"name":"Iphone 10","price":7000},
    {"_id":5,"name":"Iphone 6","price":3000},
    {"_id":6,"name":"Iphone 15","price":9000}
]
productlist3 =[
    {"name":"Iphone 7","price":4000,"Yorum":"İyi Telefon"},
    {"name":"Iphone 8","price":5000,"kategory":["elektronik","Telefon"]}
    
]
result = mycollaction.insert_many(productlist3)## Burda birden çok veri eklemek için kullanırız inserttmany
print(result.inserted_ids)# Eklenen ürünlerin Id sini verir Burda s olduğuna dikkat 