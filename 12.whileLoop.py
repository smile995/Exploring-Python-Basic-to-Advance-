# write a while loop to print 1-10
i=0
while i<10:
    # print(i)
    i +=1

# use continue statement to skip a part that match will conditions

i = 0
while i < 10:
  i += 1
  if i % 2==0:
    continue
  print(i)
  
# use break statement to dismiss the loop

i = 1
while i < 6:
  print("inside the break",i)
  if i == 3:
    break
  i += 1