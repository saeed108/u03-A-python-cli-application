import unittest
from guestbook import *
import os

class guestbook_test(unittest.TestCase):
    main=Main()
    main.add_note("this is my first test note")
    main.add_note("this note will be deleted")
    main.add_note("this is my second test note")
    main.add_note("this is my newest note")
    main.delete_note(3)

    #test new note
    def test_new(self):

        self.assertEqual(guestbook_test.main.notes[0].text , "this is my newest note")
        self.assertEqual(guestbook_test.main.notes[1].id , 2)
    
