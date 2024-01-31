value = "Okay"
count = 0

while value:
    count += 1
    print(count)# 1
    if count == 5:
        break
    else:
        value = 0
        continue
 # 1 gets printed only once. ALl this shows is that the value is set to zero AND ZERO IS FALSE SO IT THE LOOP ACTUALLY CONTINUED BUT THE VALUE WAS ALREADY SET TO ZERO SO IT ENDED