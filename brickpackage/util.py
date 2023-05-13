"""Utility methods"""
from configparser import ConfigParser
from tkinter import messagebox
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Restriction
from dnachisel import AvoidPattern
from tkinter import Text, END
from Bio.SeqFeature import SeqFeature
from Bio.SeqUtils import seq3
import os

''' only static methods here. More like a container for utility methods'''
class Util:

	def appendDnaLineWithHighlightedCodons( sequenceTextBox:Text, text:str, features:list=None):
		'''append a new line in themain window a DNA line and colors separately codons assuming 0 start frame'''
		sequenceTextBox.insert(END,"\n"+text) # replace can also be used
		highlightCodons( sequenceTextBox,text)
		print("line count:",sequenceTextBox.count("1.0","end",'lines')[0])
		lastLine=sequenceTextBox.count("1.0","end",'lines')[0]
		if features is not None:
			sequenceTextBox.tag_config("changedBases", background="red", foreground="black")
			for feature in features: # real changes
				#print("feature:",feature.location)
				sequenceTextBox.tag_add("changedBases", str(lastLine)+"."+str(feature.location.start), str(lastLine)+"."+str(feature.location.end))
			myInSeq=SeqRecord(Seq(text))
			transText=seq3(myInSeq.translate().seq)
			sequenceTextBox.insert(END,"\n"+transText) # replace can also be used
			for feature in features:
				sequenceTextBox.tag_add("changedBases", str(lastLine+1)+"."+str(feature.location.start), str(lastLine+1)+"."+str(feature.location.end))
			highlightCodons( sequenceTextBox,transText)
		else:
			highlightCodons( sequenceTextBox,text)

def highlightCodons( sequenceTextBox:Text, text:str):
		print("line count:",sequenceTextBox.count("1.0","end",'lines')[0])
		lastLine=sequenceTextBox.count("1.0","end",'lines')[0]

		sequenceTextBox.tag_config("codonHightlighting", background='#ffffd0', foreground="black") # last 2 yellow
		for co in range(0,len(text),6):
			sequenceTextBox.tag_add("codonHightlighting", str(lastLine)+"."+str(co), str(lastLine)+"."+str(co+3))	

