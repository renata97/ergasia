print ("Welcome!")

print ("Type 'start' if you want to begin")

a=raw_input(">>")
       
if a=="start":
    print ("================================================================")
    ret=0
    
    while a!= "end":   
        print ("Please insert the ammount of sheep that returned...otherwise type 'night' to proceed to the next night or 'end' to end the session...")
        a=raw_input(">>")
        if a=="night":
            ret=0
        elif a!="end":
            ret+=int(a)
        

print ("================================================================")
print ("Now...how many sheep do you recall in the beggining?")
total=int(raw_input(">>"))

dif=total-ret
print ("You are missing %d sheep!" %dif)

end=input("Hope to see you soon!")

