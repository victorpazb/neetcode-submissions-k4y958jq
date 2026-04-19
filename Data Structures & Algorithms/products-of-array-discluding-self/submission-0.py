class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = []
        #nums = [1,2,4,6]
        i = 1

        while(len(output_array) < len(nums)):
        
            j = i - 1
    
            output = 1

            #print(nums[:j])
            for num in nums[:j]:
                output *= num 

            #print(output)

            output2 = 1
            #print(nums[i:])
            for num in nums[i:]:
                output2 *= num 


            output_array.append(output2*output)
            #print(output_array)
            #print("=================")

            
            i += 1
            
        return output_array
                