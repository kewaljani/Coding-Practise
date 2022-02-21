def maxNumber(n:int, k:int) ->int:
	i = 0
	while k > 0 and i < 3:
		n_str = str(n)
		tmp = int(n_str[i])
		if tmp == 9:
			i += 1
		else:
			new_n_str = n_str[:i] + str(tmp+1) + n_str[i+1:]
			if int(new_n_str) > n:
				n = int(new_n_str)
				k -= 1
	return n


n = 285
k = 20
print(maxNumber(n,k))