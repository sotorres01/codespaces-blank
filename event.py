from place import Place

class Event():
    def __init__(self, place: Place, id: int = 0, timeIn: int = 0, timeOut: int = 0, date: str = 'date'):
        self.id = id
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.date = date
        self.place = place
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value) -> None:
        self._id = value   
    
    @property
    def timeIn(self) -> int:
        return self._timeIn
    
    @timeIn.setter
    def timeIn(self, value) -> None:
        self._timeIn = value
            
    @property
    def timeOut(self) -> int:
        return self._timeOut
    
    @timeOut.setter
    def timeOut(self, value) -> None:
        self._timeOut = value 
            
    @property
    def date(self) -> str:
        return self._date
    
    @date.setter
    def date(self, value) -> None:
        self._date = value 
            
    @property
    def place(self) -> Place:
        return self._place
    
    @place.setter
    def place(self, value) -> None:
        self._place = value 
    
    def __str__(self) -> str:
        return f"Event: {self.place} - {self.id} - {self.timeIn} - {self.timeOut} - {self.date}"
    
    def equals(self, other) -> bool:
        if isinstance(other, Event):
            return self.place == other.place and self.id == other.id and self.timeIn == other.timeIn and self.timeOut == other.timeOut and self.date == other.date
        return False
            

