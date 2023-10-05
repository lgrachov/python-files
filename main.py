# Python-Files
# A filesystem made in Python
# ---
# codeatbed
filesystem = None
def initFiles():
    filesystem = []
    return True
def createFile(name,val):
    filesystem.append([name,val])
    return filesystem
def createFolder(name,refName,refVal):
    # Generating names like this:
    # refName + ('@'+name)
    createFile(refName + ('@'+name),refVal)
    return filesystem
