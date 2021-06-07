#Script to Determine if two given rectangles defined by their width, height, and (x, y) coordinates of their top left corner have any intersecting region. 
# Python3 implementation of above problem

# function to find intersection rectangle of given two rectangles.
def FindPoints(x1, y1, x2, y2, 
			x3, y3, x4, y4): 


	#gives the co-ordinates of bottom-right point of intersection 
	x5 = max(x1, x3) 
	y5 = max(y1, y3) 


    #gives the co-ordinates of top-left point of intersection 
	x6 = min(x2, x4) 
	y6 = min(y2, y4) 

	
    #If their is no intersection 
	if (x5 > x6 or y5 > y6) : 
		print("No intersection") 
		return

	print( "(", x5, ", ", y5, ") ", end = " ") 

	print( "(", x6, ", ", y6, ") ", end = " ") 

	#gives the co-ordinates of top-right point of intersection  
	x7 = x5 
	y7 = y6 

	print( "(", x7, ", ", y7, ") ", end = " ") 

    #gives the co-ordinates of bottom-left point of intersection 
	x8 = x6 
	y8 = y5 

	print( "(", x8, ", ", y8, ") ") 

#CASE1
if __name__ == "__main__":
	
	 
	x1 = 0
	y1 = 0
	x2 = 10
	y2 = 8

	 
	x3 = 2
	y3 = 3
	x4 = 7
	y4 = 9

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4) 
#CASE2
if __name__ == "__main__":
	
	 
	x1 = 0
	y1 = 0
	x2 = 12
	y2 = 10

	 
	x3 = 3
	y3 = 4
	x4 = 9
	y4 = 11

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)
#CASE3
if __name__ == "__main__":
	
	 
	x1 = 2
	y1 = 4
	x2 = 12
	y2 = 10

	 
	x3 = 3
	y3 = 4
	x4 = 9
	y4 = 11

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)
#CASE4    
if __name__ == "__main__":
	
	 
	x1 = 4
	y1 = 6
	x2 = 12
	y2 = 10

	 
	x3 = 3
	y3 = 4
	x4 = 9
	y4 = 11

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)   

#CASE5
if __name__ == "__main__":
	
	 
	x1 = 0
	y1 = 0
	x2 = 12
	y2 = 10

	 
	x3 = 1
	y3 = 1
	x4 = 2
	y4 = 2

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)

#CASE6
if __name__ == "__main__":
	
	 
	x1 = 0
	y1 = 0
	x2 = 16
	y2 = 18

	 
	x3 = 3
	y3 = 4
	x4 = 9
	y4 = 11

	
	FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)

