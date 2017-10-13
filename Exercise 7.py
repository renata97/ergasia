print ("Choose your words wisely...")
text = raw_input (">>")

words = text.split(" ")

max=0
c=0
for i in words:
        if len(words[c])>=max:
                mword= words[c]
                max=len(words[c])
        c+=1  
      
print (mword)     

end=input("Bye")
   
