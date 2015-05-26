#This program takes in multiple gene files in fasta format for a few species. It then goes threw and takes each fasta formatted file and concatenatenates them end to end. The output file is called ConcatinatedGenes.txt. The only thing you need to change in this program is the path2file. The path2file should contain ONLY the genes you want to concatenate and this file.
#This Script was written by Pablo Mendieta an Undergradutae in the Nolan Kane lab. This script is free to use but citation  
import os, re

path2files = "/Users/Pablo/Desktop/Code/Python_Scripts/DaniellaTest"


Files4Parsing = []

def FileFinder(path):
	possibleFile = os.listdir(path)
	for item in possibleFile:
		if str(item).endswith('.fas'):
			Files4Parsing.append(item)


Gene_order = []

#The below section was proabbly the hardest to write. I ended up makign a enw list from the list of all sequences and used the join function to keep adding sequence to itself.

def FileParser(listoffiles):
	Filecounter = 0
	FinalFileCount = len(listoffiles)
	GeneName = []
	GeneAlignment = []
	GenePairedAlignemtn = []

	for Filecounter, item in enumerate(listoffiles):
		#print Filecounter
		if FinalFileCount >= Filecounter:
			Gene_order.append(item)
			with open(item, 'r') as f:
				#print f
				for line in f:
					#print len(line)
					if ">" in line:
						RegexGroup = re.match(r"(>[A-Za-z]*)", line)
						#print RegexGroup.group()
						GeneName.append(RegexGroup.group().replace('\n', '').replace("\r", ''))
					else:
						GeneAlignment.append(line.replace('\n', '').replace("\r", ''))
	microcount = 0	
	for seq in GeneAlignment:
		if (len(GeneName)/FinalFileCount) > len(GenePairedAlignemtn):
			GenePairedAlignemtn.append(seq)
		elif len(GeneName)/FinalFileCount <= len(GenePairedAlignemtn) :
			GenePairedAlignemtn.append(''.join(GenePairedAlignemtn[microcount] + seq))
			microcount += 1
	
	FinalCleanedAlignment = (GenePairedAlignemtn[-(len(GeneName)/FinalFileCount):])
	SingleCopyOfGeneName = GeneName[0:(len(GeneName)/FinalFileCount)]
	FinalDict = dict(zip(SingleCopyOfGeneName, list(FinalCleanedAlignment)))	
	
	FileWriter(FinalDict)
				


glblCounter = 0



					
	

FileFinder(path2files)	
FileParser(Files4Parsing)	
print Gene_order	
