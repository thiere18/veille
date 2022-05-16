import csv
from io import BytesIO
from pwned.endpoint.schemas import Student
from fastapi.responses import StreamingResponse
# from pwned.endpoint.utils import send_simple_message
def  create_csv(data):
    with open('data.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
def get_user(student: Student):
    create_csv([student.prenom,student.nom])
    return student

    
def get_students():
    with open(f"data.csv", "rb") as f:
            data = BytesIO(f.read())
    return StreamingResponse(data, media_type="text/csv")