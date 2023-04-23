#the classes of person and place are imported so that this class can be a relationship between these two
from person import Person 
from place import Place 


#the registration class that will serve to register the entry of people is initialized
class Register():
    '''
    the constructor of the class is made, through which we are going to call the place class and the person class
    subject: is the subject that will represent the person class
    zone: is the area that will represent the place where the person was
    '''
    def __init__(self, subject: Person, zone: Place):
            self.subject = subject
            self.zone = zone
    
    '''
    gets the subject that is part of person hat enters

    return to subject
    '''
    @property
    def subject(self) -> str:
        return self._subject
    
    '''
    sets the subject that enters

    Args:
        value (str): gives a value to the subject that enters
    '''
    @subject.setter
    def subject(self, value) -> str:
        self._subject = value

    '''
    gets the zone by referencing the place class

    return to the zone 
    '''
    @property
    def zone(self) -> str:
        return self.zone 
    
    '''
    sets the zone the subject entered

    Args:
        value (str): gives a value to the zone that the subject entereds
    '''
    @zone.setter
    def zone(self, value) -> str:
        self.zone = value

