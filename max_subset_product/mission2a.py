# given the height of a perfectly balanced post-order traversal binary tree h, find the parents of the elements given in the list q
# tree is constructed with elements starting from 1,2,3,...2^h-1

def solution(h,q):

	root = (2**h)-1
	result = [search(root,h,key) for key in q]
	return result

def search(root, h, key):

	if h==1:
		return -1

	right = root-1
	h-=1
	left = root-(2**h)

	if key==left or key==right:
		return root

	return max(search(left, h, key), search(right, h, key))