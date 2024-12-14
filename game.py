from tkinter import *
import time
import random

root = Tk()
root.title("Bounce")
root.geometry("500x570")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
score = Label(height=50, width=80, text="Score: 00", font="Consolas 14 bold")
score.pack(side="left")
root.update()

player_name = "Player"
playing = False
level = 1

def ask_name():
    global player_name

    def save_name():
        nonlocal name_entry, error_label
        entered_name = name_entry.get().strip()
        if entered_name:
            global player_name
            player_name = entered_name
            name_window.destroy()
            show_menu()
        else:
            error_label.config(text="Name cannot be empty!", fg="red")

    name_window = Toplevel(root)
    name_window.title("Enter Name")
    name_window.geometry("300x150")
    name_window.transient(root)
    name_window.grab_set()

    Label(name_window, text="Enter your name:", font="Consolas 14").pack(pady=10)
    name_entry = Entry(name_window, font="Consolas 14")
    name_entry.pack(pady=5)
    error_label = Label(name_window, text="", font="Consolas 12")
    error_label.pack()
    Button(name_window, text="Submit", command=save_name, font="Consolas 12").pack(pady=10)

ask_name()

class Ball:
    def __init__(self, canvas, color, paddle, bricks, score, speed_factor, obstructions):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.obstructions = obstructions
        self.bottom_hit = False
        self.hit = 0
        self.speed_factor = speed_factor
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
        self.canvas.move(self.id, 230, 461)
        start = [4 * speed_factor, 3.8 * speed_factor, 3.6 * speed_factor]
        random.shuffle(start)
        self.x = start[0]
        self.y = -start[0]
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def brick_hit(self, pos):
        for brick_line in self.bricks:
            for brick in brick_line:
                brick_pos = self.canvas.coords(brick.id)
                try:
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            canvas.bell()
                            self.hit += 1
                            self.score.configure(text=f"{player_name}'s Score: {self.hit}")
                            self.canvas.delete(brick.id)
                            return True
                except:
                    continue
        return False

    def obstruction_hit(self, pos):
        for obstruction in self.obstructions:
            obstruction_pos = self.canvas.coords(obstruction)
            if pos[2] >= obstruction_pos[0] and pos[0] <= obstruction_pos[2]:
                if pos[3] >= obstruction_pos[1] and pos[1] <= obstruction_pos[3]:
                    self.x = -self.x
                    self.y = -self.y
                    return True
        return False

    def paddle_hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if self.brick_hit(pos):
            self.y = -self.y
        if self.obstruction_hit(pos):
            return
        if pos[1] <= 0:
            self.y = -self.y
        if pos[3] >= self.canvas_height:
            self.bottom_hit = True
        if pos[0] <= 0:
            self.x = -self.x
        if pos[2] >= self.canvas_width:
            self.x = -self.x
        if self.paddle_hit(pos):
            self.y = -self.y

class Paddle:
    def __init__(self, canvas, color, width):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, width, 10, fill=color)
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<Escape>", self.return_to_menu)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x <= 0:
            self.x = 0
        if pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    def turn_left(self, event):
        self.x = -3.5

    def turn_right(self, event):
        self.x = 3.5

    def return_to_menu(self, event):
        global playing
        playing = False
        show_menu()

class Bricks:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)

def reset_score():
    score.configure(text=f"{player_name}'s Score: 0")

def set_level(selected_level):
    global level
    level = selected_level
    canvas.delete("all")
    canvas.create_text(250, 250, text=f"Level {level} Selected!\nPress Enter to Start", fill="green", font="Consolas 18")

def show_menu():
    canvas.delete("all")
    canvas.create_text(250, 100, text="Bouncing Ball Game", fill="white", font="Consolas 28 bold")
    canvas.create_text(250, 200, text="Select Level (1-3)", fill="white", font="Consolas 24")
    canvas.create_text(250, 250, text="1: Easy", fill="green", font="Consolas 18")
    canvas.create_text(250, 300, text="2: Medium", fill="yellow", font="Consolas 18")
    canvas.create_text(250, 350, text="3: Hard", fill="red", font="Consolas 18")

root.bind("1", lambda event: set_level(1))
root.bind("2", lambda event: set_level(2))
root.bind("3", lambda event: set_level(3))

def start_game(event):
    global playing
    if playing is False:
        playing = True
        reset_score()
        canvas.delete("all")

        BALL_COLOR = ["red", "yellow", "white"]
        BRICK_COLOR = ["PeachPuff3", "dark slate gray", "rosy brown", "light goldenrod yellow", "turquoise3", "salmon"]
        random.shuffle(BALL_COLOR)

        paddle_width = 120 if level == 1 else 100 if level == 2 else 80
        speed_factor = 0.8 if level == 1 else 1 if level == 2 else 1.2

        paddle = Paddle(canvas, "blue", paddle_width)
        bricks = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                random.shuffle(BRICK_COLOR)
                tmp = Bricks(canvas, BRICK_COLOR[0])
                b.append(tmp)
            bricks.append(b)

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(bricks[i][j].id, 25 * j, 25 * i)

        obstructions = []
        if level in [2, 3]:
            num_obstructions = 2 if level == 2 else 4
            obstruction_areas = []

            while len(obstructions) < num_obstructions:
                x1 = random.randint(50, 400)
                y1 = random.randint(220, 320)
                x2 = x1 + random.randint(30, 60)
                y2 = y1 + random.randint(10, 30)

                new_obstruction = (x1, y1, x2, y2)

                overlap = any(
                    not (new_obstruction[2] < existing[0] or
                         new_obstruction[0] > existing[2] or
                         new_obstruction[3] < existing[1] or
                         new_obstruction[1] > existing[3])
                    for existing in obstruction_areas
                )

                if not overlap:
                    obstruction = canvas.create_rectangle(*new_obstruction, fill="gray")
                    obstructions.append(obstruction)
                    obstruction_areas.append(new_obstruction)

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score, speed_factor, obstructions)
        root.update_idletasks()
        root.update()

        time.sleep(1)
        while 1:
            if not ball.bottom_hit:
                ball.draw()
                paddle.draw()
                root.update_idletasks()
                root.update()
                time.sleep(0.01)
                if ball.hit == 95:
                    canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = False
                    break
            else:
                canvas.create_text(250, 250, text="GAME OVER!!", fill="red", font="Consolas 24 ")
                root.update_idletasks()
                root.update()
                playing = False
                break

root.bind_all("<Return>", start_game)
root.mainloop()