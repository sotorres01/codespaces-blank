from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class PersonIn(BaseModel):
    name: str
    email: str
    telephone: str
    id: int 

class PlaceIn(BaseModel):
    name: str
    ubication: str
    type_place: str

class AutorizedPersonnelIn(BaseModel):
    name: str
    email: str
    telephone: str
    id: int
    rolname: str
    roltype: str
    rolcode: int

class EventIn(BaseModel):
    place: PlaceIn
    id: int
    timeIn: int
    timeOut: int
    date: str

class VisitorIn(BaseModel):
    responsible: AutorizedPersonnelIn
    event: EventIn
    name: str
    email: str
    telephone: str
    id: int

class PackageIn(BaseModel):
    subject: VisitorIn
    name: str
    description: str
    code: int

class RegisterIn(BaseModel):
    subject: PersonIn
    zone: PlaceIn

@app.get("/")
async def root():
    return {"hello world"}

@app.post("/person/")
async def create_person(person: PersonIn):
    # Aquí puedes agregar el código para crear una nueva instancia de Person y guardarla en una base de datos o en memoria
    return {"message": "Person created"}

@app.post("/place/")
async def create_place(place: PlaceIn):
    # Aquí puedes agregar el código para crear una nueva instancia de AutorizedPersonnel y guardarla en una base de datos o en memoria
    return {"message": "Place created"}

@app.post("/autorized_personnel/")
async def create_autorized_personnel(autorized_personnel: AutorizedPersonnelIn):
    # Aquí puedes agregar el código para crear una nueva instancia de AutorizedPersonnel y guardarla en una base de datos o en memoria
    return {"message": "Autorized personnel created"}

@app.post("/event/")
async def create_event(event: EventIn):
    # Aquí puedes agregar el código para crear una nueva instancia de Event y guardarla en una base de datos o en memoria
    return {"message": "Event created"}

@app.post("/visitor/")
async def create_visitor(visitor: VisitorIn):
    # Aquí puedes agregar el código para crear una nueva instancia de Visitor y guardarla en una base de datos o en memoria
    return {"message": "Visitor created"}

@app.post("/package/")
async def create_package(package: PackageIn):
    # Aquí puedes agregar el código para crear una nueva instancia de Package y guardarla en una base de datos o en memoria
    return {"message": "Package created"}

@app.post("/register/")
async def create_register(register: RegisterIn):
    # Aquí puedes agregar el código para crear una nueva instancia de Register y guardarla en una base de datos o en memoria
    return {"message": "Register created"}