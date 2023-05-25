with open("Experimento.txt","a") as file:
  print("Abierto de otro modo")
with open("Experimento.txt","r") as file:
  ly=file.read()
  for line in ly:
    
    wds=line.split()
    if len(wds) <3 or wds[0]!='From':
      continue
    print(wds[2])
    
