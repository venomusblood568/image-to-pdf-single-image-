from PIL import Image
#PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities
import tkinter as tk
#Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk. 
from tkinter import ANCHOR, filedialog
#File dialogs help you open, save files or directories.
#Anchors are used to define where text is positioned relative to a reference point
from tkinter import messagebox
#MessageBox Widget is used to display the message boxes in the python applications. 

root= tk.Tk()#main loop 
root.title('image to pdf converter') #title name of canvas
root.iconbitmap('/path/to/ico/icon.ico') #logo

# this is canvas description 
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'black', relief = 'groove')
canvas1.pack()

#this is for button1 
#root,text,background,forground,anchor,font
#size of the button 
label1 = tk.Label(root, text='File Conversion Tool', bg = 'black',fg ="green",anchor='center')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)
#function of button 1 
# it will ask to select the file and after selction it will open the file and finally convert the RGB
def getFile ():
    global im1
    import_file_path = filedialog.askopenfilename()
    image1 = Image.open(import_file_path)

    
    im1 = image1.convert('RGB')

browseButton = tk.Button(text="           Select File             ", command=getFile, bg='green', fg='magenta', font=('helvetica', 28, 'bold'),anchor='center')
canvas1.create_window(150, 130, window=browseButton)



# button 2 
# here it will ask you to select a name for the file which will be saved in pdf 
def convertToPdf ():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    
    
    im1.save(export_file_path)
#here we are defining the botton 2 size name and background ,forground and text and my more 
saveAsButton = tk.Button(text='      Convert to PDF         ', command=convertToPdf, bg='magenta', fg='red', font=('helvetica', 28, 'bold'),anchor='center')
canvas1.create_window(150, 180, window=saveAsButton)


#here is the button 3
#here we are saying that for exit button and how it works 
def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application','glad i helped you master!!! and are you sure you want to leave',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()
#here we are defining the botton 3 size name and background ,forground and text and my more 
    
exitButton = tk.Button (root, text='        Exit Application         ',command=exitApplication, bg='brown', fg='magenta', font=('helvetica', 28, 'bold'),anchor='center')
canvas1.create_window(150, 230, window=exitButton)
#exit of main loop and here program will end 
root.mainloop()