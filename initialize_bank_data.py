import json
db={
    "1001":{
        "name":"shrey",
        "password":"1234",
        "balance":9000,
    }
}
with open("accounts/1001","w") as fp:
    json.dump(db,fp)
last_account=1001
with open("last_account.json","w") as fp:
    json.dump(last_account,fp)
print("bank.json and last_account.json successfully created")
