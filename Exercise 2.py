print("please input the number of vehicles for every 10 minutes...")

hours=["16:00 to 16:10","16:10 to 16:20","16:20 to 16:30","16:30 to 16:40","16:40 to 16:50","16:50 to 17:00",
	   "17:00 to 17:10","17:10 to 17:20","17:20 to 17:30","17:30 to 17:40","17:40 to 17:50","17:50 to 18:00",
	   "18:00 to 18:10","18:10 to 18:20","18:20 to 18:30","18:30 to 18:40","18:40 to 18:50","18:50 to 19:00",
	   "19:00 to 19:10","19:10 to 19:20","19:20 to 19:30","19:30 to 19:40","19:40 to 19:50","19:50 to 20:00"]

num=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
	   
for x in range(0, 24):
    num[x] = input("please input the number of vehicles from %s" %hours[x] )

m4 = max( num[0],num[1],num[2],num[3],num[4],num[5])
m5 = max( num[6],num[7],num[8],num[9],num[10],num[11])
m6 = max( num[12],num[13],num[14],num[15],num[16],num[17])
m7 = max( num[18],num[19],num[20],num[21],num[22],num[23])

print ("-------------------------------")
print ("16:00 , %s" %m4)
print ("17:00 , %s" %m5)
print ("18:00 , %s" %m6)
print ("19:00 , %s" %m7)
print ("-------------------------------")

end = input("Hope to see you soon...")
	


	
	
	

