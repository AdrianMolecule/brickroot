from dnachisel import *
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation, ExactPosition
from Bio.SeqRecord import SeqRecord
import os


class Model:
    

    def __init__(self):
        self.forbiddenList:list =list("Initial")
        self.problem:DnaOptimizationProblem=None
        self.sequenceText:str=None
        self.sequenceLabel:str=None
        self.loadedSequenceFileName:str=None
        self.lastFastaFile:str=None #os.path.dirname(os.path.abspath(__file__))+"\\..\\default.fa"

    def dump(self):
        print("forbiddenList:", self.forbiddenList)
        print("sequenceText:", self.sequenceText)
        print("sequenceLabel:", self.sequenceLabel)
        print("lastFastaFile:", self.lastFastaFile)
        print("problem:", self.problem)

    def printDump(self):
        print("forbiddenList:", self.forbiddenList)
        print("sequenceText:", self.sequenceText)
        print("sequenceLabel:", self.sequenceLabel)
        print("lastFastaFile:", self.lastFastaFile)
        print("loadedSequenceFileName:", self.loadedSequenceFileName)
        print("problem:", self.problem)

