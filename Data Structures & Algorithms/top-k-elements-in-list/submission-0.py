class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        #freq1=freq.sorted()
        desc_scores =dict(sorted(freq.items(),key=lambda item: item[1], reverse=True))
        for i in range(k):
            result.append(list(desc_scores.keys())[i])
        
        return result