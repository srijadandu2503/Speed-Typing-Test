#registration,login,game 1
from tkinter import *
import os
import pygame
from pygame.locals import *
import sys
import time
import random


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            # login_sucess()
            instructions()

        else:
            password_not_recognised()

    else:
        user_not_found()
def instructions():
    global instruction_screen
    instruction_screen = Toplevel(main_screen)
    instruction_screen.geometry("450x300")
    instruction_screen.title("Instructions")
    Label(instruction_screen,text="INSTRUCTIONS\n * There are 3 levels in this Application.\n * The Start Button redirects you to Level 1\n * If you type the Given Sentence with 100% \nAccuracy within 25 seconds you \nget to play level 2 and then level 3\n* If the above conditions are not satisfied \nyou can retry in the same level until \nthe given conditions are satisfied\n**ALL THE BEST**\n", width="300", height="12", font=("Calibri", 12)).pack()
    Label(instruction_screen,text="").pack()
    Button(instruction_screen,text="Start Game", bg="blue", height="2", width="20", command=login_sucess).pack()
    Label(instruction_screen,text="").pack()

def login_sucess():
    login_screen.destroy();
    main_screen.destroy();
    class Game:

        def __init__(self):
            self.w = 850
            self.h = 500
            self.reset = True
            self.active = False
            self.input_text = ''
            self.word = ''
            self.time_start = 0
            self.total_time = 0
            self.accuracy = '0%'
            self.results = 'Time:0     Accuracy:0 %     Wpm:0 '
            self.wpm = 0
            self.end = False
            self.HEAD_C = (0, 0, 0)  # for colours
            self.TEXT_C = (0, 0, 0)
            self.RESULT_C = (0, 0, 0)

            pygame.init()
            self.open_img = pygame.image.load('type-speed-open.png')
            self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))
            self.bg = pygame.image.load('background.jpg')
            self.bg = pygame.transform.scale(self.bg, (900, 600))
            self.screen = pygame.display.set_mode((self.w, self.h))
            pygame.display.set_caption('Type Speed test')

        def draw_text(self, screen, msg, y, fsize, color):
            font = pygame.font.Font(None, fsize)
            text = font.render(msg, 1, color)
            text_rect = text.get_rect(center=(self.w / 2, y))
            screen.blit(text, text_rect)
            pygame.display.update()

        def get_sentence(self):
            f = open('level1.txt').read()
            sentences = f.split('\n')
            sentence = random.choice(sentences)
            return sentence

        def show_results(self, screen):
            if (not self.end):

                self.total_time = time.time() - self.time_start

                count = 0
                for i, c in enumerate(self.word):
                    try:
                        if self.input_text[i] == c:
                            count += 1
                    except:
                        pass
                self.accuracy = count / len(self.word) * 100


                self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
                self.end = True
                print(self.total_time)

                self.results = 'Time:' + str(round(self.total_time)) + " secs Accuracy:" + str(
                    round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))

                if (self.accuracy == 100 and self.total_time < 25) :
                    level2();
                self.time_img = pygame.image.load('icon.png')
                self.time_img = pygame.transform.scale(self.time_img, (150, 150))

                screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
                self.draw_text(screen, "", self.h - 70, 26, (100, 100, 100))

                print(self.results)
                pygame.display.update()


        def run(self):
            self.reset_game()

            self.running = True
            while (self.running):
                clock = pygame.time.Clock()
                self.screen.fill((0, 0, 0), (50, 250, 650, 50))
                pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)

                self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos()

                        if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
                            self.active = True
                            self.input_text = ''
                            self.time_start = time.time()

                        if (x >= 310 and x <= 510 and y >= 390 and self.end):
                            self.reset_game()
                            x, y = pygame.mouse.get_pos()


                    elif event.type == pygame.KEYDOWN:
                        if self.active and not self.end:
                            if event.key == pygame.K_RETURN:
                                print(self.input_text)
                                self.show_results(self.screen)
                                print(self.results)
                                self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                                self.end = True

                            elif event.key == pygame.K_BACKSPACE:
                                self.input_text = self.input_text[:-1]
                            else:
                                try:
                                    self.input_text += event.unicode
                                except:
                                    pass

                pygame.display.update()

            clock.tick(60)

        def reset_game(self):
            self.screen.blit(self.open_img, (0, 0))

            pygame.display.update()
            time.sleep(1)

            self.reset = False
            self.end = False

            self.input_text = ''
            self.word = ''
            self.time_start = 0
            self.total_time = 0
            self.wpm = 0


            self.word = self.get_sentence()
            if (not self.word): self.reset_game()
            # drawing heading
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.bg, (0, 0))
            msg = "Let's test your typing speed !!"
            self.draw_text(self.screen, msg, 60, 50, self.HEAD_C)

            pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

            self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

            pygame.display.update()

    level = 1
    def level1():
        global level
        level = 1
        mainLevel()
    def level2():
        global level
        level = 2
        mainLevel()
    def level3():
        global level
        level = 3
        mainLevel()

    def mainLevel():
        class Game:
            def __init__(self):
                self.w = 850
                self.h = 500
                self.reset = True
                self.active = False
                self.input_text = ''
                self.word = ''
                self.time_start = 0
                self.total_time = 0
                self.accuracy = '0%'
                self.results = 'Time:0     Accuracy:0 %     Wpm:0 '
                self.wpm = 0
                self.end = False
                self.HEAD_C = (0, 0, 0)  # for colours
                self.TEXT_C = (0, 0, 0)
                self.RESULT_C = (0, 0, 0)

                pygame.init()
                self.open_img = pygame.image.load('type-speed-open.png')
                self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))
                self.bg = pygame.image.load('background.jpg')
                self.bg = pygame.transform.scale(self.bg, (900, 600))
                self.screen = pygame.display.set_mode((self.w, self.h))
                pygame.display.set_caption('Type Speed test')

            def draw_text(self, screen, msg, y, fsize, color):
                font = pygame.font.Font(None, fsize)
                text = font.render(msg, 1, color)
                text_rect = text.get_rect(center=(self.w / 2, y))
                screen.blit(text, text_rect)
                pygame.display.update()

            def get_sentence(self):
                global level
                f = open('level1.txt').read()
                if(level == 1) :
                    f = open('level1.txt').read()
                if (level == 2):
                    f = open('level2.txt').read()
                if (level == 3):
                    f = open('level3.txt').read()


                sentences = f.split('\n')
                sentence = random.choice(sentences)
                return sentence

            def show_results(self, screen):
                global level

                if (not self.end):

                    self.total_time = time.time() - self.time_start

                    count = 0
                    for i, c in enumerate(self.word):
                        try:
                            if self.input_text[i] == c:
                                count += 1
                        except:
                            pass
                    self.accuracy = count / len(self.word) * 100

                    self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
                    self.end = True
                    print(self.total_time)

                    self.results = 'Time:' + str(round(self.total_time)) + " secs Accuracy:" + str(
                        round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))

                    self.time_img = pygame.image.load('icon.png')
                    self.time_img = pygame.transform.scale(self.time_img, (150, 150))

                    screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
                    self.draw_text(screen, "", self.h - 70, 26, (100, 100, 100))

                    print(self.results)
                    pygame.display.update()
                    if (self.accuracy == 100 and self.total_time < 25):
                        if (level == 1):
                            level2()
                        if (level == 2):
                            level3()
                        if (level == 3):
                            level4()
            def run(self):
                self.reset_game()

                self.running = True
                while (self.running):
                    clock = pygame.time.Clock()
                    self.screen.fill((0, 0, 0), (50, 250, 650, 50))
                    pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)

                    self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            self.running = False
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONUP:
                            x, y = pygame.mouse.get_pos()

                            if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
                                self.active = True
                                self.input_text = ''
                                self.time_start = time.time()

                            if (x >= 310 and x <= 510 and y >= 390 and self.end):
                                self.reset_game()
                                x, y = pygame.mouse.get_pos()


                        elif event.type == pygame.KEYDOWN:
                            if self.active and not self.end:
                                if event.key == pygame.K_RETURN:
                                    print(self.input_text)
                                    self.show_results(self.screen)
                                    print(self.results)
                                    self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                                    self.end = True

                                elif event.key == pygame.K_BACKSPACE:
                                    self.input_text = self.input_text[:-1]
                                else:
                                    try:
                                        self.input_text += event.unicode
                                    except:
                                        pass

                    pygame.display.update()

                clock.tick(60)

            def reset_game(self):
                self.screen.blit(self.open_img, (0, 0))

                pygame.display.update()
                time.sleep(1)

                self.reset = False
                self.end = False

                self.input_text = ''
                self.word = ''
                self.time_start = 0
                self.total_time = 0
                self.wpm = 0

                self.word = self.get_sentence()
                if (not self.word): self.reset_game()
                # drawing heading
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.bg, (0, 0))
                msg = "Let's test your typing speed !!"
                self.draw_text(self.screen, msg, 60, 50, self.HEAD_C)

                pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

                self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

                pygame.display.update()

        Game().run()
    Game().run()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Speed Typing Test")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()





