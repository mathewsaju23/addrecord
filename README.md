# Addrecord

## Run

1)Created an api with route (/task/new): It takes (name, description, email) in the request body and
creates a new record in the database
a. Each record should have an unique “id” parameter
b. The “createdAt” parameter (with timestamp value) should be automatically added, whenever a
new record is created..
Sample Request Body:
{
"name":"Maths assignment",
"description":"Complete todays assignment",
"email":"user@example.com"
}

2)Created a GET api with route (/task/all) : It results all the saved records in the database as a list of
objects in the response. Each object should have (id, name, description, email, createdAt) parameters.
Sample response:
{
{
"data": [
{
"id": "c39fd77c-6df5-4ffe-879a-5ccee5d77cbf",
"name": "Maths assignment",
"description": "Complete todays assignment",
"email": "user@example.com",
"createdAt": "2021-12-24T18:10:22Z"
}
]
}
}

1. Clone the repository

```shell
git clone https://github.com/mathewsaju23/addrecord.git
```

2. Move into the repo

```shell
cd addrecord
```

3. Install the dependencies

4. Run the file

```shell
python3 manage.py runserver
```
