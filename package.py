#The visitor class is imported to be able to establish the relationship between the object that enters and the person who takes it
from visitor import Visitor


class Package():
    def __init__(self, subject: Visitor, name: str = 'name', description: str = 'description', code: int = 0):
        self.name = name
        self.description = description
        self.code = code 
        self.subject = subject 
        
    @property
    def name(self) -> str:
            return self._name
    
    @name.setter 
    def name(self, value) -> str:
            self._name = value 

    @property
    def description(self) -> str:
            return self._description
    
    @description.setter 
    def description(self, value) -> str:
            self._description = value 

    @property
    def code(self) -> str:
            return self._code
    
    @code.setter 
    def code(self, value) -> str:
            self._code = value 

    @property
    def subject(self) -> str:
            return self._subject
    
    @subject.setter 
    def subject(self, value) -> str:
            self._subject = value 

    