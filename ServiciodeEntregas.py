

class Package:
    W_GR_100 = 1.0
    def __init__(self, code: int = 0
                 , weight: float = 0.0
                 , description: str = "description", 
                 cost: float = 0.0):
        self.__code = code
        self.__weight = weight
        self.__description = description
        self.__cost = cost
        
    def  get_code(self):  
        return self.__code 
    
    def set_code(self, code):
        self.__code = code  
        
    def  get_weight(self):  
        return self.__weight
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def  get_description(self):  
        return self.__description
    
    def set_description(self, description):
        self.__description = description
        
    def  get_cost(self):  
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost
         
    def __str__(self):
        return f"El codigo del producto es: {self.__code}, el peso es: {self.__weight}, la descripcion es: {self.__description}, el costo es: {self.__cost} "
    
    def calculate(self):
        print(f"El costo de envio del paquete{self.__code} es: ", self.__weight * self.__cost) 
        

class StandarPackage(Package):
    def __init__(self, code: int = 0
                 , weight: float = 1.0, 
                 description: str ="description"
                 , cost: float = 1.0,
                 fixedfee: float = 1.0):
        self.__code = code
        self.__weight = weight
        self.__description = description
        self.__cost = cost
        self.__fixedfee = fixedfee 

    def  get_code(self):  
        return self.__code 
    
    def set_code(self, code):
        self.__code = code  
        
    def  get_weight(self):  
        return self.__weight
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def  get_description(self):  
        return self.__description
    
    def set_description(self, description):
        self.__description = description
        
    def  get_cost(self):  
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost
    def  get_fixedfee(self):  
        return self.__fixedfee
    
    def set_fixedfee(self,fixedfee):
        self.__fixedfee= fixedfee
        
    def __str__(self):
        return f"la cuota fija que contiene este producto es: {self.__fixedfee}"
        
    def calculate (self):
        print(f"el costo de envio del paquete{self.__code} es:", self.__fixedfee + (self.__weight * self.__cost) ) 
        
        
class Overweight(Package):
    def __init__(self, code: int = 0
                 , weight: float = 1.0
                 , description: str ="description"
                 , cost: float = 1.0
                 , overweight: float = 0.0):
        self.__code = code
        self.__weight = weight
        self.__description = description
        self.__cost = cost
        self.__overweight = overweight 
        
    def __str__(self):
        return f"El sobre peso que contiene este producto es: {self.__overweight}"
      
    def  get_code(self):  
        return self.__code 
    
    def set_code(self, code):
        self.__code = code  
        
    def  get_weight(self):  
        return self.__weight
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def  get_description(self):  
        return self.__description
    
    def set_description(self, description):
        self.__description = description
        
    def  get_cost(self):  
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost
      
    def  get_overweight(self):  
        return self.__overweight
    
    def set_fixedfee(self,overweight):
        self.__overweight= overweight
        
    def calculate(self): 
        print(f"el costo de envio del paquete{self.__code} es:", self.__overweight + (self.__weight * self.__cost) ) 
    

  
class Person():
    
    def __init__(self, name: str= "name"
               , lastname: str="lastname"
               , dnicard: int = 0
               , birthdate: str = "00/00/00"
               , phone=0):
        
        self.__name = name
        self.__lastname = lastname
        self.__dnicard = dnicard
        self.__birthdate = birthdate
        self.__phone = phone
        

    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name

    def get_lastname(self):
        return self.__lastname
    
    def set_lastname(self, lastname):
        self.__lastname = lastname
    

    def get_dnicard(self):
        return self.__dnicard
    
    def set_dnicard(self, dnicard):
        self.__dnicard = dnicard
        
    def get_birthdate(self):
        return self.__birthdate
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone
        
    def __str__(self):
        return f"el nombre de la persona es: {self.__name}{self.__lastname}, el cedula es: {self.__dnicard}, la fecha del nacimiento es: {self.__birthdate}, y el mumero de telefono es{self.__phone}"

