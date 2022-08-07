# Rock Paper Scissor Game

from tkinter import *
from tkinter.messagebox import *
from random import randrange

root = Tk()
root.title("Rock Paper Scissor")
root.geometry("500x500+400+100")

def choose_the_winner(num):
	if num == 1:
		user = 'rock'
	elif num == 2:
		user = 'paper'
	else:
		user = 'scissor'

	choices = ['rock', 'paper', 'scissor']
	comp = choices[randrange(len(choices))]
	print(user, comp)
	if comp == user:
		msg = "its a tie"
	elif comp=='rock' and user=='scissor':
		msg = "comp wins"
	elif comp=='paper' and user=='rock':
		msg = "comp wins"	
	elif comp=='scissor' and user=='paper':
		msg = "comp wins"
	elif user=='rock' and comp=='scissor':
		msg = "user wins"
	elif user=='paper' and comp=='rock':
		msg = "user wins"	
	elif user=='scissor' and comp=='paper':
		msg = "user wins"

	final_msg = "user selected --> " + user + " and computer selected --> " + comp + " \nresult is " + msg
	showinfo("Result", final_msg)




f = ('Calibri', 20, 'bold')
btn_rock = Button(root, text="Rock", font=f, width=10, command=lambda:choose_the_winner(1))
btn_paper = Button(root, text="Paper", font=f, width=10, command=lambda:choose_the_winner(2))
btn_scissor = Button(root, text="Scissor", font=f, width=10, command=lambda:choose_the_winner(3))

btn_rock.pack(pady=10)
btn_paper.pack(pady=10)
btn_scissor.pack(pady=10)



root.mainloop()



