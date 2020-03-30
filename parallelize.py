import numpy as np

def permute(permutation, sparse, sig):
	"""
	Applies permutations on the rows of the sparse matrix.
	Returns the first non-zero value in each column (i.e. user) to be appended to the signature matrix (each permutation is a row).
	"""
	index = np.random.permutation(np.arange(np.shape(sparse)[0]))
	return permutation, sparse[index, :].argmax(axis=0)

def similarity(u1, u2, s1, s2, t):
	"""
	The Jaccard index, or Jaccard similarity coefficient, defined as the size of the intersection 
	divided by the size of the union of two label sets, is used to compare set of predicted labels 
	for a sample to the corresponding set of labels in y_true.
	"""
	s1, s2 = set(s1), set(s2)
	u = s1.union(s2)
	i = s1.intersection(s2)
	score = len(i)/len(u)

	# u1 < u2
	u1, u2 = min(u1, u2), max(u1, u2)

	if score >= t:
		return (u1, u2)