class Address():

    def __init__(self,
                 city: str="",
                 neighborhood: str="",
                 street_number: int=0,
                 street_name: str="",
                 batch_number: int = 0,
                 postal_code: int = 0):
        self.__city = city
        self.__neighborhood = neighborhood 
        self.__street_number = street_number
        self.__street_name = street_name
        self.__batch_number = batch_number
        self.__postal_code = postal_code

    def get_city(self):
        return self.__city
        
    def set_city(self, city):
        self.__city = city

    def get_neighborhood(self):
        return self.__neighborhood

    def set_neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood
    
    def get_street_number(self):
        return self.__street_number
        
    def set_street_number(self, street_number):
        self.__street_number = street_number
    
    def get_street_name(self):
        return self.__street_name 

    def set_street_name(self, street_name):
        self.__street_name = street_name
    
    def get_batch_number(self):
        return self.__batch_number

    def set_batch_number(self, batch_number):
        self.__batch_number = batch_number
      
    def get_postal_code(self):
        return self.__postal_code 

    def set_postal_code(self, postalcode):
        self.__postal_code = postalcode 

    def __str__(self):
        return f"la ciudad donde vive es: {self.__city}, el barrio donde vive es: {self.__neighborhood}, el nombre y numero de la calle es {self.__street_name}{self.__street_number}, el numero del lote es{self.__batch_number}, y el codigo postal de donde vive es: {self.__postal_code}"

        
        
class delivor(Person):
    def __init__(self,
                 name: str= "", 
                 lastname: str="",
                 dnicard: int = 0,
                 birthdate: str="",
                 phone: int = 0,
                 idperson: str="",
                 date: str ="",
                 time: str ="",
                 sender=Person(),
                 receiver=Person(),
                 sender_add=Address(),
                 receiver_add=Address(),
                 contact=Person(),
                 items=[Package()]):
        
        self.__idpersona = idperson 
        self.__date = date
        self.__time = time
        self.__sender = Person() 
        if (sender != Person):
            print ("\nEl valor es incorrecto")
        else:
            self.__sender = Person()
            
        self.__receiver = Person() 
        if (receiver != Person):
            print ("\nEl valor es incorrecto")
        else:
            self.__receiver = Person() 
            
        self.__sender_add = Address() 
        if (sender_add!= Address()):
            print ("\nEl valor es incorrecto")
        else:
            self.__sender_add = Address()
            
        self.__receiver_add = Address() 
        if (receiver_add!= Address()):
            print ("\nEl valor es incorrecto")
        else:
            self.__receiver_add = Address()
            
        self.__contact = Person() 
        if (contact != Person):
            print ("\nEl valor es incorrecto")
        else:
            self.__contact = Person() 
            
        self.__items = [Package()] 
        if (items != Package()):
            print ("\nNULLL")
        else:
            self.__items = Package()


    def get_idpersona(self):
        return self.__idpersona
    
    def set_idpersona(self, idpersona):
        self.__idpersona = idpersona
        
    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date


    def get_time(self):
        return self.__time
    
    def set_time(self, time):
        self.__time = time
        
    def get_sender(self):
        return self.__sender
    
    def set_sender(self, sender):
        if type (sender) != Person:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__sender = Person( ) 
        
    def get_receiver(self):
        return self.__receiver
    
    def set_receiver(self, receiver): 
        if type (receiver) != Person:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__receiver = Person() 
        
    def get_sender_add(self):
        return self.__sender_add

    def set_sender_add(self, sender_add):
         if type (sender_add) != Address:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
         else:
            self.__sender_add = Address()
        
    def get_receiver_add(self):
        return self.__receiver_add
    
    def set_receiver_add(self, receiver_add):
        if type (receiver_add) != Address:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__receiver_add = Address()

    def get_contact(self):
        return self.__contact
    
    def set_contact(self, contact):
        if type (contact) != Person:
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__contact = Person() 
    
    def get_items(self):
        return self.__items
    
    def set_items(self, items):
        if (items != Package()):
            print ("\n¡¡El dato ingresado es inválido!!, por favor ingrese un nuevo dato")
        else:
            self.__items = [Package()]

    # __str__
    def _str_(self):
        return f"el Id: {self.__idpersona}, la fecha es: {self.__date}, el tiempo de entrega es{self.__time}, la informacion del que envia es: {self.__sender} la informacion del que lo recibe es: , {self.__receiver}  " 


