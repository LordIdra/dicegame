from tkinter import *
from random import randint, choice
from time import sleep
from math import sin, cos, radians, pi


def convert(r, g, b):
    return "#%02x%02x%02x" % (int(r), int(g), int(b))

def getRGB(hx):
    return int(hx[1:3], 16), int(hx[3:5], 16), int(hx[5:7], 16)

class game:

    def __init__(self):
            
        #Check for file existance
        open('usernames.txt.', 'a+').close()
        open('passwords.txt.', 'a+').close()
        open('settings.txt.', 'a+').close()
        open('statistics.txt.', 'a+').close()

        #Initialization. Canvas can be moved around to fit the screen size if necessary
        self.window = Tk()
        self.window.title('DICEGAME')
        self.window.attributes('-fullscreen', True)
        
        self.canvas = Canvas(self.window, width = 3000, height = 3000, bg = convert(0, 0, 0), highlightthickness = 0)
        self.canvas.pack()
        self.window.update()

        sleep(0.1)
        
        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX

        #Startup code
        self.lines = list()
        self.colours = list()
        self.onscreen = list()
        
        def drawStartLine(value, colour = convert(0, 255, 0)):
            self.lines.append(value)
            self.colours.append(colour)
            
            if len(self.lines) > 35:
                self.lines.pop(0)
                self.colours.pop(0)
            else:
                pass

            #clear terminal
            for x in self.onscreen:
                self.canvas.delete(x)
            self.onscreen = []

            #redraw
            for x in range(len(self.lines)):
                self.onscreen.append(self.canvas.create_text(20*unitX, (x*20*unitY)+20, text = self.lines[x], fill = self.colours[x], font = ('courier new', int(10*unitX)), anchor = 'w'))

        def redrawStartLines():
            #clear terminal
            for x in self.onscreen:
                self.canvas.delete(x)
            self.onscreen = []

            #redraw
            for x in range(len(self.lines)):
                self.onscreen.append(self.canvas.create_text(20*unitX, (x*20*unitY)+20, text = self.lines[x], fill = self.colours[x], font = ('courier new', int(10*unitX)), anchor = 'w'))

        def progressSlider():
            progress = 0
            def upd():
                if progress > 0 and progress < 10:
                    self.lines[-1] = str(self.lines[-1][0:-2]) + str(progress) + '%'
                elif progress >= 10 and progress < 100:
                    self.lines[-1] = str(self.lines[-1][0:-3]) + str(progress) + '%'
                else:
                    self.lines[-1] = str(self.lines[-1][0:-4]) + str(progress) + '%'
                redrawStartLines()
                self.window.update()
                
            speed = int(choice([1, 2]))
            for x in range(int(100/speed)):
                progress += speed
                upd()
        startScript = '''PROGRAM STARTED

establishing connection...
connection established

>>version check
>>running version v1.0.2r
>>no new patches
VERSION CHECK COMPLETE

>>importing data
>>sql............█
>>gui............█
>>storage........█
>>rng............█
IMPORTS COMPLETE

>>loading modules
>>dicemodule...
loaded
>>mathmodule...
loaded
>>menumodule...
loaded
>>dmhsmodule...
loaded
>>hotelmodule...
trivago
MODULE LOAD COMPLETE

>>running data check
>>usernames......█
>>passwords......█
>>statistics.....█
>>settings.......█
DATA CHECK COMPLETE

final JVM loading...
>>$//DCJ-h47nbfu28
>>$//DCK-ufh28738f
>>$//DCL-oqa0h4484
JVM LOADING COMPLETE

program initialization complete'''.splitlines()
        for x in range(len(startScript)):
            drawStartLine(startScript[x])
            if startScript[x] != '':
                if startScript[x][-1] == '█':
                    progressSlider()
            sleep(randint(5, 8)/50)
            self.window.update()


        for i in range(18):
            for j in range(len(self.colours)):
                self.colours[j] = convert(0, 255-(i*15), 0)
                redrawStartLines()
            self.window.update()

        self.selectionScreen()





    def clearScreen(self):
        
        for x in self.canvas.winfo_children():
            x.configure(bd = 0)
            if x.winfo_class() == 'Scale':
                x.destroy()
            elif x.winfo_class() == 'Button':
                x.configure(command = '')
                x.configure(state = NORMAL)
            
        for i in range(100):


            
            for x in self.canvas.find_all():
                try:
                    r, g, b = getRGB(self.canvas.itemcget(x, 'fill'))
                    r = (r*0.96)
                    g = (g*0.96)
                    b = (b*0.96)
                    self.canvas.itemconfig(x, fill = convert(r, g, b))
                except:
                    pass

                try:
                    r, g, b = getRGB(self.canvas.itemcget(x, 'outline'))
                    r = (r*0.96)
                    g = (g*0.96)
                    b = (b*0.96)
                    self.canvas.itemconfig(x, outline = convert(r, g, b))
                except:
                    pass

                
                
            for x in self.canvas.winfo_children():
                if x.winfo_class() == 'Canvas':
                    for i in x.find_all():
                        try:
                            r, g, b = getRGB(x.itemcget(i, 'fill'))
                            r = (r*0.96)
                            g = (g*0.96)
                            b = (b*0.96)
                            x.itemconfig(i, fill = convert(r, g, b))
                        except:
                            pass

                        try:
                            r, g, b = getRGB(x.itemcget(i, 'outline'))
                            r = (r*0.96)
                            g = (g*0.96)
                            b = (b*0.96)
                            x.itemconfig(i, outline = convert(r, g, b))
                        except:
                            pass

                try:
                    r, g, b = getRGB(x.cget('bg'))
                    r = (r*0.96)
                    g = (g*0.96)
                    b = (b*0.96)
                    x.configure(bg = convert(r, g, b))
                except:
                    pass

                try:
                    r, g, b = getRGB(x.cget('fg'))
                    r = (r*0.96)
                    g = (g*0.96)
                    b = (b*0.96)
                    x.configure(fg = convert(r, g, b))
                except:
                    pass

                try:
                    r, g, b = getRGB(x.cget('troughcolor'))
                    r = (r*0.96)
                    g = (g*0.96)
                    b = (b*0.96)
                    x.configure(troughcolor = convert(r, g, b))
                except:
                    pass
                
                self.window.update()
                
        for x in self.canvas.winfo_children():
            x.destroy()

        self.window.update()


    def fadeIn(self):
        pbg = list()
        pfg = list()
        trc = list()

        fill = list()
        outline = list()

        for x in self.canvas.find_all():
            try:
                fill.append(self.canvas.itemcget(x, 'fill'))
                self.canvas.itemconfig(x, fill = convert(0, 0, 0))
            except:
                fill.append('invalid')
                
            try:
                outline.append(self.canvas.itemcget(x, 'outline'))
                self.canvas.itemconfig(x, fill = convert(0, 0, 0))
            except:
                outline.append('invalid')
        
        for x in self.canvas.winfo_children():
            try:
                pbg.append(x.cget('bg'))
                x.configure(bg = convert(0, 0, 0))
            except:
                pbg.append('invalid')
                
            try:
                pfg.append(x.cget('fg'))
                x.configure(fg = convert(0, 0, 0))
            except:
                pfg.append('invalid')

            try:
                x.configure(bd = 0)
            except:
                pass

            try:
                trc.append(x.cget('troughcolor'))
                x.configure(troughcolor = convert(0, 0, 0))
            except:
                trc.append('invalid')

        self.window.update()

        for x in range(len(pbg)):

            if str(pbg[x]) == 'invalid':
                pass
            if str(pbg[x])[0] != '#':
                pbg[x] = convert(0, 0, 0)

        for x in range(len(pfg)):
            if str(pfg[x]) == 'invalid':
                pass
            elif str(pfg[x])[0] != '#':
                pfg[x] = convert(255, 255, 255)

        for x in range(len(trc)):
            if str(trc[x]) == 'invalid':
                pass
            elif str(trc[x])[0] != '#':
                trc[x] = convert(255, 255, 255)

        for x in range(len(fill)):
            if str(fill[x]) == 'invalid':
                pass
            elif str(fill[x])[0] != '#':
                fill[x] = convert(255, 255, 255)

        for x in range(len(outline)):
            if str(outline[x]) == 'invalid':
                pass
            elif str(outline[x])[0] != '#':
                outline[x] = convert(255, 255, 255)

        children = self.canvas.winfo_children()
        canvasChildren = self.canvas.find_all()

        for i in range(25):
            for x in range(len(canvasChildren)):
                
                if str(fill[x]) == 'invalid':
                    pass
                else:
                    r, g, b = getRGB(fill[x])
                    r = (0.04*i)*r
                    g = (0.04*i)*g
                    b = (0.04*i)*b
                    self.canvas.itemconfig(canvasChildren[x], fill = convert(r, g, b))

                if str(outline[x]) == 'invalid':
                    pass
                else:
                    r, g, b = getRGB(outline[x])
                    r = (0.04*i)*r
                    g = (0.04*i)*g
                    b = (0.04*i)*b
                    self.canvas.itemconfig(canvasChildren[x], outline = convert(r, g, b))
                    
            for x in range(len(children)):
                
                if str(pbg[x]) == 'invalid':
                    pass
                else:
                    r, g, b = getRGB(pbg[x])
                    r = (0.01*i)*r
                    g = (0.01*i)*g
                    b = (0.01*i)*b
                    children[x].configure(bg = convert(r, g, b))

                if str(pfg[x]) == 'invalid':
                    pass
                else:
                    r, g, b = getRGB(pfg[x])
                    r = (0.04*i)*r
                    g = (0.04*i)*g
                    b = (0.04*i)*b
                    children[x].configure(fg = convert(r, g, b))

            self.window.update()

        for x in range(len(children)):
            if children[x].winfo_class() == 'Scale':
                r, g, b = getRGB(trc[x])
                children[x].configure(troughcolor = convert(r, g, b))

        self.window.update()

        
    def loadingScreen(self, time):

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX
            
        time = int(time*0.5)
        self.clearScreen()
        rots = radians(60)
        fade = 0
        for i in range(time):
            if i < 30:
                fade += 8.5
            if time - i < 30:
                fade -= 8.5
            points = [[1, 0]]
            self.canvas.delete('all')
            self.canvas.create_text(700*unitX, 400*unitY, text = 'LOADING', fill = convert(fade, fade, fade), font = ('', 15))
            for x in range(5):
                points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])

            for p in range(len(points)):
                points[p] = ([(points[p][0]*cos(radians(i*3))) - (points[p][1]*sin(radians(i*3))), ((points[p][0]*sin(radians(i*3))) + (points[p][1]*cos(radians(i*3))))])
            
            for x in range(len(points)-1):
                self.canvas.create_line((points[x][0]*80)+700*unitX, (points[x][1]*80)+400*unitY, (points[x+1][0]*80)+700*unitX, (points[x+1][1]*80)+400*unitY, fill = convert(0, 0, fade))
            self.canvas.create_line((points[-1][0]*80)+700*unitX, (points[-1][1]*80)+400*unitY, (points[0][0]*80)+700*unitX, (points[0][1]*80)+400*unitY, fill = convert(0, 0, fade))
            
            sleep(0.01)
            self.window.update()

        self.canvas.delete('all')
        self.window.update()
        sleep(0.3)

    def selectionScreen(self):

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX

        self.loadingScreen(randint(100, 200))

        def login():
            self.loadingScreen(randint(100, 200))
            
            def process():
                usernameFile = open('usernames.txt', 'r+')
                passwordFile = open('passwords.txt', 'r+')

                self.passwordEntry.configure(bg = convert(0, 100, 0))
                self.usernameEntry.configure(bg = convert(0, 100, 0))

                username = self.usernameEntry.get()
                password = self.passwordEntry.get()
                usernames = usernameFile.read().splitlines()
                passwords = passwordFile.read().splitlines()


                if username in usernames:
                    if password == passwords[usernames.index(username)]:
                        self.informationLabel.configure(text = 'success')
                        self.userIndex = usernames.index(username)
                        self.username = username
                        self.window.update()
                        sleep(1)
                        self.menu()
                    else:
                        self.passwordEntry.configure(bg = convert(100, 0, 20))
                        self.informationLabel.configure(text = 'invalid password')
                else:
                    self.usernameEntry.configure(bg = convert(100, 0, 0))
                    self.passwordEntry.configure(bg = convert(100, 0, 0))
                    self.informationLabel.configure(text = 'invalid username')

                usernameFile.close()
                passwordFile.close()

            self.titleLabel = Label(self.canvas, text = 'LOGIN', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
            self.usernameEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.passwordEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10), show = '*')
            self.loginButton = Button(self.canvas, text = 'LOGIN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = process, relief = 'sunken')
            self.returnButton = Button(self.canvas, text = 'RETURN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = self.selectionScreen, relief = 'sunken')
            self.usernameLabel = Label(self.canvas, text = 'username', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.passwordLabel = Label(self.canvas, text = 'password', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.informationLabel = Label(self.canvas, text = 'enter details', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))

            self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
            self.usernameEntry.place(x = 700*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
            self.passwordEntry.place(x = 700*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
            self.usernameLabel.place(x = 600*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
            self.passwordLabel.place(x = 600*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
            self.returnButton.place(x = 600*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
            self.loginButton.place(x = 700*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
            self.informationLabel.place(x = 600*unitX, y = 480*unitY, width = 200*unitX, height = 30*unitY)

            self.fadeIn()
            
            self.window.update()
                

        def register():
            self.loadingScreen(randint(100, 200))

            def process():
                self.usernameEntry.configure(bg = convert(0, 100, 0))
                self.passwordEntry.configure(bg = convert(0, 100, 0))
                self.confirmPasswordEntry.configure(bg = convert(0, 100, 0))
                
                username = self.usernameEntry.get()
                password = self.passwordEntry.get()
                confirm = self.confirmPasswordEntry.get()

                tempFile = open('usernames.txt', 'r+')

                breaker = False

                if username in tempFile.read().splitlines():
                    self.informationLabel.configure(text = 'username taken')
                    self.usernameEntry.configure(bg = convert(100, 0, 0))
                    self.passwordEntry.configure(bg = convert(100, 0, 0))
                    self.confirmPasswordEntry.configure(bg = convert(100, 0, 0))
                    breaker = True
                else:
                    if len(username) < 3:
                        self.informationLabel.configure(text = 'username too short')
                        self.usernameEntry.configure(bg = convert(100, 0, 0))
                        self.passwordEntry.configure(bg = convert(100, 0, 0))
                        self.confirmPasswordEntry.configure(bg = convert(100, 0, 0))
                        breaker = True
                    else:
                        if len(password) < 5:
                            self.informationLabel.configure(text = 'password too short')
                            self.passwordEntry.configure(bg = convert(100, 0, 0))
                            self.confirmPasswordEntry.configure(bg = convert(100, 0, 0))
                            breaker = True
                        else:
                            if password != confirm:
                                self.informationLabel.configure(text = 'passwords do not match')
                                self.confirmPasswordEntry.configure(bg = convert(100, 0, 0))
                                breaker = True

                tempFile.close()

                if breaker == True:
                    pass
                else:
                    usernames = open('usernames.txt', 'a+')
                    passwords = open('passwords.txt', 'a+')
                    settings = open('settings.txt', 'a+')
                    statistics = open('statistics.txt', 'a+')

                    usernames.write(username + '\n')
                    passwords.write(password + '\n')
                    settings.write('SB6SE RB5RE DB0DE PB0PE\n')
                    statistics.write('HB0HE TB0TE GB0GE\n')

                    usernames.close()
                    passwords.close()
                    settings.close()
                    statistics.close()

                    self.informationLabel.configure(text = 'success')
                    self.window.update()

                    sleep(1)
                    self.selectionScreen()


            self.titleLabel = Label(self.canvas, text = 'REGISTER', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
            self.usernameEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.passwordEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10), show = '*')
            self.confirmPasswordEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10), show = '*')
            self.loginButton = Button(self.canvas, text = 'REGISTER', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = process, relief = 'sunken')
            self.returnButton = Button(self.canvas, text = 'RETURN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = self.selectionScreen, relief = 'sunken')
            self.usernameLabel = Label(self.canvas, text = 'username', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.passwordLabel = Label(self.canvas, text = 'password', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.confirmPasswordLabel = Label(self.canvas, text = 'confirm', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
            self.informationLabel = Label(self.canvas, text = 'enter details', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))

            self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
            self.usernameEntry.place(x = 700*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
            self.passwordEntry.place(x = 700*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
            self.confirmPasswordEntry.place(x = 700*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
            self.usernameLabel.place(x = 600*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
            self.passwordLabel.place(x = 600*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
            self.confirmPasswordLabel.place(x = 600*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
            self.returnButton.place(x = 600*unitX, y = 480*unitY, width = 100*unitX, height = 30*unitY)
            self.loginButton.place(x = 700*unitX, y = 480*unitY, width = 100*unitX, height = 30*unitY)
            self.informationLabel.place(x = 600*unitX, y = 540*unitY, width = 200*unitX, height = 30*unitY)

            self.fadeIn()
            
            self.window.update()

        self.titleLabel = Label(self.canvas, text = 'DICE GAME', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
        self.loginButton = Button(self.canvas, text = 'LOGIN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                  activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), highlightbackground = convert(40, 40, 40),
                                  relief = 'sunken', command = login)
        self.registerButton = Button(self.canvas, text = 'REGISTER', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                  activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), highlightbackground = convert(40, 40, 40),
                                     relief = 'sunken', command = register)

        self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
        self.loginButton.place(x = 650*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.registerButton.place(x = 650*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)

        self.fadeIn()
        
        self.window.mainloop()

    def menu(self):

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX
            
        self.loadingScreen(randint(100, 200))

        self.titleLabel = Label(self.canvas, text = 'MENU', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))

        self.singleplayerButton = Button(self.canvas, text = 'singleplayer', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.singleplayer)
        self.localMultiplayerButton = Button(self.canvas, text = 'multiplayer', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.multiplayer)
        self.networkMultiplayerButton = Button(self.canvas, text = 'lobby', bg = convert(50, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(50, 0, 0), activeforeground = convert(255, 255, 255), relief = 'sunken')
        self.settingsButton = Button(self.canvas, text = 'settings', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.settings)
        self.statisticsButton = Button(self.canvas, text = 'statistics', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.statistics)
        self.leaderboardButton = Button(self.canvas, text = 'leaderboard', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.leaderboard)
        self.logoutButton = Button(self.canvas, text = 'logout', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.selectionScreen)

        self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
        self.singleplayerButton.place(x = 625*unitX, y = 300*unitY, width = 150*unitX, height = 40*unitY)
        self.localMultiplayerButton.place(x = 625*unitX, y = 360*unitY, width = 150*unitX, height = 40*unitY)
        self.networkMultiplayerButton.place(x = 625*unitX, y = 420*unitY, width = 150*unitX, height = 40*unitY)
        self.settingsButton.place(x = 625*unitX, y = 480*unitY, width = 150*unitX, height = 40*unitY)
        self.statisticsButton.place(x = 625*unitX, y = 540*unitY, width = 150*unitX, height = 40*unitY)
        self.leaderboardButton.place(x = 625*unitX, y = 600*unitY, width = 150*unitX, height = 40*unitY)
        self.logoutButton.place(x = 625*unitX, y = 660*unitY, width = 150*unitX, height = 40*unitY)

        self.fadeIn()
        
        self.window.update()


    def settings(self):
        #1) x sided dice
        #2) round numbers
        #3) difficulty
        #4) starting player
        #SB7SE RB6RE DB2DE PB1PE


        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX

        self.clearScreen()

        self.loadingScreen(randint(100, 200))

        def writeSettings():
            fileRead = open('settings.txt', 'r+')
            settings = fileRead.read().splitlines()
            fileRead.close()

            sides = str(self.sidesSlider.get())
            rounds = str(self.roundsSlider.get())
            difficulty = str(self.difficultySlider.get())
            starting = str(self.startingSlider.get())

            settings[self.userIndex] = 'SB' + sides + 'SE' + ' ' + 'RB' + rounds + 'RE' + ' ' + 'DB' + difficulty + 'DE' + ' ' + 'PB' + starting + 'PE'

            fileWrite = open('settings.txt', 'w+')
            fileWrite.write(''.join([str(x + '\n') for x in settings]))
            fileWrite.close()

            sleep(0.05)

        def interfaceUpdate(arbitrary):
            writeSettings()
            
            fileRead = open('settings.txt', 'r+')
            userSettings = fileRead.read().splitlines()[self.userIndex]
            fileRead.close()

            sides = int(userSettings[userSettings.index('SB')+2:userSettings.index('SE')])
            rounds = int(userSettings[userSettings.index('RB')+2:userSettings.index('RE')])
            difficulty = int(userSettings[userSettings.index('DB')+2:userSettings.index('DE')])
            starting = int(userSettings[userSettings.index('PB')+2:userSettings.index('PE')])

            self.sidesSlider.configure(troughcolor = convert(255-(sides*15), (sides*15), 0))
            self.roundsSlider.configure(troughcolor = convert(255-(rounds*15), (rounds*15), 0))
            self.difficultySlider.configure(troughcolor = convert(255-(difficulty*50), (difficulty*50), 0))
            self.startingSlider.configure(troughcolor = convert(255-(starting*255), (starting*255), 0))

            self.sidesCounter.config(text = sides)
            self.roundsCounter.config(text = rounds)
            self.difficultyCounter.config(text = difficulty)
            self.startingCounter.config(text = starting)

        fileRead = open('settings.txt', 'r+')
        userSettings = fileRead.read().splitlines()[self.userIndex]
        fileRead.close()

        sides = int(userSettings[userSettings.index('SB')+2:userSettings.index('SE')])
        rounds = int(userSettings[userSettings.index('RB')+2:userSettings.index('RE')])
        difficulty = int(userSettings[userSettings.index('DB')+2:userSettings.index('DE')])
        starting = int(userSettings[userSettings.index('PB')+2:userSettings.index('PE')])

        self.titleLabel = Label(self.canvas, text = 'SETTINGS', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
        self.returnButton = Button(self.canvas, text = 'return', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 40, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.menu)
        
        self.sidesSlider = Scale(self.canvas, bg = convert(0, 0, 0), fg = convert(0, 0, 0), troughcolor = convert(0, 0, 0), highlightcolor = convert(0, 0, 0),
                                 resolution = 1, orient = HORIZONTAL, from_ = 6, to = 16, showvalue = False, relief = SUNKEN, borderwidth = 0,
                                 activebackground = convert(0, 0, 40), highlightthickness = 0, command = interfaceUpdate)
        self.roundsSlider = Scale(self.canvas, bg = convert(0, 0, 0), fg = convert(0, 0, 0), troughcolor = convert(0, 0, 0), highlightcolor = convert(0, 0, 0),
                                 resolution = 1, orient = HORIZONTAL, from_ = 4, to = 16, showvalue = False, relief = SUNKEN, borderwidth = 0,
                                 activebackground = convert(0, 0, 40), highlightthickness = 0, command = interfaceUpdate)
        self.difficultySlider = Scale(self.canvas, bg = convert(0, 0, 0), fg = convert(0, 0, 0), troughcolor = convert(0, 0, 0), highlightcolor = convert(0, 0, 0),
                                 resolution = 1, orient = HORIZONTAL, from_ = 0, to = 4, showvalue = False, relief = SUNKEN, borderwidth = 0,
                                 activebackground = convert(0, 0, 40), highlightthickness = 0, command = interfaceUpdate, state = DISABLED)
        self.startingSlider = Scale(self.canvas, bg = convert(0, 0, 0), fg = convert(0, 0, 0), troughcolor = convert(0, 0, 0), highlightcolor = convert(0, 0, 0),
                                 resolution = 1, orient = HORIZONTAL, from_ = 0, to = 1, showvalue = False, relief = SUNKEN, borderwidth = 0,
                                 activebackground = convert(0, 0, 40), highlightthickness = 0, command = interfaceUpdate, state = NORMAL)
        
        self.sidesLabel = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = 'sides', font = ('courier new', 10))
        self.roundsLabel = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = 'rounds', font = ('courier new', 10))
        self.difficultyLabel = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = '-----', font = ('courier new', 10))
        self.startingLabel = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = 'starting', font = ('courier new', 10))

        self.sidesCounter = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = '0')
        self.roundsCounter = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = '0')
        self.difficultyCounter = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = '-')
        self.startingCounter = Label(self.canvas, bg = convert(0, 0, 0), fg = convert(255, 255, 255), highlightthickness = 0, text = '0')
        
        self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
        self.returnButton.place(x = 650*unitX, y = 530*unitY, width = 100*unitX, height = 30*unitY)
        
        self.sidesSlider.place(x = 600*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.roundsSlider.place(x = 600*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
        self.difficultySlider.place(x = 600*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
        self.startingSlider.place(x = 600*unitX, y = 480*unitY, width = 100*unitX, height = 30*unitY)

        self.sidesLabel.place(x = 700*unitX, y = 290*unitY, width = 100*unitX, height = 30*unitY)
        self.roundsLabel.place(x = 700*unitX, y = 350*unitY, width = 100*unitX, height = 30*unitY)
        self.difficultyLabel.place(x = 700*unitX, y = 410*unitY, width = 100*unitX, height = 30*unitY)
        self.startingLabel.place(x = 700*unitX, y = 470*unitY, width = 100*unitX, height = 30*unitY)

        self.sidesCounter.place(x = 780*unitX, y = 290*unitY, width = 100*unitX, height = 30*unitY)
        self.roundsCounter.place(x = 780*unitX, y = 350*unitY, width = 100*unitX, height = 30*unitY)
        self.difficultyCounter.place(x = 780*unitX, y = 410*unitY, width = 100*unitX, height = 30*unitY)
        self.startingCounter.place(x = 780*unitX, y = 470*unitY, width = 100*unitX, height = 30*unitY)

        self.sidesSlider.configure(troughcolor = convert(255-(sides*15), (sides*15), 0))
        self.roundsSlider.configure(troughcolor = convert(255-(rounds*15), (rounds*15), 0))
        self.difficultySlider.configure(troughcolor = convert(255-(difficulty*50), (difficulty*50), 0))
        self.startingSlider.configure(troughcolor = convert(255-(starting*255), (starting*255), 0))

        self.sidesSlider.set(sides)
        self.roundsSlider.set(rounds)
        self.difficultySlider.set(difficulty)
        self.startingSlider.set(starting)

        self.fadeIn()
        
        self.window.update()



    def statistics(self):

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX

        self.clearScreen()

        self.loadingScreen(randint(100, 200))

        file = open('statistics.txt', 'r+')

        stats = file.read().splitlines()[self.userIndex]

        highscore = stats[stats.index('HB')+2:stats.index('HE')]
        total = stats[stats.index('TB')+2:stats.index('TE')]
        games = stats[stats.index('GB')+2:stats.index('GE')]

        file.close()
        
        self.titleLabel = Label(self.canvas, text = 'STATISTICS', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
        self.returnButton = Button(self.canvas, text = 'return', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.menu)
        
        self.highscoreCounter = Label(self.canvas, text = highscore, bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.totalCounter = Label(self.canvas, text = total, bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.gamesCounter = Label(self.canvas, text = games, bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))

        self.highscoreLabel = Label(self.canvas, text = 'highscore', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.totalLabel = Label(self.canvas, text = 'total', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.gamesLabel = Label(self.canvas, text = 'games', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))

        self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
        self.returnButton.place(x = 650*unitX, y = 480*unitY, width = 100*unitX, height = 30*unitY)

        self.highscoreCounter.place(x = 700*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.totalCounter.place(x = 700*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
        self.gamesCounter.place(x = 700*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)

        self.highscoreLabel.place(x = 600*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.totalLabel.place(x = 600*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
        self.gamesLabel.place(x = 600*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)

        self.fadeIn()

        self.window.update()


    def leaderboard(self):
        self.clearScreen()
        self.loadingScreen(randint(100, 200))

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX
            
        #Sort leaderboard
        file = open('leaderboard.txt', 'r+')
        contents = file.read().splitlines()
        file.close()

        scores = []
        games = []
        for x in contents:
            scores.append([x[x.index('TB')+2:x.index('TE')]])
            games.append(x)

        if len(contents) > 2: #would raise an error
            #Swapsort. If the item to the left is larger, move the element to the left
            movement = True
            while movement == True:
                movement = False
                for x in range(len(scores)-1):
                    if scores[x] < scores[x+1]:
                        
                        Sleft = scores[x]
                        Sright = scores[x+1]
                        Gleft = games[x]
                        Gright = games[x+1]
                        
                        scores[x] = Sright
                        scores[x+1] = Sleft
                        games[x] = Gright
                        games[x+1] = Gleft
                        
                        movement = True

        #I'm not going to bother writing this back to the file because I've had problems with it in the past and the efficiency increase wouldn't be that high
        #So now we need to create an interface to display all this. We'll do the top 10 results
        self.scoreTITLE = Label(self.canvas, text = 'SCORE', bg = convert(0, 0, 0), fg = convert(100, 100, 200), font = ('courier new', 20), anchor = 'center')
        self.nameTITLE = Label(self.canvas, text = 'NAME', bg = convert(0, 0, 0), fg = convert(100, 100, 200), font = ('courier new', 20), anchor = 'center')
        self.roundsTITLE = Label(self.canvas, text = 'ROUNDS', bg = convert(0, 0, 0), fg = convert(100, 100, 200), font = ('courier new', 20), anchor = 'center')
        self.sidesTITLE = Label(self.canvas, text = 'SIDES', bg = convert(0, 0, 0), fg = convert(100, 100, 200), font = ('courier new', 20), anchor = 'center')
        self.startingTITLE = Label(self.canvas, text = 'STARTING', bg = convert(0, 0, 0), fg = convert(100, 100, 200), font = ('courier new', 20), anchor = 'center')
        
        self.scoreTITLE.place(x = width-(500*unitX), y = height-(200*unitX), height = unitY*50, width = unitX*200)
        self.nameTITLE.place(x = width-(300*unitX), y = height-(200*unitX), height = unitY*50, width = unitX*200)
        self.roundsTITLE.place(x = width-(100*unitX), y = height-(200*unitX), height = unitY*50, width = unitX*200)
        self.sidesTITLE.place(x = width+(100*unitX), y = height-(200*unitX), height = unitY*50, width = unitX*200)
        self.startingTITLE.place(x = width+(300*unitX), y = height-(200*unitX), height = unitY*50, width = unitX*200)

        for x in range(10):
            if x == 0:
                colour = convert(220, 200, 50) #gold
            elif x == 1:
                colour = convert(255, 255, 255) #silver
            elif x == 2:
                colour = convert(255, 170, 80) #bronze
            else:
                colour = convert(180, 180, 180) #gray for contrast with silver

            if x < len(scores):
                score = scores[x]
                name = games[x][games[x].index('UB')+2:games[x].index('UE')]
                rounds = games[x][games[x].index('RB')+2:games[x].index('RE')]
                sides = games[x][games[x].index('SB')+2:games[x].index('SE')]
                starting = games[x][games[x].index('PB')+2:games[x].index('PE')]
            else:
                score = '---'
                name = '---'
                rounds = '---'
                sides = '---'
                starting = '---'
            
            self.canvas.create_text(width-(500*unitX)+100, height-(150*unitX)+(x*40)+20, fill = colour, text = score, font = ('courier new', 12), anchor = 'center')
            self.canvas.create_text(width-(300*unitX)+100, height-(150*unitX)+(x*40)+20, fill = colour, text = name, font = ('courier new', 12), anchor = 'center')
            self.canvas.create_text(width-(100*unitX)+100, height-(150*unitX)+(x*40)+20, fill = colour, text = rounds, font = ('courier new', 12), anchor = 'center')
            self.canvas.create_text(width+(100*unitX)+100, height-(150*unitX)+(x*40)+20, fill = colour, text = sides, font = ('courier new', 12), anchor = 'center')
            self.canvas.create_text(width+(300*unitX)+100, height-(150*unitX)+(x*40)+20, fill = colour, text = starting, font = ('courier new', 12), anchor = 'center')

        self.returnButton = Button(self.canvas, text = 'return', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                   activebackground = convert(0, 50, 0), activeforeground = convert(255, 255, 255), relief = 'sunken', command = self.menu)
        self.returnButton.place(x = 650*unitX, y = 650*unitY, width = 100*unitX, height = 30*unitY)
        
        self.fadeIn()

        self.window.update()
        

    def singleplayer(self):
        #This is the big part!
        #There will be three dice, each nested within the other one. The outer two will be spun in opposite directions as normal
        #to provide our two random dice throws. Faster than just using one
        #The one in the centre will have a different animation/look to it and will be used if the player rolls a double
        #Each player will have their own 'terminal' windows in which the results from the dice throws + logic will be shown
        #There is going to be another challenge here. Ideally we want the whole thing to take up the entire screen to feel more immersive
        #So we're going to have to account for different screen resolutions.
        #How are we going to do this? We're going to use a system based on the centre of the screen, then add and subtract from there
        #Addition and subtraction will be multiplied by a certain unit also dependant on screen resolution to keep stuff on the screen
        #I'm developing with a 1366 x 768 display so let's centre on that.
        #Additionally the height/width will have to be proportional to each other. In other words, a cube is going to remain a cube - not a rectangle

        self.clearScreen()
        self.loadingScreen(randint(100, 200))

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX

        self.player1title = Label(self.canvas, text = self.username, bg = convert(0, 0, 0), fg = convert(0, 255, 0), font = ('', 25), anchor = 'center')
        self.player2title = Label(self.canvas, text = 'Computer', bg = convert(0, 0, 0), fg = convert(255, 0, 0), font = ('', 25), anchor = 'center')
        self.player1scoreLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(0, 255, 0), font = ('', 20), anchor = 'center')
        self.player2scoreLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(255, 0, 0), font = ('', 20), anchor = 'center')

        self.player1console = Canvas(self.canvas, bg = convert(0, 0, 0), highlightcolor = convert(0, 0, 0), highlightthickness = 0, bd = 0)
        self.player2console = Canvas(self.canvas, bg = convert(0, 0, 0), highlightcolor = convert(0, 0, 0), highlightthickness = 0, bd = 0)

        self.player1title.place(x = width+(unitX*400), y = height+(unitY*-370), height = unitY*60, width = unitX*200)
        self.player2title.place(x = width+(unitX*-600), y = height+(unitY*-370), height = unitY*60, width = unitX*200)
        self.player1scoreLabel.place(x = width+(unitX*400), y = height+(unitY*-300), height = unitY*60, width = unitX*200)
        self.player2scoreLabel.place(x = width+(unitX*-600), y = height+(unitY*-300), height = unitY*60, width = unitX*200)

        self.player1console.place(x = width+(unitX*400), y = height+(unitY*-200), height = unitY*420, width = unitX*200)
        self.player2console.place(x = width+(unitX*-600), y = height+(unitY*-200), height = unitY*420, width = unitX*200)

        self.player1lines = list()
        self.player1colours = list()

        self.player2lines = list()
        self.player2colours = list()
        
        def addLine(player, line, colour = convert(255, 255, 255)):

            if player == 1:
                
                self.player1lines.append(line)
                self.player1colours.append(colour)
                
                if len(self.player1lines) > 20:
                    
                    self.player1lines.pop(0)
                    self.player1colours.pop(0)
                    
                self.player1console.delete('all')
                
                for i in range(len(self.player1lines)):

                    self.player1console.create_text(10, int(i*20)+20, text = self.player1lines[i], fill = self.player1colours[i], font = ('courier new', int(unitY*10)), anchor = 'w')



            if player == 2:
                
                self.player2lines.append(line)
                self.player2colours.append(colour)
                
                if len(self.player2lines) > 20:
                    
                    self.player2lines.pop(0)
                    self.player2colours.pop(0)

                self.player2console.delete('all')
                
                for i in range(len(self.player2lines)):

                    self.player2console.create_text(10, int(i*20)+20, text = self.player2lines[i], fill = self.player2colours[i], font = ('courier new', int(unitY*10)), anchor = 'w')


        #And now comes a fairly difficult part: drawing this dice
        #This will involve some basic trigonometry to rotate our vectors, similar to what we did in the loading screen
        file = open('settings.txt', 'r+')
        settings = file.read().splitlines()[self.userIndex]
        numberOfSides = int(settings[settings.index('SB')+2:settings.index('SE')])
        rounds = int(settings[settings.index('RB')+2:settings.index('RE')])
        starting = int(settings[settings.index('PB')+2:settings.index('PE')])
        file.close()
        
        rots = radians(360/numberOfSides)
        points = [[1, 0]]

        outter = list()
        inner = list()

        for x in range(numberOfSides-1):
            points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
            

        for x in range(len(points)-1):
            outter.append(self.canvas.create_line((points[x][0]*(1200/(numberOfSides/2)))+width, (points[x][1]*(1200/(numberOfSides/2)))+height, (points[x+1][0]*(1200/(numberOfSides/2)))+width, (points[x+1][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
            outter.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(1200/(numberOfSides/2)))+width, ((points[x][1]+points[x+1][1])/2)*(1200/(numberOfSides/2))+height,
                                    text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))
            
        outter.append(self.canvas.create_line((points[-1][0]*(1200/(numberOfSides/2)))+width, (points[-1][1]*(1200/(numberOfSides/2)))+height, (points[0][0]*(1200/(numberOfSides/2)))+width, (points[0][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
        outter.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(1200/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(1200/(numberOfSides/2)))+height,
                                    text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))

            
        for x in range(len(points)-1):
            outter.append(self.canvas.create_line((points[x][0]*(800/(numberOfSides/2)))+width, (points[x][1]*(800/(numberOfSides/2)))+height, (points[x+1][0]*(800/(numberOfSides/2)))+width, (points[x+1][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
            outter.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(800/(numberOfSides/2))+width), ((points[x][1]+points[x+1][1])/2)*(800/(numberOfSides/2))+height,
                                    text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))
            
        outter.append(self.canvas.create_line((points[-1][0]*(800/(numberOfSides/2)))+width, (points[-1][1]*(800/(numberOfSides/2)))+height, (points[0][0]*(800/(numberOfSides/2)))+width, (points[0][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
        outter.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(800/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(800/(numberOfSides/2)))+height,
                                    text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))

            
        for x in range(len(points)-1):
            inner.append(self.canvas.create_line((points[x][0]*(400/(numberOfSides/2)))+width, (points[x][1]*(400/(numberOfSides/2)))+height, (points[x+1][0]*(400/(numberOfSides/2)))+width, (points[x+1][1]*(400/(numberOfSides/2)))+height, fill = convert(220, 140, 0)))
            inner.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(400/(numberOfSides/2)))+width, (((points[x][1]+points[x+1][1])/2)*(400/(numberOfSides/2)))+height,
                                    text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

        inner.append(self.canvas.create_line((points[-1][0]*(400/(numberOfSides/2)))+width, (points[-1][1]*(400/(numberOfSides/2)))+height, (points[0][0]*(400/(numberOfSides/2)))+width, (points[0][1]*(400/(numberOfSides/2)))+height, fill = convert(220, 140, 0)))
        inner.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(400/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(400/(numberOfSides/2)))+height,
                                    text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

        #I really don't know what I was on when I wrote this code but here we are
        #Copy and paste will be a very strongly used tool when it comes to the dice spinning script.
        self.totalLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', int(20/unitX)))
        self.totalLabel.place(x = width-(30*unitX), y = height-(30*unitY), width = 60, height = 60)

        self.roundsCounter = Label(self.canvas, text = rounds, bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', int(20/unitX)))
        self.roundsCounter.place(x = width-(40*unitX), y = height-(350*unitY), width = 80*unitX, height = 60*unitY)

        global upperText
        global lowerText
        global upperLine
        global lowerLine

        upperText = list()
        lowerText = list()
        upperLine = list()
        lowerLine = list()

        def roll():
            global upperText
            global lowerText
            global upperLine
            global lowerLine

            for x in upperText:
                self.canvas.delete(x)
            for x in lowerText:
                self.canvas.delete(x)
            for x in upperLine:
                self.canvas.delete(x)
            for x in lowerLine:
                self.canvas.delete(x)
            for x in outter:
                self.canvas.delete(x)
                
            #OH NO
            #COPY PASTE TIME!!!
            rotation = randint(400, 500)
            dice2co = randint(100, 200)/100
            speed1 = randint(100, 300)/100
            speed2 = randint(600, 1000)/100
            circ1 = 0
            circ2 = 0
            lowerText = list()
            lowerLine = list()
            upperText = list()
            upperLine = list()
            for i in range(rotation):

                if rotation-i < 150:
                    speed1 *= 0.97
                    speed2 *= 0.95

                circ1 += speed1
                circ2 += speed2

                for x in upperText:
                    self.canvas.delete(x)
                for x in lowerText:
                    self.canvas.delete(x)
                for x in upperLine:
                    self.canvas.delete(x)
                for x in lowerLine:
                    self.canvas.delete(x)
                
                rots = radians(360/numberOfSides)
                points = [[1, 0]]

                lowerText = list()
                lowerLine = list()
                upperText = list()
                upperLine = list()

                for x in range(numberOfSides-1):
                    points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
                for p in range(len(points)):
                    points[p] = ([(points[p][0]*cos(radians(circ1))) - (points[p][1]*sin(radians(circ1))), ((points[p][0]*sin(radians(circ1))) + (points[p][1]*cos(radians(circ1))))])
                    
                for x in range(len(points)-1):
                    upperLine.append(self.canvas.create_line((points[x][0]*(1200/(numberOfSides/2)))+width, (points[x][1]*(1200/(numberOfSides/2)))+height, (points[x+1][0]*(1200/(numberOfSides/2)))+width, (points[x+1][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                    upperText.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(1200/(numberOfSides/2)))+width, ((points[x][1]+points[x+1][1])/2)*(1200/(numberOfSides/2))+height,
                                            text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))
                    
                upperLine.append(self.canvas.create_line((points[-1][0]*(1200/(numberOfSides/2)))+width, (points[-1][1]*(1200/(numberOfSides/2)))+height, (points[0][0]*(1200/(numberOfSides/2)))+width, (points[0][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                upperText.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(1200/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(1200/(numberOfSides/2)))+height,
                                            text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))

                rots = radians(360/numberOfSides)
                points = [[1, 0]]

                for x in range(numberOfSides-1):
                    points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
                for p in range(len(points)):
                    points[p] = ([(points[p][0]*cos(radians(-circ2))) - (points[p][1]*sin(radians(-circ2))), ((points[p][0]*sin(radians(-circ2))) + (points[p][1]*cos(radians(-circ2))))])
                    
                for x in range(len(points)-1):
                    lowerLine.append(self.canvas.create_line((points[x][0]*(800/(numberOfSides/2)))+width, (points[x][1]*(800/(numberOfSides/2)))+height, (points[x+1][0]*(800/(numberOfSides/2)))+width, (points[x+1][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                    lowerText.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(800/(numberOfSides/2))+width), ((points[x][1]+points[x+1][1])/2)*(800/(numberOfSides/2))+height,
                                            text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))
                    
                lowerLine.append(self.canvas.create_line((points[-1][0]*(800/(numberOfSides/2)))+width, (points[-1][1]*(800/(numberOfSides/2)))+height, (points[0][0]*(800/(numberOfSides/2)))+width, (points[0][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                lowerText.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(800/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(800/(numberOfSides/2)))+height,
                                            text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))

                lowerList = list(self.canvas.coords(x)[1] for x in lowerText)
                upperList = list(self.canvas.coords(x)[1] for x in upperText)
                
                dice1 = lowerList.index(min(lowerList))+1
                dice2 = upperList.index(min(upperList))+1
                
                total = dice1 + dice2
                self.totalLabel.configure(text = str(total))

                self.window.update()
                
            return dice1, dice2


        global ln
        global pnt
        ln = list()
        pnt = list()

        def bonusRoll():
            global ln
            global pnt

            for x in ln:
                self.canvas.delete(x)
            for x in pnt:
                self.canvas.delete(x)
            for x in inner:
                self.canvas.delete(x)
            #oh no 2
            #more copy and paste
            rotations = 200
            circ = 0
            circSep = 0
            speed = 5

            pnt = list()
            ln = list()
            
            for i in range(rotations):

                if rotations-i < 80:
                    speed *= 0.93

                for x in ln:
                    self.canvas.delete(x)
                for x in pnt:
                    self.canvas.delete(x)

                pnt = list()
                ln = list()

                points = [[1, 0]]
                circ += speed
                
                for x in range(numberOfSides-1):
                    points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])

                for p in range(len(points)):
                    points[p] = ([(points[p][0]*cos(radians(-circ))) - (points[p][1]*sin(radians(-circ))), ((points[p][0]*sin(radians(-circ))) + (points[p][1]*cos(radians(-circ))))])


                for x in range(len(points)-1):
                    ln.append(self.canvas.create_line(((points[x][0]*(400/(numberOfSides/2))))+width, ((points[x][1]*(400/(numberOfSides/2))))+height, ((points[x+1][0]*(400/(numberOfSides/2))))+width, ((points[x+1][1]*(400/(numberOfSides/2))))+height, fill = convert(220, 140, 0)))
                    pnt.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(400/(numberOfSides/2)))+width, (((points[x][1]+points[x+1][1])/2)*(400/(numberOfSides/2)))+height,
                                            text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

                ln.append(self.canvas.create_line(((points[-1][0]*(400/(numberOfSides/2))))+width, ((points[-1][1]*(400/(numberOfSides/2))))+height, ((points[0][0]*(400/(numberOfSides/2))))+width, ((points[0][1]*(400/(numberOfSides/2))))+height, fill = convert(220, 140, 0)))
                pnt.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(400/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(400/(numberOfSides/2)))+height,
                                            text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

                mainList = list(self.canvas.coords(x)[1] for x in pnt)
                
                dice = mainList.index(min(mainList))+1
                
                self.totalLabel.configure(text = str(dice))

                sleep(0.01)
                self.window.update()
                
            return dice



        #And now the main code which will mostly make use of the above functions
        roundsPlayed = 0
        
        play = False
        
        def move():
            play = True

        var = IntVar()
        self.rollButton = Button(self.canvas, text = 'ROLL', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), highlightbackground = convert(40, 40, 40),
                                relief = 'sunken', state = DISABLED, command = lambda: var.set(1))
        self.rollButton.place(x = width+(450*unitX), y = height+(300*unitY), width = 100*unitX, height = 30*unitY)
        
        score = [0, 0]
        toAdd = 0

        player = starting+1

        addLine(player, 'You are starting.', convert(255, 255, 0))
        
        while roundsPlayed < rounds:

            addLine(player, 'YOUR TURN!', convert(80, 80, 160))
            addLine(player, '')

            self.window.update()

            if player == 1:
                self.rollButton.configure(state = 'normal')
                self.rollButton.wait_variable(var)
                self.rollButton.configure(state = DISABLED)
            else:
                pass

            toAdd = 0

            self.roundsCounter.configure(text = str(rounds-roundsPlayed))
            
            self.window.update()

            dice1, dice2 = roll()
            total = dice1 + dice2
            
            if total % 2 == 0:
                toAdd += 10
                addLine(player, 'TOTAL EVEN          +10', convert(0, 255, 0))
            else:
                toAdd -= 5
                addLine(player, 'TOTAL ODD           -5', convert(255, 0, 0))

            if dice1 == dice2:
                addLine(player, 'DOUBLE ROLLED!', convert(230, 50, 140))
                bonus = bonusRoll()
                addLine(player, 'BONUS ROLL          +' + str(bonus), convert(230, 50, 140))
                toAdd += bonus

            addLine(player,     'DICE ROLL           +' + str(total), convert(0, 255, 0))
            toAdd += total

            self.window.update()
            sleep(0.5)
            addLine(player, '')
            
            if toAdd >= 0:
                addLine(player, 'NET SCORE           +' + str(toAdd), convert(0, 255, 0))
            else:
                addLine(player, 'NET SCORE           ' + str(toAdd), convert(255, 0, 0))

            score[player-1] += toAdd
            
            if score[player-1] < 0:
                score[player-1] = 0

            addLine(player,     'TOTAL                ' + str(score[player-1]), convert(50, 50, 200))
            addLine(player, '')
            addLine(player, '')

            if player == 1:
                self.player1scoreLabel.configure(text = score[0])
            else:
                self.player2scoreLabel.configure(text = score[1])
            
            roundsPlayed += 1

            self.window.update()
            sleep(2)
            
            if player == 1:
                player = 2
            else:
                player = 1
        
        #End game script
        self.roundsCounter.configure(text = '0')
        self.window.update()
        
        #File updates
        file = open('statistics.txt', 'r+')
        contents = file.read().splitlines()
        userStats = contents[self.userIndex]
        previousHigh = int(userStats[userStats.index('HB')+2:userStats.index('HE')])
        previousTotal = int(userStats[userStats.index('TB')+2:userStats.index('TE')])
        previousGames = int(userStats[userStats.index('GB')+2:userStats.index('GE')])

        if score[0] > score[1]:
            if previousHigh < score[0]:
                contents[self.userIndex] = 'HB' + str(score[0]) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE'
            else:
                contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'
        else:
            contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE'

        file.close()

        sleep(0.5) #Just in case, to prevent timing issues wiping all data or something. Probably overkill but still a good idea
        
        file = open('statistics.txt', 'w+')
        file.write(''.join([str(x + '\n') for x in contents]))
        file.close()

        if score[0] > score[1]:
            
            file = open('settings.txt', 'r+')
            
            userSettings = file.read().splitlines()[self.userIndex]
            
            sides = int(userSettings[userSettings.index('SB')+2:userSettings.index('SE')])
            rounds = int(userSettings[userSettings.index('RB')+2:userSettings.index('RE')])
            difficulty = int(userSettings[userSettings.index('DB')+2:userSettings.index('DE')])
            starting = int(userSettings[userSettings.index('PB')+2:userSettings.index('PE')])

            file.close()

            file = open('leaderboard.txt', 'a+')
            file.write('UB' + str(self.username) + 'UE RB' + str(rounds) + 'RE SB' + str(sides) + 'SE PB' + str(starting) + 'PE TB' + str(score[0]) + 'TE')
            file.close()

        #Interface updates
        
        self.clearScreen()
        self.canvas.delete('all')
            
        rects = list()
        fade = 0
        
        for n in range(21):
            rects.append(self.canvas.create_rectangle(0, ((n-0.99)*38.4)*unitY, 1366*unitX, ((n*38.4)+10)*unitY, fill = convert(0, 0, 0)))

        self.indicator = self.canvas.create_text(width, height-(300*unitY), text = '', fill = convert(0, 0, 0), font = ('courier new', 80))
        self.score1indicator = self.canvas.create_text(width, height-(200*unitY), text = self.username + ' - ' + str(score[0]), fill = convert(0, 0, 0), font = ('courier new', 30))
        self.score2indicator = self.canvas.create_text(width, height-(150*unitY), text = 'computer' + ' - ' + str(score[1]), fill = convert(0, 0, 0), font = ('courier new', 30))
        
        if score[0] > score[1]:
            self.canvas.itemconfig(self.indicator, text = 'SUCCESS')
            win = True
        else:
            self.canvas.itemconfig(self.indicator, text = 'FAILURE')
            win = False

        for x in range(200):
            if fade < 250:
                fade += 5
                if win == True:
                    self.canvas.itemconfig(self.indicator, fill = convert(0, fade, 0))
                    self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                else:
                    self.canvas.itemconfig(self.indicator, fill = convert(fade, 0, 0))
                    self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                    
            for n in range(len(rects)):
                self.canvas.itemconfig(rects[n], fill = convert(0, 0, (sin(x*(pi/400))/(n+1))*250))
                self.window.update()
            sleep(0.03)

        for x in range(50):
            fade -= 5
            if win == True:
                self.canvas.itemconfig(self.indicator, fill = convert(0, fade, 0))
                self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
            else:
                self.canvas.itemconfig(self.indicator, fill = convert(fade, 0, 0))
                self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                
            for n in range(len(rects)):
                self.canvas.itemconfig(rects[n], fill = convert(0, 0, (sin((250-(5*x))*(pi/400))/(n+1))*250))
                
            sleep(0.03)

            self.window.update()

        sleep(2)
        
        self.menu()




    def multiplayer(self):

        width = self.window.winfo_width()/2 #center of screen X
        height = self.window.winfo_height()/2 #center of screen Y
        unitX = width/(1366/2)
        unitY = height/(768/2)
        if unitX > unitY:
            unitX = unitY
        elif unitY > unitX:
            unitY = unitX
        
        self.clearScreen()

        self.loadingScreen(randint(100, 200))

        
            
        def process():

            file = open('settings.txt', 'r+')
            settings = file.read().splitlines()[self.userIndex]
            numberOfSides = int(settings[settings.index('SB')+2:settings.index('SE')])
            rounds = int(settings[settings.index('RB')+2:settings.index('RE')])
            starting = int(settings[settings.index('PB')+2:settings.index('PE')])
            file.close()

            self.clearScreen()

            self.loadingScreen(randint(100, 200))

            self.player1title = Label(self.canvas, text = self.username, bg = convert(0, 0, 0), fg = convert(0, 255, 0), font = ('', 25), anchor = 'center')
            self.player2title = Label(self.canvas, text = self.opponentUsername, bg = convert(0, 0, 0), fg = convert(255, 0, 0), font = ('', 25), anchor = 'center')
            self.player1scoreLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(0, 255, 0), font = ('', 20), anchor = 'center')
            self.player2scoreLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(255, 0, 0), font = ('', 20), anchor = 'center')

            self.player1console = Canvas(self.canvas, bg = convert(0, 0, 0), highlightcolor = convert(0, 0, 0), highlightthickness = 0, bd = 0)
            self.player2console = Canvas(self.canvas, bg = convert(0, 0, 0), highlightcolor = convert(0, 0, 0), highlightthickness = 0, bd = 0)

            self.player1title.place(x = width+(unitX*400), y = height+(unitY*-370), height = unitY*60, width = unitX*200)
            self.player2title.place(x = width+(unitX*-600), y = height+(unitY*-370), height = unitY*60, width = unitX*200)
            self.player1scoreLabel.place(x = width+(unitX*400), y = height+(unitY*-300), height = unitY*60, width = unitX*200)
            self.player2scoreLabel.place(x = width+(unitX*-600), y = height+(unitY*-300), height = unitY*60, width = unitX*200)

            self.player1console.place(x = width+(unitX*400), y = height+(unitY*-200), height = unitY*420, width = unitX*200)
            self.player2console.place(x = width+(unitX*-600), y = height+(unitY*-200), height = unitY*420, width = unitX*200)

            self.totalLabel = Label(self.canvas, text = '0', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', int(20/unitX)))
            self.totalLabel.place(x = width-(30*unitX), y = height-(30*unitY), width = 60, height = 60)

            self.roundsCounter = Label(self.canvas, text = rounds, bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', int(20/unitX)))
            self.roundsCounter.place(x = width-(40*unitX), y = height-(350*unitY), width = 80*unitX, height = 60*unitY)

            self.player1lines = list()
            self.player1colours = list()

            self.player2lines = list()
            self.player2colours = list()
            
            def addLine(player, line, colour = convert(255, 255, 255)):

                if player == 1:
                    
                    self.player1lines.append(line)
                    self.player1colours.append(colour)
                    
                    if len(self.player1lines) > 20:
                        
                        self.player1lines.pop(0)
                        self.player1colours.pop(0)
                        
                    self.player1console.delete('all')
                    
                    for i in range(len(self.player1lines)):

                        self.player1console.create_text(10, int(i*20)+20, text = self.player1lines[i], fill = self.player1colours[i], font = ('courier new', int(unitY*10)), anchor = 'w')



                if player == 2:
                    
                    self.player2lines.append(line)
                    self.player2colours.append(colour)
                    
                    if len(self.player2lines) > 20:
                        
                        self.player2lines.pop(0)
                        self.player2colours.pop(0)

                    self.player2console.delete('all')
                    
                    for i in range(len(self.player2lines)):

                        self.player2console.create_text(10, int(i*20)+20, text = self.player2lines[i], fill = self.player2colours[i], font = ('courier new', int(unitY*10)), anchor = 'w')


            #And now comes a fairly difficult part: drawing this dice
            #This will involve some basic trigonometry to rotate our vectors, similar to what we did in the loading screen
            rots = radians(360/numberOfSides)
            points = [[1, 0]]

            outter = list()
            inner = list()

            for x in range(numberOfSides-1):
                points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
                

            for x in range(len(points)-1):
                outter.append(self.canvas.create_line((points[x][0]*(1200/(numberOfSides/2)))+width, (points[x][1]*(1200/(numberOfSides/2)))+height, (points[x+1][0]*(1200/(numberOfSides/2)))+width, (points[x+1][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                outter.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(1200/(numberOfSides/2)))+width, ((points[x][1]+points[x+1][1])/2)*(1200/(numberOfSides/2))+height,
                                        text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))
                
            outter.append(self.canvas.create_line((points[-1][0]*(1200/(numberOfSides/2)))+width, (points[-1][1]*(1200/(numberOfSides/2)))+height, (points[0][0]*(1200/(numberOfSides/2)))+width, (points[0][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
            outter.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(1200/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(1200/(numberOfSides/2)))+height,
                                        text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))

                
            for x in range(len(points)-1):
                outter.append(self.canvas.create_line((points[x][0]*(800/(numberOfSides/2)))+width, (points[x][1]*(800/(numberOfSides/2)))+height, (points[x+1][0]*(800/(numberOfSides/2)))+width, (points[x+1][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                outter.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(800/(numberOfSides/2))+width), ((points[x][1]+points[x+1][1])/2)*(800/(numberOfSides/2))+height,
                                        text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))
                
            outter.append(self.canvas.create_line((points[-1][0]*(800/(numberOfSides/2)))+width, (points[-1][1]*(800/(numberOfSides/2)))+height, (points[0][0]*(800/(numberOfSides/2)))+width, (points[0][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
            outter.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(800/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(800/(numberOfSides/2)))+height,
                                        text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))

                
            for x in range(len(points)-1):
                inner.append(self.canvas.create_line((points[x][0]*(400/(numberOfSides/2)))+width, (points[x][1]*(400/(numberOfSides/2)))+height, (points[x+1][0]*(400/(numberOfSides/2)))+width, (points[x+1][1]*(400/(numberOfSides/2)))+height, fill = convert(220, 140, 0)))
                inner.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(400/(numberOfSides/2)))+width, (((points[x][1]+points[x+1][1])/2)*(400/(numberOfSides/2)))+height,
                                        text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

            inner.append(self.canvas.create_line((points[-1][0]*(400/(numberOfSides/2)))+width, (points[-1][1]*(400/(numberOfSides/2)))+height, (points[0][0]*(400/(numberOfSides/2)))+width, (points[0][1]*(400/(numberOfSides/2)))+height, fill = convert(220, 140, 0)))
            inner.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(400/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(400/(numberOfSides/2)))+height,
                                        text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

            global upperText
            global lowerText
            global upperLine
            global lowerLine

            upperText = list()
            lowerText = list()
            upperLine = list()
            lowerLine = list()

            def roll():
                global upperText
                global lowerText
                global upperLine
                global lowerLine

                for x in upperText:
                    self.canvas.delete(x)
                for x in lowerText:
                    self.canvas.delete(x)
                for x in upperLine:
                    self.canvas.delete(x)
                for x in lowerLine:
                    self.canvas.delete(x)
                for x in outter:
                    self.canvas.delete(x)
                    
                #OH NO
                #COPY PASTE TIME!!!
                rotation = randint(400, 500)
                dice2co = randint(100, 200)/100
                speed1 = randint(100, 300)/100
                speed2 = randint(600, 1000)/100
                circ1 = 0
                circ2 = 0
                lowerText = list()
                lowerLine = list()
                upperText = list()
                upperLine = list()
                for i in range(rotation):

                    if rotation-i < 150:
                        speed1 *= 0.97
                        speed2 *= 0.95

                    circ1 += speed1
                    circ2 += speed2

                    for x in upperText:
                        self.canvas.delete(x)
                    for x in lowerText:
                        self.canvas.delete(x)
                    for x in upperLine:
                        self.canvas.delete(x)
                    for x in lowerLine:
                        self.canvas.delete(x)
                    
                    rots = radians(360/numberOfSides)
                    points = [[1, 0]]

                    lowerText = list()
                    lowerLine = list()
                    upperText = list()
                    upperLine = list()

                    for x in range(numberOfSides-1):
                        points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
                    for p in range(len(points)):
                        points[p] = ([(points[p][0]*cos(radians(circ1))) - (points[p][1]*sin(radians(circ1))), ((points[p][0]*sin(radians(circ1))) + (points[p][1]*cos(radians(circ1))))])
                        
                    for x in range(len(points)-1):
                        upperLine.append(self.canvas.create_line((points[x][0]*(1200/(numberOfSides/2)))+width, (points[x][1]*(1200/(numberOfSides/2)))+height, (points[x+1][0]*(1200/(numberOfSides/2)))+width, (points[x+1][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                        upperText.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(1200/(numberOfSides/2)))+width, ((points[x][1]+points[x+1][1])/2)*(1200/(numberOfSides/2))+height,
                                                text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))
                        
                    upperLine.append(self.canvas.create_line((points[-1][0]*(1200/(numberOfSides/2)))+width, (points[-1][1]*(1200/(numberOfSides/2)))+height, (points[0][0]*(1200/(numberOfSides/2)))+width, (points[0][1]*(1200/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                    upperText.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(1200/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(1200/(numberOfSides/2)))+height,
                                                text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(13*unitX))))

                    rots = radians(360/numberOfSides)
                    points = [[1, 0]]

                    for x in range(numberOfSides-1):
                        points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])
                    for p in range(len(points)):
                        points[p] = ([(points[p][0]*cos(radians(-circ2))) - (points[p][1]*sin(radians(-circ2))), ((points[p][0]*sin(radians(-circ2))) + (points[p][1]*cos(radians(-circ2))))])
                        
                    for x in range(len(points)-1):
                        lowerLine.append(self.canvas.create_line((points[x][0]*(800/(numberOfSides/2)))+width, (points[x][1]*(800/(numberOfSides/2)))+height, (points[x+1][0]*(800/(numberOfSides/2)))+width, (points[x+1][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                        lowerText.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(800/(numberOfSides/2))+width), ((points[x][1]+points[x+1][1])/2)*(800/(numberOfSides/2))+height,
                                                text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))
                        
                    lowerLine.append(self.canvas.create_line((points[-1][0]*(800/(numberOfSides/2)))+width, (points[-1][1]*(800/(numberOfSides/2)))+height, (points[0][0]*(800/(numberOfSides/2)))+width, (points[0][1]*(800/(numberOfSides/2)))+height, fill = convert(0, 0, 255)))
                    lowerText.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(800/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(800/(numberOfSides/2)))+height,
                                                text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(10*unitX))))

                    lowerList = list(self.canvas.coords(x)[1] for x in lowerText)
                    upperList = list(self.canvas.coords(x)[1] for x in upperText)
                    
                    dice1 = lowerList.index(min(lowerList))+1
                    dice2 = upperList.index(min(upperList))+1
                    
                    total = dice1 + dice2
                    self.totalLabel.configure(text = str(total))

                    self.window.update()
                    
                return dice1, dice2


            global ln
            global pnt
            ln = list()
            pnt = list()

            def bonusRoll():
                global ln
                global pnt

                for x in ln:
                    self.canvas.delete(x)
                for x in pnt:
                    self.canvas.delete(x)
                for x in inner:
                    self.canvas.delete(x)
                #oh no 2
                #more copy and paste
                rotations = 200
                circ = 0
                circSep = 0
                speed = 5

                pnt = list()
                ln = list()
                
                for i in range(rotations):

                    if rotations-i < 80:
                        speed *= 0.93

                    for x in ln:
                        self.canvas.delete(x)
                    for x in pnt:
                        self.canvas.delete(x)

                    pnt = list()
                    ln = list()

                    points = [[1, 0]]
                    circ += speed
                    
                    for x in range(numberOfSides-1):
                        points.append([(points[x][0]*cos(rots)) - (points[x][1]*sin(rots)), ((points[x][0]*sin(rots)) + (points[x][1]*cos(rots)))])

                    for p in range(len(points)):
                        points[p] = ([(points[p][0]*cos(radians(-circ))) - (points[p][1]*sin(radians(-circ))), ((points[p][0]*sin(radians(-circ))) + (points[p][1]*cos(radians(-circ))))])


                    for x in range(len(points)-1):
                        ln.append(self.canvas.create_line(((points[x][0]*(400/(numberOfSides/2))))+width, ((points[x][1]*(400/(numberOfSides/2))))+height, ((points[x+1][0]*(400/(numberOfSides/2))))+width, ((points[x+1][1]*(400/(numberOfSides/2))))+height, fill = convert(220, 140, 0)))
                        pnt.append(self.canvas.create_text((((points[x][0]+points[x+1][0])/2)*(400/(numberOfSides/2)))+width, (((points[x][1]+points[x+1][1])/2)*(400/(numberOfSides/2)))+height,
                                                text = x+1, fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

                    ln.append(self.canvas.create_line(((points[-1][0]*(400/(numberOfSides/2))))+width, ((points[-1][1]*(400/(numberOfSides/2))))+height, ((points[0][0]*(400/(numberOfSides/2))))+width, ((points[0][1]*(400/(numberOfSides/2))))+height, fill = convert(220, 140, 0)))
                    pnt.append(self.canvas.create_text((((points[-1][0]+points[0][0])/2)*(400/(numberOfSides/2)))+width, (((points[-1][1]+points[0][1])/2)*(400/(numberOfSides/2)))+height,
                                                text = str(numberOfSides), fill = convert(255, 255, 255), font = ('courier new', int(7*unitX))))

                    mainList = list(self.canvas.coords(x)[1] for x in pnt)
                    
                    dice = mainList.index(min(mainList))+1
                    
                    self.totalLabel.configure(text = str(dice))

                    sleep(0.01)
                    self.window.update()
                    
                return dice



            #And now the main code which will mostly make use of the above functions
            roundsPlayed = 0
            
            play = False
            
            def move():
                play = True

            var1 = IntVar()
            var2 = IntVar()
            
            self.rollButton1 = Button(self.canvas, text = 'ROLL', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                    activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), highlightbackground = convert(40, 40, 40),
                                    relief = 'sunken', state = DISABLED, command = lambda: var1.set(1))
            self.rollButton1.place(x = width+(450*unitX), y = height+(300*unitY), width = 100*unitX, height = 30*unitY)
            self.rollButton2 = Button(self.canvas, text = 'ROLL', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10),
                                    activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), highlightbackground = convert(40, 40, 40),
                                    relief = 'sunken', state = DISABLED, command = lambda: var2.set(1))
            self.rollButton2.place(x = width-(450*unitX), y = height+(300*unitY), width = 100*unitX, height = 30*unitY)
            
            score = [0, 0]
            toAdd = 0

            player = starting+1

            addLine(player, 'You are starting.', convert(255, 255, 0))

            self.fadeIn()
            
            while roundsPlayed < rounds:

                addLine(player, 'YOUR TURN!', convert(80, 80, 160))
                addLine(player, '')

                self.window.update()

                if player == 1:
                    self.rollButton1.configure(state = 'normal')
                    self.rollButton1.wait_variable(var1)
                    self.rollButton1.configure(state = DISABLED)
                else:
                    self.rollButton2.configure(state = 'normal')
                    self.rollButton2.wait_variable(var2)
                    self.rollButton2.configure(state = DISABLED)

                toAdd = 0

                self.roundsCounter.configure(text = str(rounds-roundsPlayed))
                
                self.window.update()

                dice1, dice2 = roll()
                total = dice1 + dice2
                
                if total % 2 == 0:
                    toAdd += 10
                    addLine(player, 'TOTAL EVEN          +10', convert(0, 255, 0))
                else:
                    toAdd -= 5
                    addLine(player, 'TOTAL ODD           -5', convert(255, 0, 0))

                if dice1 == dice2:
                    addLine(player, 'DOUBLE ROLLED!', convert(230, 50, 140))
                    bonus = bonusRoll()
                    addLine(player, 'BONUS ROLL          +' + str(bonus), convert(230, 50, 140))
                    toAdd += bonus

                addLine(player,     'DICE ROLL           +' + str(total), convert(0, 255, 0))
                toAdd += total

                self.window.update()
                sleep(0.5)
                addLine(player, '')
                
                if toAdd >= 0:
                    addLine(player, 'NET SCORE           +' + str(toAdd), convert(0, 255, 0))
                else:
                    addLine(player, 'NET SCORE           ' + str(toAdd), convert(255, 0, 0))

                score[player-1] += toAdd
                
                if score[player-1] < 0:
                    score[player-1] = 0

                addLine(player,     'TOTAL                ' + str(score[player-1]), convert(50, 50, 200))
                addLine(player, '')
                addLine(player, '')

                if player == 1:
                    self.player1scoreLabel.configure(text = score[0])
                else:
                    self.player2scoreLabel.configure(text = score[1])
                
                roundsPlayed += 1

                self.window.update()
                sleep(2)
                
                if player == 1:
                    player = 2
                else:
                    player = 1
            
            #End game script
            self.roundsCounter.configure(text = '0')
            self.window.update()
            
            #File updates
            file = open('statistics.txt', 'r+')
            contents = file.read().splitlines()
            userStats = contents[self.userIndex]
            previousHigh = int(userStats[userStats.index('HB')+2:userStats.index('HE')])
            previousTotal = int(userStats[userStats.index('TB')+2:userStats.index('TE')])
            previousGames = int(userStats[userStats.index('GB')+2:userStats.index('GE')])

            if score[0] > score[1]:
                if previousHigh < score[0]:
                    contents[self.userIndex] = 'HB' + str(score[0]) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'
                else:
                    contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'
            else:
                contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'

            file.close()

            sleep(0.5) #Just in case, to prevent timing issues wiping all data or something. Probably overkill but still a good idea
            
            file = open('statistics.txt', 'w+')
            file.write(''.join([str(x + '\n') for x in contents]))
            file.close()


            file = open('statistics.txt', 'r+')
            contents = file.read().splitlines()
            userStats = contents[self.opponentIndex]
            previousHigh = int(userStats[userStats.index('HB')+2:userStats.index('HE')])
            previousTotal = int(userStats[userStats.index('TB')+2:userStats.index('TE')])
            previousGames = int(userStats[userStats.index('GB')+2:userStats.index('GE')])

            if score[1] > score[0]:
                if previousHigh < score[1]:
                    contents[self.userIndex] = 'HB' + str(score[0]) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'
                else:
                    contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'
            else:
                contents[self.userIndex] = 'HB' + str(previousHigh) + 'HE' + ' ' + 'TB' + str(int(previousTotal)+int(score[0])) + 'TE' + ' ' + 'GB' + str(previousGames+1) + 'GE\n'

            file.close()

            sleep(0.5) #Just in case, to prevent timing issues wiping all data or something. Probably overkill but still a good idea
            
            file = open('statistics.txt', 'w+')
            file.write(''.join(contents))
            file.close()

            

            if score[0] > score[1]:
                
                file = open('settings.txt', 'r+')
                
                userSettings = file.read().splitlines()[self.userIndex]
                
                sides = int(userSettings[userSettings.index('SB')+2:userSettings.index('SE')])
                rounds = int(userSettings[userSettings.index('RB')+2:userSettings.index('RE')])
                difficulty = int(userSettings[userSettings.index('DB')+2:userSettings.index('DE')])
                starting = int(userSettings[userSettings.index('PB')+2:userSettings.index('PE')])

                file.close()

                file = open('leaderboard.txt', 'a+')
                file.write('\nUB' + str(self.username) + 'UE RB' + str(rounds) + 'RE SB' + str(sides) + 'SE PB' + str(starting) + 'PE TB' + str(score[0]) + 'TE')
                file.close()

            elif score[1] > score[0]:
                
                file = open('settings.txt', 'r+')
                
                userSettings = file.read().splitlines()[self.opponentIndex]
                
                sides = int(userSettings[userSettings.index('SB')+2:userSettings.index('SE')])
                rounds = int(userSettings[userSettings.index('RB')+2:userSettings.index('RE')])
                difficulty = int(userSettings[userSettings.index('DB')+2:userSettings.index('DE')])
                starting = int(userSettings[userSettings.index('PB')+2:userSettings.index('PE')])

                file.close()

                file = open('leaderboard.txt', 'a+')
                file.write('\nUB' + str(self.opponentUsername) + 'UE RB' + str(rounds) + 'RE SB' + str(sides) + 'SE PB' + str(starting) + 'PE TB' + str(score[0]) + 'TE')
                file.close()

            #Interface updates
            
            self.clearScreen()
            self.canvas.delete('all')
                
            rects = list()
            fade = 0
            
            for n in range(21):
                rects.append(self.canvas.create_rectangle(0, ((n-0.99)*38.4)*unitY, 1366*unitX, ((n*38.4)+10)*unitY, fill = convert(0, 0, 0)))

            self.indicator = self.canvas.create_text(width, height-(300*unitY), text = '', fill = convert(0, 0, 0), font = ('courier new', 80))
            self.score1indicator = self.canvas.create_text(width, height-(200*unitY), text = self.username + ' - ' + str(score[0]), fill = convert(0, 0, 0), font = ('courier new', 30))
            self.score2indicator = self.canvas.create_text(width, height-(150*unitY), text = self.opponentUsername + ' - ' + str(score[1]), fill = convert(0, 0, 0), font = ('courier new', 30))
            
            if score[0] > score[1]:
                self.canvas.itemconfig(self.indicator, text = self.username + ' WINS')
                win = True
            else:
                self.canvas.itemconfig(self.indicator, text = self.opponentUsername + ' WINS')
                win = False

            for x in range(200):
                if fade < 250:
                    fade += 5
                    if win == True:
                        self.canvas.itemconfig(self.indicator, fill = convert(0, fade, 0))
                        self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                        self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                    else:
                        self.canvas.itemconfig(self.indicator, fill = convert(fade, 0, 0))
                        self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                        self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                        
                for n in range(len(rects)):
                    self.canvas.itemconfig(rects[n], fill = convert(0, 0, (sin(x*(pi/400))/(n+1))*250))
                    self.window.update()
                sleep(0.03)

            for x in range(50):
                fade -= 5
                if win == True:
                    self.canvas.itemconfig(self.indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                else:
                    self.canvas.itemconfig(self.indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score1indicator, fill = convert(fade, fade, fade))
                    self.canvas.itemconfig(self.score2indicator, fill = convert(fade, fade, fade))
                    
                for n in range(len(rects)):
                    self.canvas.itemconfig(rects[n], fill = convert(0, 0, (sin((250-(5*x))*(pi/400))/(n+1))*250))
                    
                sleep(0.03)

                self.window.update()

            sleep(2)
            
            self.menu()

        def checkCreds():
            usernameFile = open('usernames.txt', 'r+')
            passwordFile = open('passwords.txt', 'r+')

            self.passwordEntry.configure(bg = convert(0, 100, 0))
            self.usernameEntry.configure(bg = convert(0, 100, 0))

            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            usernames = usernameFile.read().splitlines()
            passwords = passwordFile.read().splitlines()

            if username in usernames:
                if password == passwords[usernames.index(username)]:
                    if username != self.username:
                        self.informationLabel.configure(text = 'success')
                        self.opponentIndex = username.index(username)
                        self.opponentUsername = username
                        self.window.update()
                        sleep(1)
                        process()
                    else:
                        self.usernameEntry.configure(bg = convert(100, 0, 0))
                        self.passwordEntry.configure(bg = convert(100, 0, 0))
                        self.informationLabel.configure(text = 'you cannot play against yourself')
                else:
                    self.passwordEntry.configure(bg = convert(100, 0, 20))
                    self.informationLabel.configure(text = 'invalid password')
            else:
                self.usernameEntry.configure(bg = convert(100, 0, 0))
                self.passwordEntry.configure(bg = convert(100, 0, 0))
                self.informationLabel.configure(text = 'invalid username')

            usernameFile.close()
            passwordFile.close()
            
        self.titleLabel = Label(self.canvas, text = 'OPPONENT LOGIN', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 30))
        self.usernameEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10), text = 'Idra')
        self.passwordEntry = Entry(self.canvas, bg = convert(0, 0, 70), fg = convert(255, 255, 255), font = ('courier new', 10), text = 'testing', show = '*')
        self.loginButton = Button(self.canvas, text = 'LOGIN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = checkCreds, relief = 'sunken')
        self.returnButton = Button(self.canvas, text = 'RETURN', bg = convert(0, 50, 0), fg = convert(255, 255, 255), font = ('courier new', 10), activebackground = convert(0, 0, 40), activeforeground = convert(255, 255, 255), command = self.selectionScreen, relief = 'sunken')
        self.usernameLabel = Label(self.canvas, text = 'username', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.passwordLabel = Label(self.canvas, text = 'password', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))
        self.informationLabel = Label(self.canvas, text = 'enter details', bg = convert(0, 0, 0), fg = convert(255, 255, 255), font = ('courier new', 10))

        self.titleLabel.place(x = 500*unitX, y = 200*unitY, width = 400*unitX, height = 100*unitY)
        self.usernameEntry.place(x = 700*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.passwordEntry.place(x = 700*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
        self.usernameLabel.place(x = 600*unitX, y = 300*unitY, width = 100*unitX, height = 30*unitY)
        self.passwordLabel.place(x = 600*unitX, y = 360*unitY, width = 100*unitX, height = 30*unitY)
        self.returnButton.place(x = 600*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
        self.loginButton.place(x = 700*unitX, y = 420*unitY, width = 100*unitX, height = 30*unitY)
        self.informationLabel.place(x = 600*unitX, y = 480*unitY, width = 200*unitX, height = 30*unitY)

        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)
        
        self.fadeIn()
        
        self.window.update()


g = game()
