from TeachingRelationship import TeachingRelationship

class User:
    '''
    Base class for all users in the management system.
    '''
    
    def __init__(self, id: int, name: str):
        '''
        Register initial data
        '''
        self.id :int = id
        self.name :str = name
        
    def get_place(self, day: str) -> str:
        '''
        Where the teaching occures in the given day.
        '''
        
        raise NotImplementedError
    
    def show_details(self) -> str:
        '''
        Returns user description data text.
        '''
        
        return f'ID: {self.id}\n Name: {self.name}'
    
    def calculate_money(self) -> int:
        '''
        Returns the amount of money the user has to pay / we have to pay.  
        Payings from us to the user are negative.
        '''
        
        raise NotImplementedError
    
    def register_teaching_relashionship_day(self, day: str, teaching_relashionship: TeachingRelationship) -> None:
        '''
        Register a new teaching relashionship for students and teachers
        '''
        
        #better to make a duplication checking here
        
        #register
        self.teaching_relationships[day] = teaching_relashionship
        
    def has_teaching_relationship(self, relationship: TeachingRelationship) -> bool:
        '''
        Returns True if the user has the given teaching relashionship
        '''
        
        return relationship in self.teaching_relationships.values()