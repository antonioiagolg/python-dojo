# ginortS

* This is a good one. First thing I thought was the ASC table. Looking into the table, the lowerst values are the numbers, follwing by the upper case characteres and last the lower case characteres. This is basically the reversed order the challenge is asking for. The next step is to deal with the odd and even numbers.
* To make the odd numbers to be sorted first, I subtracted the code by 10, so the highest odd number, 9, will be lower than the lowest even number, 0.
* I prepared a key function to sort by the asc code, with the custon number sorting, and also a group key function to create the groups based on the lower, upper and number cases.
* First I sorted the word, then I created the groups, with keys based on the ordering requested by the challenge (l0wercase group -> key 0, upper case group -> key 1 and numbers -> key 2)
* I sorted the groups based on the key, and I have now the brute answer. Thew last step is to iterate over the groups, and create the final result as string to print.
