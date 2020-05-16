def reverseSting(text): 
	index = -1

	# Loop from last index untill half of the index	 
	for i in range(len(text)-1, int(len(text)/2), -1): 

		# match character is alphabet or not		 
		if text[i].isalpha(): 
			temp = text[i] 
			while True: 
				index += 1
				if text[index].isalpha(): 
					text[i] = text[index] 
					text[index] = temp 
					break
	return text 
	
# Driver code 
string = "a!!!b.c.d,e'f,ghi"
print ("Input string: ", string) 
string = reverseSting(list(string)) 
print ("Output string: ", "".join(string)) 