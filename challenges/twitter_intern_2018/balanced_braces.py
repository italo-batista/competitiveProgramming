class Stack(object):
    def __init__(self):
        self.q = []
    def top(self):
        if len(self.q) > 0:
            return self.q[-1]
        else:
            return None
    def put(self, i):
        self.q.append(i)
    def get(self):
        if not self.is_empty():
            return self.q.pop()
        else:
            return None
    def print(self):
        print(self.q)
    def is_empty(self):
        return len(self.q) == 0

open_braces = ['(', '{', '[']
closing_braces = [')', '}', ']']        
        
def convert_brace(b):
    if b in open_braces:
        i = open_braces.index(b)
        return closing_braces[i]
    elif b in closing_braces:
        i = closing_braces.index(b)
        return open_braces[i]

def braces(values):
    
    ans = []
    for braces in values:
    
        stack = Stack()
        balanced = True

        for bi in braces:

            if bi in open_braces:
                stack.put(bi)

            elif bi in closing_braces:
                stack_top = stack.get()

                if bi != convert_brace(stack_top):
                    balanced = False
                    break
            
        if balanced and stack.is_empty():
            ans.append("YES")        
        else:
            ans.append("NO")
    
    return ans


if __name__ == '__main__':
	N = int(input())
	values = []	
	for _ in range(N):
		values_item = input()
		values.append(values_item)
		
	res = braces(values)
	print(res)
		
