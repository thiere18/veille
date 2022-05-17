import email
from re import I, U
from fastapi import FastAPI
import pypwned
from pwned.endpoint.schemas import DomainDetails, EmailDomain,Email

from fastapi import APIRouter

router=APIRouter()
your_hibp_key ='0a8f8f992cee4b9bb798a761db6fe950'
pwny = pypwned.pwned(your_hibp_key)


@router.get("/data-classes",tags=['pwned'] )
def root():
    # get the password from the request
    return pwny.getAllDataClasses()

@router.post("/get-paste")
def verify_paste(item: Email):
    return pwny.getAllBreachesForAccount(item.email)

@router.get('/get-hacked-websites', tags=['pwned'])
def getHackedWebsites():
    return pwny.getAllBreaches()



@router.post('/verify-email-password/specific-domain', tags=['pwned'])
def verify_specific_domain(user:EmailDomain):
    return pwny.getAllBreachesForAccount(user.email, user.domain)


@router.post('/specific-domain-detail', tags=['pwned'])
def specific_domain_detail(user:DomainDetails):
    return pwny.getAllBreaches(domain=user.domain)

