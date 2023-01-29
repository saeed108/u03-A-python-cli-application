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
    
    
    def test_edit(self):
        
        
        guestbook_test.main.edit_note(3 , "first note is edited!")
        self.assertEqual(guestbook_test.main.notes[2].text , "first note is edited!")
        self.assertEqual(guestbook_test.main.edit_note(4 , "test") , False)
    
    def test_delete(self):
        
        self.assertEqual(len(guestbook_test.main.notes) , 3)
        self.assertEqual(guestbook_test.main.delete_note(4) , False)
    

    def  test_save(self):
        guestbook_test.main.save()
        
        f=open("notes.txt" , "r")
        output=f.read()
        expected='1 , this is my newest note , {}'.format(guestbook_test.main.notes[0].date )+"\n2 , this is my second test note , {}".format(guestbook_test.main.notes[1].date )+"\n3 , first note is edited! , {} , edited".format(guestbook_test.main.notes[2].date )
        self.assertEqual(output , expected)
        f.close()
        os.remove("notes.txt")