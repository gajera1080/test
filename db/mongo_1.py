from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["kaluo"]
collection = db["student"]

while True:
    print("\n---------------------")
    print("Enter 1 for INSERT")
    print("Enter 2 for UPDATE")
    print("Enter 3 for DELETE")
    print("Enter 4 for LIST")
    print("Enter 5 to Exit")
    val_get = int(input("--Enter Value: "))

    match val_get:
        case 1:
            nm_get = input("--Enter Name: ")
            collection.insert_one({"name": nm_get})
        case 2:
            nm_get = input("--Enter Name: ")
            new_nm_get = input("--Enter New Name: ")
            collection.update_many({"name": nm_get}, {"$set": {"name": new_nm_get}})
        case 3:
            nm_get = input("--Enter Name: ")
            collection.delete_one({"name": nm_get})
        case 4:
            for documemts in collection.find():
                print(documemts)
        case 5:
            break
        case _:
            print("Unknown Choice")
