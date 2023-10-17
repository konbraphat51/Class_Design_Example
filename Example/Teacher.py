from typing import Dict, List

from TeachingRelationship import TeachingRelationship
from User import User

class Teacher(User):
    '''
    User Data for teachers
    '''

    def __init__(self, id: int, name: str, salary_rate: float):
        super().__init__(id, name)
        
        self.salary_rate :float = salary_rate
        
        #day -> TeachingRelashionship
        self.teaching_relationships :Dict[str, TeachingRelationship] = {}
        
    #would be better if method's name is verb
    def salary(self) -> int:
        '''
        Returns how much money the student has to pay.
        '''
           
        _salary = 0  # underbar for avoid duplication with spendings() method
        for teaching_relationship in self.teaching_relationships.values():
            _salary += int(teaching_relationship.tuition * self.salary_rate)
        
        return _salary
        
    def show_details(self) -> str:
        #top part
        output = super().show_details()
        
        #category
        output += "\n Category: Teacher"
        
        #spendings
        output += f'\n Salary {self.salary()}'
        
        #relashionships
        output += '\n Relashionships:'
        for teaching_relationship in self.teaching_relationships.values():
            output += f'\n {teaching_relationship.show_details(needs_student = True)}'
        
        return output
    
    def calculate_money(self) -> int:
        return -self.salary()