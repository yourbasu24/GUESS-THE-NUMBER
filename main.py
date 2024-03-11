import threading
import pyttsx3
import time
import random
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

# Initialize attempt count and score
atemptaken = 0
score = 0

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def col():
    colour=["red","green","white","cyan","purple","pink","blue","yellow","violet","orange","grey","magenta","aquamarine","beige","brown","chocolate","gold","indigo","lavender","olive","peru","silver","teal","wheat","turquoise"]
    sel=random.choice(colour)
    root.configure(bg=sel)

def hint():
    c=0
    l=[f"The Number Between {generated-10} To {generated+10}"]
    if generated%2==0:
        l.append("Number Is Even")
    if generated%2!=0:
        l.append("Number Is Odd")
    if generated%5 ==0:
        l.append("Number Is Divisible By 5")
    if str(generated) == str(generated)[::-1]:
        l.append("The Number Is Palindrome")
    for i in range(2,generated):
        if generated%i==0:
            c+=1
    if c==0:
        l.append("prime number")
    if c!=0:
        l.append("not a prime number")
    hintr=random.choice(l)
    messagebox.showinfo("hint", hintr)

def choose_difficulty():
    def startgame(range, attempt, max_score):
        def result(userno, attempt, max_score):
            global atemptaken
            global score
            atemptaken += 1  # Increment attempt count
            guess = int(userno.get())
            print(f"User's guess: {guess}")
            if guess == generated:
                rangelabel.destroy()
                userno.destroy()
                submit.destroy()
                hintb.destroy()
                calculate_score(max_score)
                cong = Label(root, text=f'''🥳🥳🥳Congratulations {player_name},\n You Won The Game 🥳🥳🥳 \n Your Score: {score}''', font=("times new roman", 24, "bold"), bg="black",fg="white", padx=10, pady=10)
                cong.pack(pady=20)
                threading.Thread(target=speak, args=(f"Congratulations {player_name}, You Won The Game 🥳🥳🥳 \n Your Score: {score}",)).start()
            elif atemptaken >= attempt:
                rangelabel.destroy()
                userno.destroy()
                submit.destroy()
                hintb.destroy()
                calculate_score(max_score, out_of_attempts=True)
                sorry = Label(root, text=f'''😭😭😭you lose {player_name},\n You have exhausted all the attempts \n Your Score: {score} \n Better luck next time 👍🏻👍🏻👍🏻''', font=("times new roman", 24, "bold"), bg="black",fg="white", padx=10, pady=10)
                sorry.pack(pady=20)
                threading.Thread(target=speak, args=(f"you lose {player_name},\n You have exhausted all the attempts \n Your Score: {score} \n Better luck next time",)).start()
            else:
                if guess < generated:
                    if guess< generated-10:
                        temp=Label(root,text="Too low! Guess higher",font=("verdana",12),bg="black",fg="white",padx=20,pady=20)
                        temp.pack(padx=10,pady=10)
                        threading.Thread(target=speak,args=("Too low! Guess higher.",)).start()
                        temp.destroy()
                    else:
                        temp=Label(root,text="so close!! Guess higher",font=("verdana",12),bg="black",fg="white",padx=20,pady=20)
                        temp.pack(padx=10,pady=10)
                        threading.Thread(target=speak,args=("so close!! guess higher",)).start()
                        temp.destroy()
                else:
                    if guess>generated+10:
                        temp=Label(root,text="Too high! Guess lower",font=("verdana",12),bg="black",fg="white",padx=20,pady=20)
                        temp.pack(padx=10,pady=10)
                        threading.Thread(target=speak,args=("Too high! Guess lower.",)).start()
                        temp.destroy()
                    else:
                        temp=Label(root,text="so close!! Guess lower",font=("verdana",12),bg="black",fg="white",padx=20,pady=20)
                        temp.pack(padx=10,pady=10)
                        threading.Thread(target=speak,args=("so close!! guess lower",)).start()
                        temp.destroy()
                userno.delete(0, 'end')
                print(atemptaken)

        global atemptaken
        global score
        atemptaken = 0  # Reset attempt count for new game
        score = 0  # Reset score for new game
        speak(f"okay {player_name}, let's start the game")
        diflabel.destroy()
        button_frame.destroy()
        l = [1, 10, 20, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
        global lower
        lower = random.choice(l)
        global generated
        generated = random.randint(lower, lower + range)
        print(generated)
        rangelabel = Label(root, text=f"guess the number between {lower}to{lower+range}", font=("times now roman", 20, "bold"), bg="black", fg="white", padx=20, pady=20, relief=GROOVE)
        rangelabel.pack(padx=20, pady=20, side=TOP)
        userno = Entry(root, font=("times new roman", 14), justify="center")
        userno.pack(pady=10)
        submit = Button(root, text="Submit", font=("helvetica", 14, "bold"), bg="black", fg="white", command=lambda: result(userno, attempt, max_score), padx=10, pady=10)
        submit.pack(pady=20)
        hintb=Button(root, text="hint", font=("helvetica", 14, "bold"), bg="black", fg="white", command=hint, padx=10, pady=10)
        hintb.pack(pady=20)

    def calculate_score(max_score, out_of_attempts=False):
        global score
        if out_of_attempts:
            score = 0
        elif atemptaken <= 3:
            score = max_score
        elif atemptaken <= 5:
            score = int(max_score * 0.8)
        else:
            score = int(max_score * 0.5)

    name_label.destroy()
    global player_name
    player_name = name_input.get()
    name_input.destroy()
    next.destroy()
    diflabel = Label(root, text="CHOOSE DIFFICULTY ", font=("times now roman", 20, "bold"), bg="black", fg="white", padx=20, pady=20, relief=GROOVE)
    diflabel.pack(padx=20, pady=20, side=TOP)

    button_frame = Frame(root, bg="black")
    button_frame.pack(pady=20)

    easy_button = Button(button_frame, text="EASY", font=("times now roman ", 13), bg="black", fg="white", command=lambda: startgame(50, 5, 100), padx=10, pady=10, relief="groove")
    easy_button.pack(side=RIGHT, padx=20, pady=10)

    medium_button = Button(button_frame, text="MEDIUM", font=("times new roman", 13), bg="black", fg="white", command=lambda: startgame(100, 8, 150), padx=10, pady=10, relief="groove")
    medium_button.pack(side=RIGHT, padx=20, pady=10)

    hard_button = Button(button_frame, text="HARD", font=("times new roman", 13), bg="black", fg="white", command=lambda: startgame(500, 12, 200), padx=10, pady=10, relief="groove")
    hard_button.pack(side=RIGHT, padx=20, pady=10)

root = Tk()
root.title("Number Guessing Game ")
root.geometry("850x750")
root.configure(bg="black")
image = Image.open("C:/Users/basud/Documents/python folder/number guessing game/image.jpg")
image = image.resize((200, 200),)
photo = ImageTk.PhotoImage(image)
logo = Label(image=photo, bg="black")
logo.pack(padx=25, pady=25)
quotes = Label(root, text="Guess The Digit, Catch The Thrill,\n Master The Number, If You Will! ", font=("verdana", 20, "bold"), bg="black", fg="white", padx=10, pady=10)
quotes.pack()
threading.Thread(target=speak, args=("Guess The Digit, Catch The Thrill,\n Master The Number, If You Will! ",)).start()
name_label = Label(root, text='Enter Name', fg='white', bg='black')
name_label.pack(pady=(20, 5))
name_label.config(font=('verdana', 14))
name_input = Entry(root, width=50,justify="center")
name_input.pack(ipady=6)
next = Button(text="submit", command=choose_difficulty, font=("verdana", 14), bg="black", fg="white", padx=10, pady=10)
next.pack(pady=20)
changcol = Button(text="change background", command=col, font=("verdana", 14), bg="black", fg="white", padx=10, pady=10)
changcol.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)
root.mainloop()