text_name = input("Enter file name: ")
if ( len(text_name) < 1 ) : text_name = 'mbox-short.txt'

try:
    text=open(text_name)
except:
    print("Name not valid")
    quit()
    
mail=list()
result=dict()

for line in text:
    if line.startswith("From "):
        words=line.rstrip()
        words=words.split()
        mail.append(words[1])
        
Max=None

for i in mail:
    result[i] = result.get(i,0)+1

for a,b in result.items():
    if Max is None or b>Max:
        Max = b
        name = a
        
print(name,Max)
