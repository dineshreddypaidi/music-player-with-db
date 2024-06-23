from songs import Songs
from player import MusicPlayer

print(" 1.initailze player \n 2.search for songs and update the db \n 3.update db and initailize the player")
choice = int(input("choose: "))

if choice == 1:
    MusicPlayer()
    
elif choice == 2:
    Songs.find_and_update_db()
    
elif choice == 3:
    Songs.find_and_update_db()
    MusicPlayer() 