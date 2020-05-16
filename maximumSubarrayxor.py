def maxSubarrayXOR(arr,n): 
  
    ans = -2147483648
    for i in range(n): 
          
        curr_xor = 0  
        for j in range(i,n): 
          
            curr_xor = curr_xor ^ arr[j] 
            ans = max(ans, curr_xor) 
          
      
    return ans 
arr = [8, 1, 2, 12] 
n = len(arr) 
  
print("Max subarray XOR is ", maxSubarrayXOR(arr, n))