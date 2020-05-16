def isPalindrome(string: str, 
                 low: int, high: int): 
    while low < high: 
        if string[low] != string[high]: 
            return False
        low += 1
        high -= 1
    return True 
def allPalPartUtil(allPart: list, currPart: list,  
                   start: int, n: int, string: str): 
  
    if start >= n: 
         
        x = currPart.copy() 
  
        allPart.append(x) 
        return
  
    for i in range(start, n):
        if isPalindrome(string, start, i): 
  
            currPart.append(string[start:i + 1]) 
  
            allPalPartUtil(allPart, currPart,  
                            i + 1, n, string) 
  
            currPart.pop() 

def allPalPartitions(string: str): 
  
    n = len(string) 
 
    allPart = [] 

    currPart = [] 

    allPalPartUtil(allPart, currPart, 0, n, string) 
    for i in range(len(allPart)): 
        for j in range(len(allPart[i])): 
            print(allPart[i][j], end = " ") 
        print() 
  
# Driver Code 
if __name__ == "__main__": 
    string = "nitin"
    allPalPartitions(string) 