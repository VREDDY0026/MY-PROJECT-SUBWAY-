from tkinter import *  #importing tinker
#from . import order  #importing order.py file


root = Tk()
#used GIF image, because PhotoImage() takes only .gif files. also specified the height width of image 
text1 = Text(root, height=10, width=50)
#photo=PhotoImage(file='./1.gif',height=90000, width=400)

#text1.image_create(END, image=photo)

#text1.pack(side=TOP) #pack is used to place image on top

#here i have defined the area for the menu and some style of my text eg. item names
text2 = Text(root, height=38, width=50)

text2.tag_configure('bold_italics', font=('Aharoni', 14, 'bold', 'italic'))
text2.tag_configure('big', font=('Times New Roman', 16, 'bold'))
text2.tag_configure('color', foreground='#476042', 
                        font=('Tempus Sans ITC', 18, 'bold'))

text2.insert(END,'\n\tWelocme To SUBWAY', 'big')
text2.insert(END,'\n\t\tMENU\n','big')
quote = """
SUBS(COST):       

ITALIAN BMT($6.99)    
PIZZA SUB($7.59)                 
                 
MAIN COURSE(COST)  :

CHICKEN TERIYAKI($12.45)          
OVEN ROASTED CHICKEN($11.54)          
TUNA SUB($7.5)         
EGG SANDWICH($10)       

DESERTS(COST)  :
   
ICE-CREAM($4.5)
PASTRIES($5)     

DRINKS(COST)  :

POPS($2.5)
CHOCOLATE MILK($4.5)
"""
text2.insert(END, quote, 'color')

text2.pack()
button1 = Button(root,height=1, width=40) #creating button()
button1["text"] = "      ORDER     "  #button name
button1["command"] = order.ord #button will refer to ord function defined in order.py
button1.pack(side=BOTTOM) #button is packed at bottom

root.mainloop() #this will keep application running (like infinite loop)
