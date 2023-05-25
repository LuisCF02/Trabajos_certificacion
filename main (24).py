with open("Experimento.txt","a") as file:
  print("Abierto de otro modo")
with open("Experimento.txt","r") as file:
  ly=file.read()
  for lx in ly:
    print(lx)


