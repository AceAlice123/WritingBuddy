import random
text="this is a file."
new_text=""
for i in text:
    if (i==" " and random.randint(1,100)<60):
        new_text+=" "
    new_text+=i
print(new_text)