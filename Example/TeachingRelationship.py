class TeachingRelationship:
    """
    Holds data of relashionship of teaching between student and teacher
    """
    
    def __init__(self, day: str, tuition: int):
        """
        Register initial data
        """
        
        #it could be **efficient** when student & teacher here, but it causes circular reference, which is not **clean**
        
        self.day :str       = day   #using **enum** would be better
        self.tuition :int   = tuition
        
    def show_details(self, needs_student: bool = False, needs_teacher: bool = False) -> str:
        '''
        Return text details of this teaching relashionship.
        '''
        
        from Manager import Manager
        
        output = f'Day: {self.day}\n Tuition: {self.tuition}'
        
        if needs_student:
            student = Manager.singleton.find_student_with_relashionship(self)
            
            output += f'\n Student: {student.name}'
            
        if needs_teacher:
            teacher = Manager.singleton.find_teacher_with_relashionship(self)
            
            output += f'\n Teacher: {teacher.name}'
            
        return output