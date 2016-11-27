from math import *
import io

epsilon = exp(-5)
delta = exp(1)*0.0001

val_a = []
val_b = []
num_buckets = ceil(exp(1)/epsilon)
word_counts = {}
num_of_hash_params = 0
n = 0

# hash_params
hash_params = open("hash_params.txt")
for lines in hash_params:
	# print(lines)
	lines = lines.strip()
	lines = lines.split("\t")
	val_a.append(int(lines[0]))
	val_b.append(int(lines[1]))
	num_of_hash_params = num_of_hash_params + 1
hash_params.close()

# initial
for i in range(num_of_hash_params):
	word_counts[i] = {}
	for j in range(num_buckets):
		word_counts[i][j] = 0

# hash function
def hash_fun(a, b, p, n_buckets, x):
	y = x % p
	hash_val = (a * y + b) % p
	return hash_val % n_buckets

def hash_funs(a, b, x):
	return hash_fun(a, b, 123457, num_buckets, x)


# read word
words_stream = open("words_stream_tiny.txt")
for word in words_stream:
	word = int(word.strip())
	if n < word:
		n = word
	for i in range(num_of_hash_params):
		h = hash_funs(val_a[i], val_b[i], word)
		word_counts[i][h] = word_counts[i][h] + 1

words_stream.close()

def word_fre(word):
	min_fre = word_counts[0][hash_funs(val_a[0], val_b[0], word)]
	for x in range(1,num_of_hash_params):
		fre = word_counts[x][hash_funs(val_a[i], val_b[i], word)]
		if fre < min_fre:
			min_fre = fre
	return min_fre
# result = open("result.txt", "wb")
for x in range(1,n+1):
	# result.write(str(x) + "\t" + str(word_fre(x)) + "\n")
	print("%d\t%d" % (x, word_fre(x)))
# result.close()