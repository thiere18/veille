from pydantic import BaseModel


class Student(BaseModel):
    prenom: str
    nom: str


class StudentOut(Student):

    class Config:
        orm_mode = True

class Email(BaseModel):
    email: str
class EmailIn(Email):
    name: str

class EmailDomain(Email):
    domain: str

class DomainDetails(BaseModel):
    domain: str