class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for s in operations:
            if s[0] == "+" or s[2] == "+":
                x += 1
            else:
                x -= 1
        
        return x
