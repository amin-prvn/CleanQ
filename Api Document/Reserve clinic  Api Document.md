## Reservation view
1. Main url

    <localhost:8000/api/v1/reserve>

2. Reserve a clinic for patient [POST]
- Header :
```
token = JWT_token
```
- Body :
```
{
    "clinic": id,
    "description": "description"
}
```
- Response :    
```
{
    "patient": id,
    "clinic": id,
    "time": "2021-01-30T11:00:00Z",
    "description": "description"
}
```
