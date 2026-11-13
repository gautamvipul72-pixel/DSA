def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i in range(len(temperatures)):
        temp = temperatures[i]
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = dailyTemperatures(temperatures)
print(result)