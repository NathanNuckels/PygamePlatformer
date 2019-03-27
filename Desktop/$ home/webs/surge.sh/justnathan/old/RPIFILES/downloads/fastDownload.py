def imports(a):
    global data
    with open(a,"r+") as file:
        data=file.read()
def exports(a,var):
    with open(a,"w+") as file:
        file.write(var)
def copyfiles(a,b):
    imports(a)
    exports(b,data)
data=""
print("file names do not include stuff aftr the dot")
print("extention is what you want the stuff after the dot to be")
print("name = video\nextention = mp4")
print("video.MPY -> video.mp4")
name=input("><FILENAME>")
copyfiles(name+".MPY",name+input("><EXTENTION>"))
