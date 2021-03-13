import os
new = '\n'
def main():
    SongTypes = []
    for file in os.listdir('./Song_Type/'):
        if ".css" not in file:
            SongTypes.append(file)

    for SongType in SongTypes:
        Songs = []
        for song in os.listdir('./Song_Type/'+SongType+"/songs"):
            Songs.append(song)
        create_song_html(Songs,SongType)
        create_songs_html(SongType,Songs)

def create_song_html(Songs,SongType):
    index = 0
    for song in Songs:
        newName = song.replace("_"," ")
        newName = newName.replace(".mp3","")
        f = open("./Song_Type/"+SongType+"/"+song.replace(".mp3","")+".html", "w", encoding="utf-8")
        f.write("""<!DOCTYPE html>"""+new)
        f.write("""<html lang="en"> """+new)
        f.write(""" <head>"""+new)
        f.write("""<meta charset="UTF-8"> """+new)
        f.write("""<meta name="viewport" content="width=device-width, initial-scale=1.0">"""+new)
        f.write("<title>"+newName+"</title>"+new)
        f.write(""" <link type="text/css" media="all" href="../song.css" rel="stylesheet">"""+new)

        f.write(
            '<script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/'+SongType+'/playlistAll.html"}</script>' + new)

        # if SongType == "English":
        #     f.write(""" <script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/English/playlistAll.html"}</script>""" + new)
        # if SongType == "Chinese":
        #     f.write(""" <script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/Chinese/playlistAll.html"}</script>""" + new)
        # if SongType == "Electronica":
        #     f.write(""" <script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/Electronica/playlistAll.html"}</script>""" + new)
        # if SongType == "Japanese":
        #     f.write(""" <script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/Japanese/playlistAll.html"}</script>""" + new)
        # if SongType == "Korean":
        #     f.write(""" <script type="text/javascript">function playlistThis() {window.location.href = "http://www.cyberpunk-studio.com/Song_Type/Korean/playlistAll.html"}</script>""" + new)

        f.write(""" </head>"""+new)
        f.write(""" <body>"""+new)
        f.write(""" <div class="box">"""+new)
        f.write("""<div class="header"><h1> <a href="http://www.cyberpunk-studio.com/Starter.html">音乐分享 <br>Daily Music</a> </h1></div>"""+new)
        f.write(""" <div class="search">"""+new)
        f.write(""" <a href="https://www.baidu.com/" target=”_blank”><img class="baidu" src="../baidu.png" alt=""></a>"""+new)
        f.write(""" <a href="https://www.google.com/" target=”_blank”><img class="google" src="../google.png" alt=""></a>"""+new)
        f.write(""" <a href="https://www.bing.com/" target=”_blank”><img class="bing" src="../bing.png" alt=""></a>"""+new)
        f.write(""" </div>"""+new)
        f.write(""" </div>"""+new)
        f.write(' <h1 class="title">'+newName+'</h1>'+new)
        f.write("""<div class="player"> """+new)
        f.write(""" <audio controls="controls">"""+new)
        f.write('<source src="./songs/'+song+'" type="audio/mpeg">'+new)
        f.write('<embed height="100" width="100" src="./songs/'+song+'" />'+new)

        f.write(""" </audio>"""+new)
        f.write(""" </div>"""+new)
        f.write(""" <div class="container">"""+new)
        f.write('<iframe src="https://www.bing.com/search?q='+newName+'" width="80%" height="600" style="border:none;"></iframe>'+new)
        f.write(""" <div class="form">"""+new)
        f.write(""" <button class="button" type="submit" id="login-button" onclick="location.href='./"""+Songs[index-1].replace(".mp3","")+""".html'">上一首 <br>Previous song</button>"""+new)
        f.write("""<button class="button" type="submit" id="login-button" onclick="return playlistThis()">返回此歌单 <br>Go to this Playlist</button>"""+new)
        try:
            f.write("""<button class="button" type="submit" id="login-button" onclick="location.href='./"""+Songs[index+1].replace(".mp3","")+""".html'">下一首 <br>Next song</button>"""+new)
        except IndexError:
            f.write("""<button class="button" type="submit" id="login-button" onclick="location.href='./"""+Songs[0].replace(".mp3","")+""".html'">下一首 <br>Next song</button>"""+new)

        f.write(""" </div>"""+new)
        f.write(""" </div>"""+new)
        f.close()
        index += 1

def create_songs_html(SongType,Songs):
    f = open("./Song_Type/" + SongType + "/playlistAll.html", "w", encoding="utf-8")
    f.write("""<html>""" + new)
    f.write("""<head>""" + new)
    f.write("""<meta charset="UTF-8">""" + new)
    f.write("""<meta name="viewport" content="width=device-width,initial-scale=1">""" + new)
    f.write("""<title>音乐分享  Music Share</title>""" + new)
    f.write("""<link type="text/css" media="all" href="../playlist.css" rel="stylesheet">""" + new)
    f.write("""</head>""" + new)
    f.write('<div class="container"><h1>Playlist of '+SongType+' Songs</h1> </div>')
    # if SongType == "English":
    #     f.write("""    <div class="container"><h1>英文歌单 <br> Playlist of English Songs</h1> </div>""" + new)
    # if SongType == "Chinese":
    #     f.write("""    <div class="container"><h1>中文歌单 <br> Playlist of Chinese Songs</h1> </div>""" + new)
    # if SongType == "Electronica":
    #     f.write("""    <div class="container"><h1>电音歌单 <br> Playlist of Electronica Songs</h1> </div>""" + new)
    # if SongType == "Japanese":
    #     f.write("""    <div class="container"><h1>日语歌单 <br> Playlist of Japanese Songs</h1> </div>""" + new)
    # if SongType == "Korean":
    #     f.write("""    <div class="container"><h1>韩语歌单 <br> Playlist of Korean Songs</h1> </div>""" + new)

    f.write("""<div class="list">""" + new)
    f.write("""<table>""" + new)
    for song in Songs:
        f.write('<tr><td><a href="./'+song.replace(".mp3",".html")+'">'+song.replace("_"," ").replace(".mp3","")+"</a></td></tr>"+new)

    f.write("""</table>""" + new)
    f.write("""</div>""" + new)
    f.write("""</body>""" + new)
    f.write("""</html>""" + new)
    f.write("""""" + new)



if __name__ == '__main__':
    main()

