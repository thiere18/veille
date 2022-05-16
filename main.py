
from re import A
from fastapi import FastAPI
import pypwned
from pwned.endpoint.schemas import DomainDetails, EmailDomain, EmailIn, Student, StudentOut, Email
from pwned.endpoint.presence import get_user, get_students
from pwned.endpoint.utils import send_email
from pwned.router import router as pwned_router
from user_crud.router import router as user_router
from pwned.route import router as presence_router

app = FastAPI()
your_hibp_key ='0a8f8f992cee4b9bb798a761db6fe950'
pwny = pypwned.pwned(your_hibp_key)
app.include_router(pwned_router, prefix='/pwned', tags=['pwned'])
app.include_router(user_router, tags=['user'])
app.include_router(presence_router, prefix='/presence', tags=['presence'])


@app.post("/verify/password")
def verify_password(item: Email):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreachesForAccount(item.email)

@app.post("/get-paste")
def verify_paste(item: Email):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreachesForAccount(item.email)

