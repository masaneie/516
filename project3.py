import re
f = open("C:/Users/Mina/Desktop/Fati/rejex.txt", "r")
# We open our text file (providing the path and the mode)
string = f.read()
# We use the read () command to read the text file
string = re.sub ("(\w+t)re", r"\1er", string)
# We use rejex to identify all the worde that endwith tre (e.g. metre) and 
# replace the "re" part with  "er"
string= re.sub("(\w+y)se", r"\1ze", string)
# We use rejext to identify all the words that endwith yse (e.g. analyse)
# and replace the "se" part with "ze"
f2 = open("C:/Users/Mina/Desktop/Fati/output.txt","w")
# Finally we open and write our output in another text file (providing the path and mode)
f2.write(string)
