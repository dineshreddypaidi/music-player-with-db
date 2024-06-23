from db import Connection
from tkinter import *
from pygame import mixer
import tkinter.font as font
import random

class MusicPlayer:
    def __init__(self):
        mixer.init()
        self.root = Tk()
        self.root.configure(bg="#252525")
        self.root.geometry('550x250')
        self.root.resizable(0, 0)
        self.root.title("musicplayer")
        
        self.defined_font = font.Font(family='Helvetica')
        
        #collecting songs
        self.collection = Connection._connection()
        self.Songs = [x for x in self.collection.find()]
        
        self.id = 0
        self.song = self.Songs[self.id]
        self.songgpath = self.song['path']
        self.songgname = self.song['name']
        
        self.setup_ui()
        self.root.mainloop()
    
    def playfile(self, songgpath, songgname):
        self.resetui()
        try:
            print(f'currently playing..\n{songgname}\n')
            mixer.music.load(songgpath)
            mixer.music.play()
            self.songtext["text"] = songgname
        except FileNotFoundError:
            self.next()
    
    def play(self):
        self.playfile(self.songgpath, self.songgname)

    def pause(self):
        mixer.music.pause()
        bt = Button(self.frm, text="resume", command=self.resume, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt["font"] = self.defined_font
        bt.grid(row=1, column=1)
        self.pausedtext.config(text="Paused")

    def resume(self):
        mixer.music.unpause()
        self.resetui()

    def stop(self):
        mixer.music.stop()
        self.resetui()

    def next(self):
        self.id += 1
        if self.id >= len(self.Songs):
            self.id = 0
        self.song = self.Songs[self.id]
        self.playfile(self.song['path'], self.song['name'])

    def prev(self):
        self.id -= 1
        if self.id < 0:
            self.id = len(self.Songs) - 1
        self.song = self.Songs[self.id]
        self.playfile(self.song['path'], self.song['name'])

    def randomsong(self):
        self.id = random.randint(0, len(self.Songs) - 1)
        self.song = self.Songs[self.id]
        self.playfile(self.song['path'], self.song['name'])

    def resetui(self):
        bt = Button(self.frm, text="pause", command=self.pause, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt["font"] = self.defined_font
        bt.grid(row=1, column=1)
        self.pausedtext.config(text="")

    def setup_ui(self):
        self.my_menu = Menu(self.root, bg="#252525")
        self.my_menu.add_cascade(label=f'SONGS  ({len(self.Songs)})', font=self.defined_font)

        self.musicfrm = Frame(self.root, bg="#252525")
        self.musicfrm.pack(padx=10, pady=10)

        self.songtext = Label(self.musicfrm, text="song name", width=60, height=4, background="#252525", fg="#fff", font=(self.defined_font, 20))
        self.songtext.pack()

        self.frm = Frame(self.root, bg="#252525")
        self.frm.pack(padx=10, pady=10)

        bt = Button(self.frm, text="play", command=self.play, width=10, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt["font"] = self.defined_font
        bt.grid(row=1,column=2)

        bt1 = Button(self.frm, text="pause", command=self.pause, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt1["font"] = self.defined_font
        bt1.grid(row=1,column=1)
         
        bt2 = Button(self.frm, text="stop", command=self.stop, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt2["font"] = self.defined_font
        bt2.grid(row=1,column=3)
        
        bt3 = Button(self.frm, text="next", command=self.next, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt3["font"] = self.defined_font
        bt3.grid(row=1,column=4)
        
        bt4 = Button(self.frm, text="previous", command=self.prev, width=8, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt4["font"] = self.defined_font
        bt4.grid(row=1,column=0)
         
        bt5 = Button(self.frm, text="random", command=self.randomsong, width=10, bg="#b0a9ac", fg="#050204", activebackground="#52a9b3")
        bt5["font"] = self.defined_font
        bt5.grid(row=2,column=2)
          
        self.pausedtext = Label(self.frm, text="", width=5, background="#252525", fg="red", font=(self.defined_font, 18))
        self.pausedtext.grid(row=2, column=1)

        self.root.configure(menu=self.my_menu)

if __name__ == "__main__":
    MusicPlayer()