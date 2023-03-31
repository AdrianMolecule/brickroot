"""Utility methods"""
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import sys
from Bio import SeqIO
from Bio import Restriction
from tkinter import *

def loadFasta(fileName:str="default.fa"):
	record:SeqRecord = SeqIO.read(fileName, "fasta")
	print("Fasta record name:%s length:%i Sequence: %s" % (record.id, len(record), record.seq))
	return record

def loadFastas(fileName:str="short.fa"):
	fIn=open(fileName,'r')
	sequenceRecordIterator=SeqIO.parse(fileName, "fasta")
	sequenceRecordList=[]
	for record in sequenceRecordIterator:
		print("Fasta record name:%s length:%i Sequence: %s" % (record.id, len(record), record.seq))
		sequenceRecordList.append(record)
	return 	sequenceRecordList


def printRed(message:str):
	print('\033[1;31m' + message + '\033[0m') 

def checkTranslation( inSeq, outSeq):
	"""Checks the translation of the engineered sequence against the wild-type sequence"""
	myInSeq=SeqRecord(Seq(inSeq))
	myOutSeq=SeqRecord(Seq(outSeq))
	if myInSeq.translate().seq==myOutSeq.translate().seq:
		successFlag=True
	else:
		successFlag=False
	return successFlag
#	

def loadTextFromFile( fileName):
	record=loadFasta(fileName)
	return record.seq, 'id {id} {len}'.format(id =record.id, len=len(record))


def loadListFromFile( fileName):
	f = open(fileName, "r")
	linesList=list()
	for line in f:
		linesList.append(line)
	f.close()
	return 	linesList



 