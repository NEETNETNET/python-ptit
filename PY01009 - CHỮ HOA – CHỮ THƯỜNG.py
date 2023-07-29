s = input()
hoa = 0
thuong = 0
for i in s:
    if i <= 'z' and i >= 'a': thuong +=1
    else: hoa +=1
if hoa > thuong: print(s.upper()) 
else: print(s.lower())