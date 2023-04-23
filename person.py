#the definition of the father class IncomePerson
class Person(object):
    #the constructor of each of the package attributes is created
        def __init__(self, name: str = 'name', email: str = 'email', telephone: str = 'telephone', id: int = 0):
            self.name = name
            self.email = email
            self.telephone = telephone
            self.id = id
        
        #we define the get and set of each of the attributes that are private
        @property
        def name(self) -> str:
            return self._name
    
        @name.setter
        def name(self, value) -> str:
            self._name = value
 
        @property
        def email(self) -> str:
            return self._email
    
        @email.setter
        def email(self, value) -> str:
            self._email = value 

        @property
        def telephone(self) -> str:
            return self._telephone
    
        @telephone.setter
        def telephone(self, value) -> str:
            self._telephone = value
            
        @property
        def id(self) -> int:
            return self._id
    
        @id.setter
        def id(self, value) -> int:
            self._id = value          

            