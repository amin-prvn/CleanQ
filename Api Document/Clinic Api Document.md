## Clinic view
1. Main url

    <localhost:8000/api/v1/clinic>

2. Get clinic reservation list [GET]
- Header :
```
token = JWT_token
```
* Query parameters :

    - Order past reservation : 

        <localhost:8000/api/v1/clinic?ordering=past>
        
    - Order upcoming reservation :

        <localhost:8000/api/v1/clinic?ordering=upcoming>
- Response :    
```
[
    {
        "patient": id,
        "clinic": id,
        "time": "2021-01-29T15:30:00Z",
        "description": "description"
    },
    {
        "patient": 3,
        "clinic": 4,
        "time": "2021-01-29T16:00:00Z",
        "description": "description"
    }
]
```
3. Create clinic [POST]
- Body :
```
{
    "email":"test@example.com",
    "password":"pass",
    "name":"clinic",
    "address":"address",
    "phone":"phone",
    "description":"description..."
}
```
- Response :    
```
{
    "token": "JWT_token"
}
```
4. Update clinic [PUT]
- Header :
```
token = JWT_token
```
- Body :
```
{
    "email":"test@example.com",
    "password":"pass",
    "name":"clinic",
    "address":"address",
    "phone":"phone",
    "description":"description..."
}
```
- Response :    
```
{
    "name":"clinic",
    "address":"address",
    "phone":"phone",
    "description":"description..."
}
```
5. Delete clinic [DELETE]
- Header :
```
token = JWT_token
```

- Status code :    
```
204 no content
```
