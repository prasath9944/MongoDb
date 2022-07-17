import pymongo

client = pymongo.MongoClient("mongodb+srv://prasathkkps:Luci1108@cluster0.ldqcx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name":"prasath",
    "email":"prasathks20@gmail.com",
    "surname":"kamalakannan"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
