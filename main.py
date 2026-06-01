from fastapi import FastAPI

app = FastAPI()

students = {}


@app.get("/")
def home():

    return {
        "message":
        "FastAPI CRUD"
    }


# CREATE
@app.post("/students")
def create_student(
        id:int,
        hours_studied:int,
        previous_scores:int
):

    students[id] = {

        "hours_studied":
        hours_studied,

        "previous_scores":
        previous_scores

    }

    return {

        "message":
        "Created",

        "data":
        students[id]

    }


# READ ALL
@app.get("/students")
def get_students():

    return students


# UPDATE
@app.put("/students/{id}")
def update_student(
        id:int,
        hours_studied:int,
        previous_scores:int
):

    if id not in students:

        return {
            "message":
            "Not found"
        }

    students[id] = {

        "hours_studied":
        hours_studied,

        "previous_scores":
        previous_scores

    }

    return students[id]


# DELETE
@app.delete("/students/{id}")
def delete_student(id:int):

    if id not in students:

        return {
            "message":
            "Not found"
        }

    deleted = students.pop(id)

    return {

        "message":
        "Deleted",

        "data":
        deleted

    }