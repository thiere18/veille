import email
from re import I, U
from fastapi import FastAPI
from pydantic import BaseModel
import pypwned, os
from demo.endpoint.schemas import DomainDetails, EmailDomain, EmailIn, Student, StudentOut, Email
from demo.endpoint.presence import get_user, get_students
from demo.endpoint.utils import send_email
app = FastAPI()
your_hibp_key ='0a8f8f992cee4b9bb798a761db6fe950'



@app.get("/verif",tags=['pwned'] )
def root():
    # get the password from the request
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllDataClasses()

@app.post("/verify/password")
def verify_password(item: Email):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreachesForAccount(item.email)

@app.post("/get-paste")
def verify_paste(item: Email):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreachesForAccount(item.email)

@app.get('/get-hacked-websites', tags=['pwned'])
def getHackedWebsites():
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreaches()



@app.post('/verify-email-password/specific-domain', tags=['pwned'])
def verify_specific_domain(user:EmailDomain):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreaches(user.email, user.domain)


@app.post('/specific-domain-detail', tags=['pwned'])
def specific_domain_detail(user:DomainDetails):
    pwny = pypwned.pwned(your_hibp_key)
    return pwny.getAllBreaches(domain=user.domain)

@app.post('/add-student',response_model=StudentOut, tags=['presence'])
def getUsers(student: Student):
    return get_user(student)
@app.get('/get-users-csv',tags=['presence'])
def getUsersCsv():
    return get_students()

@app.post('/send-email',tags=['presence'])
def sendEmail(item: EmailIn):
    return send_email(item.email, item.name)
