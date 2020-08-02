import time
import pyperclip
from nltk.corpus import wordnet
import tkinter as tk
from tkinter import ttk
import re

def popupmsg(msg):
	root = tk.Tk()
	label = ttk.Label(root, text=msg)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(root, text="OK", command = root.destroy)
	B1.pack()
	root.mainloop()


old_word = ""
while(True):
    time.sleep(2)
    new_word=pyperclip.paste()
    

    if(new_word!=old_word):
    	print(new_word)
    	time.sleep(2)

    	define = wordnet.synsets(new_word)
    	#print(define)
    	#time.sleep(2)

    	counter=1
    	definitions='Meaning of word - '+new_word+'\n\n'
    	for i in define:
    		message = str(counter)+'. '+i.definition()+'\n'
    		definitions = definitions+'\n'+message
    		print(str(counter)+'. '+i.definition()+'\n')
    		counter=counter+1

    	synonyms=[]
    	for i in define:
    		for j in i.lemmas():
    			synonyms=synonyms+[j.name()]
    	synonyms=set(synonyms)


    	display = definitions+'\n\nSynonyms: '+','.join(synonyms)
    	popupmsg(display)

    	old_word=pyperclip.paste()
