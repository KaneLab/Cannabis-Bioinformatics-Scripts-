import os
"""Not that this is no longer the preferred script for use in pulling out Mitochdonria Genes. Instead the chosen file is called MitochondriaGeneFinder.py and can be found in this repository.
"""

#The segment below asks the user for Two files. One with gene locations split into 5 columns, and the otehr for the Fasta file. 

#Input your file names BELOW!!!!

gene_locations = ("genelist.txt")
fasta_file = ("mitochondria.fasta")
newfile = open("NEWFILENAME.txt", "wb")


gene_list = open(gene_locations, 'r')
THINGS = gene_list.read()
firstlist = []

#Splits the file on \r which are the rows
unprorows = THINGS.split("\r")

#Splits every row on the tab. Allowing items to be seperated. Adds every item first list
for item in unprorows:
	firstlist.append(item.split("\t"))

#This segment only adds the gene name, and the two locations to an item called second list



secondlist = []
for item in firstlist:
	secondlist.append(item[2])
	secondlist.append(item[3])
	secondlist.append(item[4])


#Removes the headers from second list so they will not interfere later on
secondlist.remove('combined')
secondlist.remove('start')
secondlist.remove('end ')


counter = 0
thirdlist = []


#while the counter is less than the length of the secondlist/3 (For the three items) 
#make a range of items from 0 - the length of the second list skipping by factors of three
#This basically appends the three items NAME POSITION1 POSITION2 into a new list, thirdlist as a list within a list
#Allowing for easier referance

for things in secondlist:
	while counter <= len(secondlist)/3:
		for i in xrange(0,len(secondlist),3):
			thirdlist.append(secondlist[i:i+3])
			counter += 1





#Officially reads in the stored fasta from the first segment of code. Joins all fasta and gets rid of \n
with open (fasta_file, "r") as myfile:
    data=myfile.read().replace('\n', '')




for pair in thirdlist:
	if pair[1] <= pair[2]:
		total_length  = int(pair[2]) - int(pair[1])
		#Prints the gene name and the locations followed by location in the DNA string. 
		CalculatedLength = len(data[int(pair[1]):int(pair[1]) + total_length])
		ActualGene = data[int(pair[1]):int(pair[1]) + total_length]
		newfile.write(pair[0] + ' ')
		newfile.write(pair[1] + ' ') 
		newfile.write(pair[2] + ' ') 
		newfile.write(str(total_length) + ' ') 
		newfile.write(str(CalculatedLength) + '\n') 
		newfile.write(ActualGene.rstrip("\r") + '' + "\n" + "\n") 
		
	elif pair[1] >= pair[2]:
		compliment = []
		total_length  = int(pair[1]) - int(pair[2])

		#Multiplied numbers be negative one to make python take it in reverse order
		Z = data[-1*int(pair[1]): -1*int(pair[2])]
		newfile.write("Here is a gene on the Neg strand" + ' ')
		newfile.write(pair[0] + ' ')
		newfile.write(pair[1] + ' ')
		newfile.write(pair[2] + ' ')
		newfile.write(str(total_length) + ' ')
		newfile.write(str(len(Z)) + "\n")
		#Had make to a list of the above line to allow for iteration through the refervse sequence and allow for complimentary DNA to be made
		list(Z)
		for item in Z:
			if item == 'A':
				compliment.append('T')
			elif item == 'C':
				compliment.append('G')
			elif item == "G":
				compliment.append("C")
			elif item == "T":
				compliment.append("A")
		Finalized_gene_neg = ''.join(compliment[::-1]) 
		newfile.write(Finalized_gene_neg.rstrip('^M') + "\n" + '\n')


newfile.close()

			
