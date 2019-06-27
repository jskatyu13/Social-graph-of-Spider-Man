# Social-graph-of-Spider-Man

A data set from the Social Characteristics of the Marvel Universe to create the social graph of Spider-Man in the Marvel Universe(Thank you, Stan Lee! R.I.P.). 

A input file (porgat.txt) which defines the social network was examined in my program. The Spider-Man number(based on “six degrees of separation” concept) for any arbitrary Marvel character is calculated.

In order to create the social graph of Spider-Man, an associate matrix and a collaboration matrix need to be created. The associate matrix is a matrix which contains 0 or 1 to show whether a character is in a comic book. A two-dimensional array was used to represent the associate matrix between character names(character ID) and comic books(book ID). Then, the collaboration matrix was calculated by multipling the associate matrix with the transpose of the associate matrix(as the associate matrix is a 6486* 12942 matrix, therefore the collaboration matrix is a square matrix, 6486*6486). The collaboration matrix is a matrix of integers where each cell(i,j) is a count of the number of comic books in which the pair of characters have jointly appeared. The diagonal contains the counts of the number of comics that each character occurs.
