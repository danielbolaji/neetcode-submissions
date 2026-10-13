class Solution:
    def hammingWeight(self, n: int) -> int:
        b = []
        while n > 0:
            b.append(n % 2)
            n = (n // 2)

        b.reverse()

        count = 0

        for i in range(len(b)):
            if b[i] == 1:
                count += 1;
            else:
                pass
        return count
