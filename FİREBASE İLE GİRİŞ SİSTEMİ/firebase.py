from firebase import firebase
firebase=firebase.FirebaseApplication('https://normal-1f2de-default-rtdb.firebaseio.com/',None)

#create

data={
    "name":"gülbahar",
    "password":"ak",
        }


firebase.patch('Users/first',data) 


rs=firebase.get('Users/first','')
print(rs["name"])
print(rs["password"])



for i in rs:
    print(rs)
