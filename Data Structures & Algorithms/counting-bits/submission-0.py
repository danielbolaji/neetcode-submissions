class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        while n > -1:
            answer.append(bin(n).count('1'))
            n += -1
        answer.reverse()
        return answer