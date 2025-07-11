# Last updated: 7/10/2025, 11:09:48 PM
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        res = []

        while i < len(encoded1) and j < len(encoded2):
            v1,f1 = encoded1[i]
            v2,f2 = encoded2[j]

            prod = v1 *v2
            freq = min(f1,f2)

            if res and res[-1][0] == prod:
                res[-1][1]+= freq
            else:
                res.append([prod,freq])

            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            
            if encoded1[i][1]== 0:
                i +=1
            
            if encoded2[j][1] == 0:
                j +=1
        return res