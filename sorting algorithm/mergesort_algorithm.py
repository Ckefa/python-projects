def sort(mlist):
	if len(mlist) > 1:
		mid = len(mlist) // 2
		
		left = mlist[:mid]
		right = mlist[mid:]
		
		left = sort(left)
		right = sort(right)
		
		return   merge_sort(left, right)

	return mlist
	
	
def merge_sort(left, right):
	pure =  []
	i = j = 0
	while i < len(left) and j < len(right):
		a = left[i] > right[j]
		if a:
			pure.append(left[i])
			i += 1
		elif not a:
			pure.append(right[j])
			j += 1
		
	while i < len(left):
			pure.append(left[i])
			i += 1
			
	while j < len(right):
		    pure.append(right[j])
		    j += 1
		
	return pure


mlist = [4, 9, 0, 6, 2, 7, 5, 1]
sorted_list = sort(mlist)
print(sorted_list)

