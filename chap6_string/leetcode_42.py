height = [0,1,0,2,1,0,1,3,2,1,2,1]

stack = []
volume = 0

for i in range(len(height)):
    # 변곡점을 만나는 경우
    while stack and height[i] > height[stack[-1]]:
        # 스택에서 꺼내기
        top = stack.pop()
        
        if not len(stack):
            break;

        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]

        volume += distance * waters
    
    stack.append(i)

print(volume)