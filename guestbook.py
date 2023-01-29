from datetime import datetime
import os
import json
import sys
class note:
    def __init__(self, text) :
        self.id=0
        self.text=text
        self.date=datetime.now().date()
        self.edited=False
    
    def __str__(self):
        pass

class Main:
    def __init__(self) :
        self.notes=[]
    
    def add_note(self, text):
       pass

        
    

    def edit_note(self, id , text):
        pass
    
    def view_note(self):
       pass

    def delete_note(self , id):
        pass
    
    def save(self):
        pass
    


    def load(self):
       pass
    
    def export(self):
        pass