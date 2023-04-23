from person import Person

#the definition of the father class IncomePerson
class AutorizedPersonnel(Person):
    #the constructor of each of the package attributes is created
        def __init__(self, name: str = 'name', email: str = 'email', telephone: str = 'telephone', id: int = 0, rolname: str = 'rolname', roltype: str = 'roltype', rolcode: int = 0):
        #with the super() function we can inherit the attributes of the package class
            super().__init__(name, email, telephone, id)
            self.rolname = rolname
            self.roltype = roltype
            self.rolcode = rolcode
        
        #we define the get and set of each of the attributes that are private
        @property
        def rolname(self) -> str:
            return self.rolname
    
        @rolname.setter
        def rolname(self, value) -> str:
            self.rolname = value
            
        @property
        def roltype(self) -> str:
            return self.roltype
    
        @roltype.setter
        def roltype(self, value) -> str:
            self.roltype = value
            
        @property
        def rolcode(self) -> int:
            return self.rolcode
    
        @rolcode.setter
        def rolcode(self, value) -> int:
            self.rolcode = value