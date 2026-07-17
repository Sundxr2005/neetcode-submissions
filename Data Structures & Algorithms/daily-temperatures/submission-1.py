class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    new.append(j - i)
                    break
            else:
                new.append(0)
        return new

        