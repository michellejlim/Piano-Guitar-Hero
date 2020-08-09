

def openMusicFile():
    file = open("musicfile.txt", "r") 
    data=file.readlines()
    music = []
    for line in data: 
        words = line.split()
        music.append(words)
    return music


    