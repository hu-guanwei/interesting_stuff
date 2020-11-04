from random import getrandbits

def approx_cnt(itr):
	cnt = 1
	for _ in itr:
		if getrandbits(cnt) == 0:
			cnt += 1
	return cnt


if __name__ == '__main__':
	from math import log
	n = int(input())
	itr = iter(range(n))
	print(approx_cnt(itr))
	print(log(n, 2))
