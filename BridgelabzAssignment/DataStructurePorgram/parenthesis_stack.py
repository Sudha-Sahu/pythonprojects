# from stack import Stack


# function to check if brackets are balanced
def check_parenthesis_balanced(expr):
	"""Desc -> Take an Arithmetic Expression such a (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used
	to order the performance of operations. Ensure parentheses must appear in a balanced fashion."""

	stack = []
	open_paren = ["(", "{", "["]
	close_paren = [")", "}", "]"]
	# Traversing the Expression
	for char in expr:
		if char in open_paren:
			stack.append(char)
		else:
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == close_paren:
				return False

	# Check Empty Stack
	if stack:
		return False
	return True


if __name__ == "__main__":
	exprs = input("enter the parenthesis expression : ")

	# Function call
	if check_parenthesis_balanced(exprs):
		print("Stack is Balanced")
	else:
		print("Stack is not Balanced")
'''
#obj = Stack()


def check_stack(expr):
	open_paren = ["(", "{", "["]
	close_paren = [")", "}", "]"]
	# Traversing the Expression
	for char in expr:
		if char in open_paren:
			obj.push_element(char)
		else:
			if not stack:
				return False
			current_char = obj.pop_element()
'''
