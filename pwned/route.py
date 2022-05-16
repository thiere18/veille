from fastapi import APIRouter
from pwned.endpoint.presence import get_user, get_students
from pwned.endpoint.schemas import EmailIn, Student, StudentOut
from pwned.endpoint.utils import send_email

router=APIRouter()

@router.post('/add-student',response_model=StudentOut, tags=['presence'])
def getUsers(student: Student):
    return get_user(student)
@router.get('/get-users-csv',tags=['presence'])
def getUsersCsv():
    return get_students()

@router.post('/send-email',tags=['presence'])
def sendEmail(item: EmailIn):
    return send_email(item.email, item.name)
