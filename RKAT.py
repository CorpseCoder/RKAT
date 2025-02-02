def checkModules():
    try:
        import keyboard,os,requests
        print("Modules installed already")
    except ModuleNotFoundError as err:
        if "keyboard" in str(err):
            os.run("pip3 install keyboard")
            print("Keyboard module installed")
            checkModules()
        elif "requests" in str(err):
            os.run("pip3 install requests")
            print("Requests module installed")
            checkModules()

checkModules()
