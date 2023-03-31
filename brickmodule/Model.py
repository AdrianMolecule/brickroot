from dnachisel import *
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation, ExactPosition
from Bio.SeqRecord import SeqRecord


class Model:
    

    def __init__(self):
        self.forbiddenList:list =list("Initial")
        self.problem:DnaOptimizationProblem
        self.sequenceText:str=None
        self.sequenceLabel:str=None

    def dump(self):
        print("ForbiddenList:", self.forbiddenList)

