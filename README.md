# Employees Registry Service


## Usage

All responses will have this form 

```json
{
    "data": "the data that we asked for",
    "message":"Description of what happened"
    
}
``` 

### List all emplyees

**Definition**

`GET /employees`

**Response**

- `200 OK` on seccess

```json
[
{
    "id": "employee id",
    "fistName":"employee first name",
    "lastName": "employee last name",
    "age" : "employee age",
    "yearsInService" : "number of years in the company"
}
{
    "id": "32",
    "fistName":"Zine",
    "lastName": "Mark",
    "age" : "26",
    "yearsInService" : "2"
}
]
``` 


### Adding a new employee

**Definition**

`POST /employees`

**Arguments**

- `"id":String` the unique identifier of employees
- `"firstName":String` fist name of the employee
- `"lastName":String` last name of the employee
- `"age":Integer` the age of the employee
- `"yearInService":Integer` number of years in the company 

IF a employee with the same id already exists, the employee will be overwritten.

**Response**

- `201 Object Created` on success

```json
{
    "id": "32",
    "fistName":"Zine",
    "lastName": "Mark",
    "age" : "26",
    "yearsInService" : "2"
}
``` 

## Lookup employee

**Definition**

`GET /employees/<id>`

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK`  on success

```json
{
    "id": "32",
    "fistName":"Zine",
    "lastName": "Mark",
    "age" : "26",
    "yearsInService" : "2"
}
``` 

## Delete a employee

**Definition**

`DELETE /employees/<id>`

**response**

- `404 Not found` if the employee does not exist
- `204 No content` on success


