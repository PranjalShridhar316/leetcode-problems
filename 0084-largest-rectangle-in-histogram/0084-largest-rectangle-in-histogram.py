class Solution:
    def largestRectangleArea(self, heights):
        stack = []          # stores indices
        maxArea = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, h * width)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            maxArea = max(maxArea, h * width)

        return maxArea