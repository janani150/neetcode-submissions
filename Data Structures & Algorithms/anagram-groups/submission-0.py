class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}

        for char in strs:
            key=''.join(sorted(char))
            
            if key not in freq:
                freq[key]=[]
            
            freq[key].append(char)

        
        return list(freq.values())


        