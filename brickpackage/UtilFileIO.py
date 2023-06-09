"""Utility methods"""
from configparser import ConfigParser
from tkinter import messagebox
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Restriction
from dnachisel import AvoidPattern
from brickpackage.Controller import Controller
from tkinter import Text, END
from Bio.SeqFeature import SeqFeature
import os

''' only static methods here. More like a container for utility methods'''
class UtilFileIO:
	def loadFasta(fileName:str="default.fa"):
		record:SeqRecord = SeqIO.read(fileName, "fasta")
		return record

	def loadFastas(fileName:str="default.fa"):
		fIn=open(fileName,'r')
		sequenceRecordIterator=SeqIO.parse(fileName, "fasta")
		sequenceRecordList=[]
		for record in sequenceRecordIterator:
			#print("Fasta record name:%s length:%i Sequence: %s" % (record.id, len(record), record.seq))
			sequenceRecordList.append(record)
		return 	sequenceRecordList

	def checkTranslation( inSeq, outSeq):
		'''Checks the translation of the engineered sequence against the wild-type sequence'''
		myInSeq=SeqRecord(Seq(inSeq))
		myOutSeq=SeqRecord(Seq(outSeq))
		if myInSeq.translate().seq==myOutSeq.translate().seq:
			successFlag=True
		else:
			successFlag=False
		return successFlag	

	def loadTextFromFile( fileName):
		record=UtilFileIO.loadFasta(fileName)
		return str(record.seq), '     {id}       length: {len}'.format(id =record.id, len=len(record))

	def loadListFromFile( fileName):
		f = open(fileName, "r")
		linesList=list()
		for line in f:
			linesList.append(line)
		f.close()
		return 	linesList

	def loadModelFromFile():
		parser:ConfigParser=ConfigParser()
		parser.read(os.path.dirname(os.path.abspath(__file__))+"\\..\\prefs.config")
		Controller.model.lastFastaFile=parser.get("general",'lastFastaFile')	
		if Controller.model.lastFastaFile is not None and not Controller.model.lastFastaFile.strip()=='' :
			text,label=UtilFileIO.loadTextFromFile( Controller.model.lastFastaFile)
			Controller.model.sequenceText=text
			Controller.model.sequenceLabel=label   
		Controller.model.forbiddenList=UtilFileIO.loadListFromFile(os.path.dirname(os.path.abspath(__file__))+"\\..\\default.txt")
		UtilFileIO.verifyForbidden()
		Controller.model.minGcContent=parser.getfloat("general",'minGcContent')	
		Controller.model.maxGcContent=parser.getfloat("general",'maxGcContent')
		print("Loaded Model:",Controller.model.dump())
						
	def saveModelToFile():					  
		# Writing our configuration file to 'example.cfg'
		config = ConfigParser()
		config.read(os.path.dirname(os.path.abspath(__file__))+"\\..\\prefs.config")
		config.set('general', 'minGcContent', str(Controller.model.minGcContent))
		config.set('general', 'maxGcContent', str(Controller.model.maxGcContent))
		config.set('general', 'lastfastafile', str(Controller.model.lastFastaFile))
		configFile= open(os.path.dirname(os.path.abspath(__file__))+"\\..\\prefs.config", 'w') 
		config.write(configFile)
		configFile.close()

	def verifyForbidden():
		for line in Controller.model.forbiddenList:
			ap:AvoidPattern=AvoidPattern(line.strip() +"_site")
			if ap.pattern.name is None:       
				messagebox.showerror("Error in forbidden List",line+" seems to be unknown.\n please doublecheck the spelling")



