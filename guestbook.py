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
