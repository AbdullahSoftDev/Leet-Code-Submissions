class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = prices[0]
        max = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = prices[i] - low
                if profit > max:
                    max = profit

        result = max
        return result

object = Solution()
print(object.maxProfit([2,4,1]))
