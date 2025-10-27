sun_is_shining = True
have_to_work = False
 
print("Should I go to the park?")
answer = sun_is_shining and not have_to_work
 
if answer == True:
    print("Yes!")
else:
    print("No!")