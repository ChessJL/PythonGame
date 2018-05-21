# Question 4

from tkinter import*
from tkinter import messagebox
import random

"""

This Game has two different modes, which are 'easy' and 'hard'. 
The rule of the game is type the words that show up when you press the 'start' button.
If you type a correct word, you will get point, and the word will be changed.
Each player has 30 seconds to challenge. The top 3 highest scores will be recorded.

Steps:
1. choose 'easy' or 'hard'
2. press 'start', try to type as fast as possible
3. Try again or Save your score if you are better than the previous player


"""

# For reading data
class readfile():

    def read_data(self):

        f = open('easy.txt', 'r')
        text_easy = f.read()
        f.close()
        self.te_split = text_easy.split()
        self.te_len = len(self.te_split)

        f = open('hard.txt', 'r')
        text_hard = f.read()
        f.close()
        self.th_split = text_hard.split()
        self.th_len = len(self.th_split)

    def read_record(self):
        f = open('record.txt','r')
        text_record = f.read()
        f.close()
        self.tr_split= text_record.split()

# Main game frame
class Speedtype(readfile):

    settime=30
    _score= 0
    _stage= 0
    _level= 0
    _position= -1

    def __init__(self):
        #read data from txt file
        self.read_data()
        self.read_record()
        #main game window
        self.root=Tk()
        self.root.title('SpeedWord')
        self.root.geometry('400x500')
        #Title
        Label(self.root, text='Welcome to SpeedTyping', font=('',30)).place(anchor='center', x=200, y=100, height=45)
        Label(self.root, text='Please choose level', font=('',20)).place(anchor='center', x=200, y=150, height=45)
        #Button for functions of game
        Button(self.root, font=('', 25), text='Easy', command=self.Easy).place(anchor='center', x=200, y=250, width=150)
        Button(self.root, font=('', 25), text='Hard', command=self.Hard).place(anchor='center', x=200, y=300, width=150)
        Button(self.root, font=('', 25), text='Show Score', command=self.Showscore).place(anchor='center', x=200, y=350)
        Button(self.root, font=('', 25), text='Exit', command=self.root.destroy).place(anchor='center', x=200, y=400)
        self.root.mainloop()

    def Showscore(self):

        self.root_score=Tk()
        self.root_score.title('Scores')
        self.root_score.geometry('300x300')

        name_e1=StringVar()
        name_e2=StringVar()
        name_e3=StringVar()
        name_h1=StringVar()
        name_h2=StringVar()
        name_h3=StringVar()

        #set the variable from the data it reads
        name_e1 = self.tr_split[0]
        name_e2 = self.tr_split[2]
        name_e3 = self.tr_split[4]
        name_h1 = self.tr_split[6]
        name_h2 = self.tr_split[8]
        name_h3 = self.tr_split[10]

        score_e1=IntVar()
        score_e2=IntVar()
        score_e3=IntVar()
        score_h1=IntVar()
        score_h2=IntVar()
        score_h3=IntVar()

        #set the variable from the data it reads
        score_e1= int(self.tr_split[1])
        score_e2= int(self.tr_split[3])
        score_e3= int(self.tr_split[5])
        score_h1= int(self.tr_split[7])
        score_h2= int(self.tr_split[9])
        score_h3= int(self.tr_split[11])

        frame1 = Frame(self.root_score, bg='green')
        frame2 = Frame(self.root_score)
        frame3 = Frame(self.root_score, bg='green')
        frame4 = Frame(self.root_score)
        frame5 = Frame(self.root_score)

        frame1.pack(side=TOP, fill=X)
        frame2.pack(side=TOP)
        frame3.pack(side=TOP, fill=X)
        frame4.pack(side=TOP)
        frame5.pack(side=TOP)

        #Layout

        Label(frame1, text='  EASY', bg='green',font=('',30)).pack(side=LEFT)

        Label(frame2, text='No.1',font=('',20)).grid(row=0,column=0)
        Label(frame2, text='No.2',font=('',20)).grid(row=1,column=0)
        Label(frame2, text='No.3',font=('',20)).grid(row=2,column=0)
        Label(frame2, text=name_e1,font=('',20),fg='gold4').grid(row=0,column=1)
        Label(frame2, text=name_e2,font=('',20),fg='lightYellow4').grid(row=1,column=1)
        Label(frame2, text=name_e3,font=('',20),fg='orange red').grid(row=2,column=1)
        Label(frame2, text=score_e1,font=('',20),fg='gold4').grid(row=0,column=2)
        Label(frame2, text=score_e2,font=('',20),fg='lightYellow4').grid(row=1,column=2)
        Label(frame2, text=score_e3,font=('',20),fg='orange red').grid(row=2,column=2)

        Label(frame3, text='  HARD', bg='green', font=('', 30)).pack(side=LEFT)

        Label(frame4, text='No.1', font=('', 20)).grid(row=0, column=0)
        Label(frame4, text='No.2', font=('', 20)).grid(row=1, column=0)
        Label(frame4, text='No.3', font=('', 20)).grid(row=2, column=0)
        Label(frame4, text=name_h1,font=('',20),fg='gold4').grid(row=0,column=1)
        Label(frame4, text=name_h2,font=('',20),fg='lightYellow4').grid(row=1,column=1)
        Label(frame4, text=name_h3,font=('',20),fg='orange red').grid(row=2,column=1)
        Label(frame4, text=score_h1,font=('',20),fg='gold4').grid(row=0,column=2)
        Label(frame4, text=score_h2,font=('',20),fg='lightYellow4').grid(row=1,column=2)
        Label(frame4, text=score_h3,font=('',20),fg='orange red').grid(row=2,column=2)
        Button(frame5, text='Reset Score', command=self.resetscore).pack(side=TOP)

        self.root_score.mainloop()

    def resetscore(self):
        # reset scores
        ans=messagebox.askyesno(title='Reset', message='Do you want to reset the scores?')
        if ans == True:
            # write the default score data to the txt file
            # From left to right is (easy)No1 No2 No3 (hard)No1 No2 No3
            reset='none 0 none 0 none 0 none 0 none 0 none 0'
            f = open('record.txt', 'w')
            f.write(reset)
            f.close()
            #when score has been reset, re-read the data from txtfile
            self.read_record()
            self.root_score.destroy()
            #show new score
            self.Showscore()
        else:
            pass

    def saferecord(self):
        #Checking the name, if there is any space, it will stop and try again.
        for check in self.name.get():
            if check == ' ':
                messagebox.showerror(title='Error', message='No space available')
                break
        #If there is not space in the name, the name will be insert to the correct location in the list.
        #And pop the name which is extra.
        else:
            temstr=''
            name=self.name.get()
            self.root_record.destroy()
            temlist=self.tr_split
            if self._level == 1 :
                temlist.insert(self._position-1,name)
                temlist.insert(self._position, self.score_easy.get())
                temlist.pop(7)
                temlist.pop(6)
                for c in temlist:
                    temstr += str(c) + ' '
                f=open('record.txt','w')
                f.write(temstr)
                f.close()
            elif self._level == 3 :
                temlist.insert(self._position - 1, name)
                temlist.insert(self._position, self.score_hard.get())
                temlist.pop(13)
                temlist.pop(12)
                for c in temlist:
                    temstr += str(c) + ' '
                f = open('record.txt', 'w')
                f.write(temstr)
                f.close()
            self.read_record()
            self.Showscore()

    def Newrecord(self):

        self.root_record=Tk()
        self.root_record.title('Congradualation')
        self.root_record.geometry('350x230')
        self.namevar=StringVar()
        Label(self.root_record, text='New Record', bg='Gold', font=('',50)).place(anchor='center', x=175,y=50)
        Label(self.root_record, text='Name:', font=('',35)).place(anchor='e', x=135,y=120)
        self.name=Entry(self.root_record, textvariable=self.namevar, font=('',30))
        self.name.bind('<Return>', lambda event: self.saferecord())
        self.name.place(anchor='w', x=145,y=124, width=180, height=40)
        Button(self.root_record, text='OK', command=self.saferecord).place(anchor='center', x=135,y=180)
        Button(self.root_record, text='Cancle', command=self.root_record.destroy).place(anchor='center', x=215,y=180)

        self.root_record.mainloop()

    def Easy(self):
        #Game time
        self.sec = self.settime
        #The first question from read data, and pick up a random one.
        self.tem = self.te_split[random.randint(0, self.te_len - 1)]
        self._score=0
        self._stage=0

        root_easy = Tk()
        #set the global number to 1
        self._level = 1
        self.stage_easy = IntVar(root_easy)
        self.score_easy = IntVar(root_easy)
        self.question_easy = StringVar(root_easy)


        sec_easy=IntVar(root_easy)
        sec_easy.set(self.sec)

        #when press start the timer will star to count.
        #if timer
        def timer():

            self.b_start_easy.configure(state='disable')
            self.enter_easy.bind('<Return>', lambda event: self.Enter())
            self.button_easy.configure(state='normal')
            self.question_easy.set(self.tem)

            if self.sec > 0:
                self.sec -= 1
                sec_easy.set(self.sec)
                self.time_easy.after(1000, timer)

            #When times up, check the score, if it is higher then data, it will ask player to safe score or not.
            else:
                if self.score_easy.get() > int(self.tr_split[1]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position=1
                        root_easy.destroy()
                        self.Newrecord()
                    else:
                        root_easy.destroy()

                elif self.score_easy.get() > int(self.tr_split[3]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position = 3
                        root_easy.destroy()
                        self.Newrecord()
                    else:
                        root_easy.destroy()

                elif self.score_easy.get() > int(self.tr_split[5]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position = 5
                        root_easy.destroy()
                        self.Newrecord()
                    else:
                        root_easy.destroy()

                else:
                    messagebox.showinfo(title='Game Over', message='Try Again!!')
                    root_easy.destroy()




        root_easy.title('SpeedWord')
        root_easy.geometry('800x600')

        Label(root_easy, text='EASY', font=('', 50)).place(anchor='center', x=400, y=30)
        self.time_easy = Label(root_easy, text='Timer', textvariable=sec_easy, font=('', 35))
        self.time_easy.place(anchor='center', x=400, y=100)
        Label(root_easy, bg='yellow', textvariable=self.question_easy, font=('',50)).place(anchor='n', x=400, y=200, width=500, height=80)
        Label(root_easy, text='Score', font=('',25)).place(anchor='e', x=150, y=130, width=100, height=40)
        Label(root_easy, textvariable=self.score_easy, font=('',25)).place(anchor='w', x=160, y=130)
        Label(root_easy, text='Stage', font=('', 25)).place(anchor='e', x=640, y=130, width=100, height=40)
        Label(root_easy, textvariable=self.stage_easy, font=('', 25)).place(anchor='w',x=650,y=130, width=40, height=40)
        self.enter_easy=Entry(root_easy, font=('',40), insertwidth=2)
        self.enter_easy.place(anchor='center', x=400, y=350, width=250, height=100)
        self.button_easy=Button(root_easy, font=('',25), text='Enter', command=self.Enter)
        self.button_easy.configure(state='disable')
        self.button_easy.place(anchor='center', x=400, y=430, width=150)
        self.b_start_easy=Button(root_easy, font=('',25), text='Start', command=timer)
        self.b_start_easy.place(anchor='center', x=400, y=480, width=150)
        root_easy.mainloop()

    def Hard(self):
        self.sec = self.settime
        self.tem = self.th_split[random.randint(0, self.th_len - 1)]
        self._score = 0
        self._stage = 0

        root_hard = Tk()
        self._level = 3
        self.stage_hard = IntVar(root_hard)
        self.score_hard = IntVar(root_hard)
        self.question_hard = StringVar(root_hard)


        sec_hard = IntVar(root_hard)
        sec_hard.set(self.sec)

        def timer():

            self.b_start_hard.configure(state='disable')
            self.enter_hard.bind('<Return>', lambda event: self.Enter())
            self.button_hard.configure(state='normal')
            self.question_hard.set(self.tem)

            if self.sec > 0:
                self.sec -= 1
                sec_hard.set(self.sec)
                self.time_hard.after(1000, timer)
            else:
                if self.score_hard.get() > int(self.tr_split[7]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position = 7
                        root_hard.destroy()
                        self.Newrecord()
                    else:
                        root_hard.destroy()
                elif self.score_hard.get() > int(self.tr_split[9]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position = 9
                        root_hard.destroy()
                        self.Newrecord()
                    else:
                        root_hard.destroy()
                elif self.score_hard.get() > int(self.tr_split[11]):
                    ans=messagebox.askyesno(title='Congradualation', message='New Record!!Do you want to record your score?')
                    if ans == True:
                        self._position = 11
                        root_hard.destroy()
                        self.Newrecord()
                    else:
                        root_hard.destroy()
                else:
                    messagebox.showinfo(title='Game Over', message='Try Again!!')
                    root_hard.destroy()

        root_hard.title('SpeedWord')
        root_hard.geometry('800x600')
        Label(root_hard, text='Hard', font=('', 50)).place(anchor='center', x=400, y=50)  # Score
        self.time_hard = Label(root_hard, text='Timer', textvariable=sec_hard, font=('', 35))  # Time
        self.time_hard.place(anchor='center', x=400, y=100)  # Time
        Label(root_hard, bg='yellow', textvariable=self.question_hard, font=('',50)).place(anchor='n', x=400, y=200, width=500, height=80)  # Question
        Label(root_hard, text='Score', font=('', 25)).place(anchor='e', x=150, y=130, width=100, height=40)  # Score
        Label(root_hard, textvariable=self.score_hard, font=('', 25)).place(anchor='w', x=160, y=130,height=40)  # Score
        Label(root_hard, text='Stage', font=('', 25)).place(anchor='e', x=640, y=130, width=100, height=40)  # Stage
        Label(root_hard, textvariable=self.stage_hard, font=('', 25)).place(anchor='w', x=650, y=130,height=40)  # Stage
        self.enter_hard=Entry(root_hard, font=('',40))
        self.enter_hard.place(anchor='center', x=400, y=350, width=250, height=100)
        self.button_hard=Button(root_hard, font=('',25), text='Enter', command=self.Enter)
        self.button_hard.configure(state='disable')
        self.button_hard.place(anchor='center', x=400, y=430, width=150)
        self.b_start_hard=Button(root_hard, font=('',25), text='Start', command=timer)
        self.b_start_hard.place(anchor='center', x=400, y=480, width=150)


        root_hard.mainloop()

    def Enter(self):
        #when chose easy or hard, the number of level will be set different numbers, and than do different jobs.
        if self._level == 1:
            #if input the correct word, score will plus 10, and stage will plus 1.
            if self.question_easy.get() == self.enter_easy.get():
                self._score += 10
                self._stage += 1
                self.score_easy.set(self._score)
                self.stage_easy.set(self._stage)
                self.tem = self.te_split[random.randint(0, self.te_len - 1)]
                self.question_easy.set(self.tem)
            self.enter_easy.delete(0, 'end')


        elif self._level == 3:
            if self.question_hard.get() == self.enter_hard.get():
                self._score += 30
                self._stage += 1
                self.score_hard.set(self._score)
                self.stage_hard.set(self._stage)
                self.tem = self.th_split[random.randint(0, self.th_len - 1)]
                self.question_hard.set(self.tem)
            self.enter_hard.delete(0, 'end')


game=Speedtype()

