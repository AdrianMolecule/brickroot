#from dnachisel import *
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation, ExactPosition
from Bio.SeqRecord import SeqRecord
import os


class Model:
    

    def __init__(self):
        self.forbiddenList:list =list("Initial")
        self.problem:DnaOptimizationProblem
        self.sequenceText:str=""
        self.sequenceLabel:str=""
        self.loadedSequenceFileName:str=""
        self.lastFastaFile:str="" #os.path.dirname(os.path.abspath(__file__))+"\\..\\default.fa"
        self.minGcContent:str=""
        self.maxGcContent:str=""
        self.checkHairpins:int=True
        self.checkGcContent:int=True

    def dump(self):
        s="forbiddenList:"
        # for f in self.forbiddenList:
        #     s+=f
        s.join(self.forbiddenList)
        s+="\nsequenceText:"
        s= s+self.sequenceText if self.sequenceText !=None  else ""
        s= s+"\nsequenceLabel:"
        s= s+self.sequenceText if self.sequenceText !=None  else ""
        s= s+"\nlastFastaFile:"
        s= s+self.lastFastaFile if self.lastFastaFile !=None  else ""
        s= s+"\nminGcContent:"
        s= s+ str(self.minGcContent) if self.minGcContent !=None  else ""
        s= s+ "\ngmaxGcContent:"
        s= s+ str(self.maxGcContent) if self.maxGcContent !=None  else ""
        return s


