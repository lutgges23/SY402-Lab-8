import sys, os, hashlib
from datetime import datetime


path = "/"
output = open("output.txt", "w")
filename = []
desired = []
baddir = ["var", "proc", "run", "sys", "tmp", "dev"]
def hashit(f_path, block_size=65536):
    h = hashlib.sha256()
    with open(f_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            h.update(block)
    return h.digest()

for root, d_names, f_names in os.walk(path):
    for f in f_names:
        fullpath = os.path.join(root, f)
        compare = fullpath.split("/")[1]
        try:
            if compare not in baddir:
                desired.append(fullpath)
            else:
                if compare == "var":
                    if "/var/lib" not in fullpath and "/var/run" not in fullpath:
                        desired.append(fullpath)
        except:
            continue

for element in desired:
    try:
        hashedout = hashit(element)
        printFormat = "fullFilePath: {0} \nhash: {1} \nobeservationTime: {2} \n\n".format(element, hashedout, datetime.now())
        output.write(printFormat)
    except:
        continue


#print(desired)

output.close()



