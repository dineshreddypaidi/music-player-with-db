import os
import fnmatch
from db import Connection

class Songs:
    def FindSong(patterns,paths):
        print("searching for songs in the OS")
        songs = []
        x = 1
        for pattern in patterns:
            for path in paths:
                for root, dirs, files in os.walk(path):
                    for name in files:
                        file_path = os.path.join(root, name)
                        if fnmatch.fnmatch(name, pattern) and os.path.getsize(file_path) > 1024 * 1024:
                            songg = {}
                            songg["_id"] = x
                            songg["path"] = file_path
                            songg['name'] = name
                            songs.append(songg)
                            x += 1
                            
        print("searching completed..")
        print(f"found {len(songs)} songs in the device")
        return songs
         
    def upload_to_collection(set_of_songs):
        collection = Connection._connection()
        if collection.delete_many({}):
            print("deleted old data records")
        if collection.insert_many(set_of_songs):
            print("database updated succesfully")
        
    def find_and_update_db():
        songextensions = ["*.mp3",]
    
        osname = os.name
        if osname == 'nt':
            searchpaths = ["C:/Users","D:/","E:/"]     
        if osname == 'posix':
            searchpaths = ["/","/usr"]   
            
        songs = Songs.FindSong(songextensions,searchpaths)
        Songs.upload_to_collection(songs)
        return True

if __name__ == "__main__" :
       Songs()