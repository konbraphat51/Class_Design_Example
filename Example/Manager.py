from __future__ import annotations
import json
from typing import List

from User import User
from Teacher import Teacher
from Student import Student
from TeachingRelationship import TeachingRelationship

class Manager:
    '''
    Entire management system
    '''
    
    #the only instance of this class
    singleton: Manager = None
    
    def __init__(self):
        '''
        Prepare initial data
        '''

        self.teachers: List[Teacher] = []
        self.students: List[Student] = []

        #singleton gurantee
        if Manager.singleton is not None:
            raise Exception('Manager is a singleton class. Second instance is not allowed.')
        Manager.singleton = self

    def load_data(self, path: str) -> None:
        '''
        Load data from the given path.
        '''
        
        with open(path, 'r') as file:
            original_data = json.load(file)
            
        self.__load_teachers(original_data['teachers'])
        self.__load_students(original_data['students'])
        self.__load_teachings(original_data['teachings'])
        
    def find_teacher(self, id: int) -> Teacher:
        '''
        Find teacher instance from id
        '''
        
        for teacher in self.teachers:
            if teacher.id == id:
                return teacher
            
    def find_student(self, id: int) -> Student:
        '''
        Find student instance from id
        '''
        
        for student in self.students:
            if student.id == id:
                return student
            
    def show_users_list(self) -> str:
        '''
        Returns users name list
        '''
        
        users = self.get_users_list()
            
        #sort by id
        users.sort(key = lambda user: user.id)
        
        #make text
        #"id: name"
        output = ""
        for user in users:
            output += f'{user.id}: {user.name}\n'
        
        return output
    
    def show_user_detail(self, id: int) -> str:
        '''
        show details of the given user
        '''
        
        for user in self.get_users_list():
            if user.id == id:
                return user.show_details()
            
    def get_users_list(self) -> List[User]:
        '''
        Get list of all users
        '''
        
        users = []
        
        for teacher in self.teachers:
            users.append(teacher)
            
        for student in self.students:
            users.append(student)
            
        return users
    
    def calculate_income(self) -> int:
        '''
        Returns the amount of the managing company
        '''
        
        income = 0
        for user in self.get_users_list():
            income += user.calculate_money()
            
        return income
            
    def find_student_with_relashionship(self, relashionship: TeachingRelationship) -> Student:
        '''
        Find student instance from the given relashionship
        '''
        
        for student in self.students:
            if student.has_teaching_relationship(relashionship):
                return student
            
    def find_teacher_with_relashionship(self, relashionship: TeachingRelationship) -> Teacher:
        '''
        Find teacher instance from the given relashionship
        '''
        
        for teacher in self.teachers:
            if teacher.has_teaching_relationship(relashionship):
                return teacher
            
    def __load_teachers(self, teachers_data: list) -> None:
        '''
        Load teachers from the given list.
        '''
        
        for teacher_data in teachers_data:
            self.teachers.append(Teacher(teacher_data['id'], teacher_data['name'], teacher_data['salary_rate']))
            
    def __load_students(self, students_data: list) -> None:
        '''
        Load students from the given list.
        '''
        
        for student_data in students_data:
            self.students.append(Student(student_data['id'], student_data['name'], student_data['address']))
            
    def __load_teachings(self, teachings_data: list) -> None:
        '''
        Load teachers-students teachings from the given list.
        '''
        
        for teaching_data in teachings_data:            
            #register relashionship
            relashionship = TeachingRelationship(teaching_data['day'], teaching_data['tuition'])
            
            #let students and teachers know about the relashionship
            student = self.find_student(teaching_data['student_id'])
            teacher = self.find_teacher(teaching_data['teacher_id'])
            
            student.register_teaching_relashionship_day(teaching_data['day'], relashionship)
            teacher.register_teaching_relashionship_day(teaching_data['day'], relashionship)