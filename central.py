import subprocess

print("hola")
ejecuto = int(input())

if ejecuto == 1 : #instalacion
    subprocess.run(["pip3", "install", "python3"])
    subprocess.run(["pip3", "upgrade", "python3"])
