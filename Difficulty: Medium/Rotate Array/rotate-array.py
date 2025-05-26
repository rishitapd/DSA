#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,arr, d):
        n=len(arr)
        d=d%n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        
    def reverse(self,arr,left,right):
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        
            