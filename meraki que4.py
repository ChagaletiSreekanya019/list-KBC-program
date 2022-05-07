
file=open("names.txt","w")
file.write("rishab-meerut\nimtiyaz - delhi\nnilima - cochin\nrati - shimla\nayishah - delhi\nkarthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nsarika - delhi\nbalwinder - tokyo\n anoop - delhi\nnand - delhi\n sekhar - delhi\ntrishna - raipur")
file.close()
file=open("names.txt","r")
a=file.readline()
print(a)