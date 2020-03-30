# LSH
Local sensitive hashing on movies seen by users.

## Objective
In this assignment, we are provided with a file (user_movie.npy) consisting of about 65 million rows and 2 columns, each row reflecting the relation: <user_id, movie_id> (i.e. user x watched movie y). In total, there are 103703 unique users, and 17700 unique movies. This data comprehends an extract from the Netflix challenge. 

The aim of this work is to find, with the help of LSH (Local Sensitive Hashing), pairs of users whose jaccard similarity is higher than 0.5.

Here, we resort to LSH instead of the brute-force search to find the aforementioned pairs of users since the latter would force us to calculate the Jaccard similarity score for about 5.377 x 10<sup>9</sup> pairs (i.e. about 5 billion pairs), which would be too expensive.

Read the **lsh.ipynb** file for a complete and exhaustively commented protocol on how to apply LSH on this type of data.
