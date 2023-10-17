from typing import Dict

from TeachingRelationship import TeachingRelationship
from User import User

class Student(User):
    '''
    User data for students
    '''
    
    def __init__(self, id: int, name: str, adress: str):
        '''
        Register initial data
        '''
        super().__init__(id, name)
        
        self.adress: str = adress
        
        #day -> TeachingRelashionship
        self.teaching_relationships :Dict[str, TeachingRelationship] = {}
        
    #would be better if method's name is verb
    def spendings(self) -> int:
        '''
        Returns how much money the student has to pay.
        '''
           
        _spendings = 0  # underbar for avoid duplication with spendings() method
        for teaching_relationship in self.teaching_relationships.values():
            _spendings += teaching_relationship.tuition
        
        return _spendings
        
    def show_details(self) -> str:
        #top part
        output = super().show_details()
        
        #category
        output += "\n Category: Student"
        
        #adress
        output += f'\n Adress: {self.adress}'
        
        #spendings
        output += f'\n Spendings: {self.spendings()}'
        
        #relashionships
        output += '\n Relashionships:'
        for teaching_relationship in self.teaching_relationships.values():
            output += f'\n {teaching_relationship.show_details(needs_teacher = True)}'
        
        return output
    
    def calculate_money(self) -> int:
        return self.spendings()