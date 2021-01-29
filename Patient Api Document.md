## Patient view
1. Main url
```
localhost:8000/api/v1/patient
```
2. Get patient reservation list [GET]
- Header :
```
token = JWT_token
```
* Query parameters :

    - Order past reservation : 
        ```
        ?ordering=past
        ```
    - Order upcoming reservation :
        ```
        ?ordering=upcoming
        ```
- Response :    
```
[
    {
        "clinic": id,
        "patient": id,
        "time": "2021-01-29T15:30:00Z",
        "description": "description"
    },
    {
        "clinic": 3,
        "patient": 4,
        "time": "2021-01-29T16:00:00Z",
        "description": "description"
    }
]
```
3. Rreate patient [POST]
- Body :
```
{
    "email":"test@example.com",
    "password":"pass",
    "name":"patient",
    "phone":"phone",
}
```
- Response :    
```
{
    "token": "JWT_token"
}
```
4. Update patient [PUT]
- Header :
```
token = JWT_token
```
- Body :
```
{
    "email":"test@example.com",
    "password":"pass",
    "name":"patient",
    "phone":"phone",
}
```
- Response :    
```
{
    "name":"patient",
    "phone":"phone",
}
```
5. Delete patient [DELETE]
- Header :
```
token = JWT_token
```

- Status code :    
```
204 no content
```
