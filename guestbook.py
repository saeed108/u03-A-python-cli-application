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
        if self.edited:
            return "{}".format(self.id)+"{}".format(self.text).center(80)+"{}".format(self.date).center(10)+"edited".center(10)
        else:

    
           return "{}".format(self.id)+"{}".format(self.text).center(80)+"{}".format(self.date).center(10)


class Main:
    def __init__(self) :
        self.notes=[]
    
    def add_note(self, text):
        n=note(text)
        self.notes.insert(0, n)

        for i in range(1 , len(self.notes)+1):
            n=self.notes[i-1]
            n.id=i
    

    def edit_note(self, id , text):
        if id<=len(self.notes):
           n=self.notes[id-1]
           n.text=text
           n.edited=True
           return True
        
        else:
            return False
    
    def view_note(self):
        display_list=[]
        line_0="id"+"note".center(80)+'date'.center(10)
        display_list.append(line_0)
        display_list.append("-"*len(line_0))
        for n in self.notes:
            t=str(n)
            display_list.append(t)
        
        display_text="\n".join(display_list)


            
        
        return display_text
    

    def delete_note(self , id):
        if id<=len(self.notes):
            self.notes.pop(id-1)
            for i in range(1 , len(self.notes)+1):
                n=self.notes[i-1]
                n.id=i
            return True
        
        else:
            return False
    
    def save(self):
        f=open("notes.txt", "w")
        f_list=[]
        for n in self.notes:
            line_list=[]

            
            for k , v in vars(n).items():
                if k!='edited':
                
                  line_list.append(str(v))
                
                else:
                    if v==True:
                        line_list.append("edited")
            
            line=" , ".join(line_list)
            
            f_list.append(line)
        
        f_text="\n".join(f_list)
        f.write(f_text)
    


    def load(self):
        if os.path.exists("notes.txt"):
            f=open("notes.txt" , "r")
            txt=f.read()
            lines=txt.split("\n")
            for line in lines:
                items=line.split(" , ")
                id=int(items[0])
                date=datetime.strptime(items[2] , "%Y-%m-%d")
                date=date.date()
                n=note(items[1])
                n.id=id
                n.date=date

                if len(items)==4:
                    n.edited=True
                
                self.notes.append(n)
    
    def export(self):
        note_dict={}
        for n in self.notes:
            note_name="note"+str(n.id)
            dict_1={}
            for k , v in vars(n).items():
                if k!="date":
                    dict_1[k]=v
                
                else: 
                    dict_1[k]=str(v)
            
            note_dict[note_name]=dict_1

        
        out_file=open("notebook.json" , "w")
        json.dump(note_dict , out_file  , indent=4)
        print(json.dumps(note_dict , indent=4))



main=Main()
main.load()

if len(sys.argv)==2:
    if sys.argv[1]=="list":
        result=main.view_note()
        print(result)
    
    elif sys.argv[1]=="export":
        main.export()
    
    else:
        print("wrong command! Try again")

elif len(sys.argv)==3:
    if sys.argv[1]=="new":
        main.add_note(sys.argv[2])
        main.save()
        print("not is added to notebook!")
    

    elif sys.argv[1]=="delete" and sys.argv[2].isdigit():
         check=main.delete_note(int(sys.argv[2]))
         if check:
            print("note{} is deleted".format(sys.argv[2]))
            main.save()
        
         else:
            print("note{} not found is notebook".format(sys.argv[2]))
    
    else:
        print("wrong command! Try again")

elif len(sys.argv)==4:
    if sys.argv[1]=="edit" and sys.argv[2].isdigit():
        check=main.edit_note(int(sys.argv[2]) , sys.argv[3])
        if check:

           print("note{} is edited!".format(sys.argv[2]))
           main.save()
        
        else:
            print("note{} not found in notebook!".format(sys.argv[2]))
    
    else:
        print("wrong command!Try again")

else:
    print("wrong command!Try again")         