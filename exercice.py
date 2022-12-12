#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(n):
	# if n==0:
	# 	return 0
	# else:
	# 	if n==1:
	# 		return 1
	# 	else:
	# 		return get_fibonacci_number(n-2) + get_fibonacci_number(n-1)
	return (
		0 if n == 0 else
		1 if n == 1 else
		get_fibonacci_number(n-2) + get_fibonacci_number(n-1)
	)
def get_fibonacci_sequence(n, seq=[0,1]):
	#return [get_fibonacci_number(i) for i in range(n)]
	# if n == 1:
	# 	return seq[0:1]
	# elif n == 2:
	# 	return seq[0:2]
	# elif len(seq) < n:
	# 	return get_fibonacci_sequence(n, seq + [seq[-1] + seq[-2]])
	# else:
	# 	return seq
	return (
		seq[0:n] if n<=2 else
		get_fibonacci_sequence(n, seq + [seq[-1] + seq[-2]]) if len(seq) < n else
		seq
	)

def get_sorted_dict_by_decimals(d: dict):
	# def decimal_part(number):
	# 	return number % 1.0
	# return sorted(d.values(), key=decimal_part) #la fonction values() renvoie les valeurs du dictionnaires
	return dict(sorted(d.items(), key=lambda x: x[1] % 1.0)) #la fonction items() renvoie une liste de tuples

def fibonacci_numbers(length):
	INIT_VALUES = [0, 1]
	# yield INIT_VALUES[0]
	# if length >= 2:
	# 	yield INIT_VALUES[1]
	for i, elem in enumerate(INIT_VALUES):
		if i >= length:
			break
		yield elem
	last_elems = deque(INIT_VALUES)
	for i in range(len(INIT_VALUES), length):
		fibo_number = last_elems[-1] + last_elems[-2]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number

def build_recursive_sequence_generator(init_values, recursive_def, keep_whole_sequence=False):
	def recursive_generator(length):
		for i, elem in enumerate(init_values):
			if i >= length:
				break
			yield elem
		last_elems = deque(init_values)
		for i in range(len(init_values), length):
			fibo_number = recursive_def(last_elems)
			last_elems.append(fibo_number)
			if not keep_whole_sequence:
				last_elems.popleft()
			yield fibo_number
	return recursive_generator

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]

	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2,1], lambda seq: seq[-1] + seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda seq: seq[-2] + seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda seq: (seq[-seq[-1]]+seq[-seq[-2]]), keep_whole_sequence=True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
