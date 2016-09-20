
* Search for pattern in given DNA sequence using Derivative Boyer Moore(DBM) algorithm. In DBM, search for pattern in encoded DNA sequence without decoding it.In DBM, encode the text by using two bits for each character. We represent each pattern as four encode pattern with corresponding alignment. Split pattern as [Pf(first byte),Pm,Pb(last byte)] and split the text as [Tb(last byte),Tf(first byte)]. First search for Pm in Tf, if found compare Pf and Pb with corresponding text.



//Follow the steps give below

1. It is the implementation of the paper pattern matching in DNA sequence using Derivative Boyer Moore algorithm.
2. open the DerivativeBooyermoore(python) file using python idle and execute it.
