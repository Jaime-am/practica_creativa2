import os

os.system("/usr/local/bin/python -m pip install --upgrade pip")
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
os.system("pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")
fin = open("./practica_creativa2/bookinfo/src/productpage/requirements.txt", "r")
for line in fin:
    os.system("pip install "+line)
    os.system("pip3 install "+line)
fin.close()
os.system("pip3 install flask")
