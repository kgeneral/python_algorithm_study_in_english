class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        maxLen = max([len(w) for w in words])
        orderMap = {c:i for i,c in enumerate(order)}
        
        for i in range(0, maxLen):
            charsToLexOrder = [orderMap[w[i]] if i < len(w) else -1 for w in words] # -1 : blank 
            
            hasDescOrder = any(charsToLexOrder[i] > charsToLexOrder[i+1] for i in range(len(charsToLexOrder)-1))
            if hasDescOrder == True:
                return False
            
            hasAnyEqual = any(charsToLexOrder[i] == charsToLexOrder[i+1] for i in range(len(charsToLexOrder)-1))
            if hasAnyEqual:
                continue
                
            isAscOrder = all(charsToLexOrder[i] < charsToLexOrder[i+1] for i in range(len(charsToLexOrder)-1))
            if isAscOrder == True:
                return True           
        
        return True
