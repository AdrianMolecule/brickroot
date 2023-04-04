from dnachisel import *
from brickmodule.util import *
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation, ExactPosition
from Bio.SeqRecord import SeqRecord
from brickmodule.Controller import Controller
from brickmodule.OptimizeDialog import OptimizeDialog
from tkinter import messagebox
#benchling utube tutorial https://www.youtube.com/watch?v=oIcz5fQgtS8&t=865s
# benchling does GC content utidine deplition and set aside region
# s, and Wants to do hairpins and loops
# https://www.benchling.com/blog/education
# need to change launch.json and add  "purpose": ["debug-in-terminal"]  and in launch.json  and settings "justMyCode": false,
# sequenceRecordList=loadFastas()
# for record in sequenceRecordList:
#     print("%s %i" % (record.id, len(record)),"\n")
# sr:SeqRecord=sequenceRecordList[0]
# se:Seq=sr.seq
# #print(dir(se))
# st=se._data
# #print("st:",dir(st))
# s=str(se)
# # print(s,s.__class__)

# apoI = Restriction.NdeI.search(sequenceRecordList[0].seq)
# #        The positions are the first base of the 3' fragment,i.e. the first base after the position the enzyme will cut.
# e:RestrictionType=ApoI

# DEFINE THE OPTIMIZATION PROBLEM
#s="AAAGGTCTCAAAAAA"

def optimize(root, sequenceText):
    # see from Bio import Restriction for name of Retrictions
    d = OptimizeDialog(root, "Optimize Options")
    root.wait_window(d.top)
    constraints:list=list()
    #constraints.append(  AvoidPattern("BsaI_site"))
    constraints.append(AvoidHairpins())
    constraints.append(EnforceTranslation())
    constraints.append(EnforceGCContent(mini=float(Controller.model.minGcContent)/100, maxi=float(Controller.model.maxGcContent)/100, window=50))
    for pat in Controller.model.forbiddenList:
        constraints.append( AvoidPattern(pat.strip() +"_site"))

    #EnforceTranslation(location=(500, 1400))
    problem = DnaOptimizationProblem(
        Controller.model.sequenceText,
        constraints,
        objectives=[CodonOptimize(species='e_coli')] #, location=(500, 1400))]
    )
    # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE
    problem.resolve_constraints()
    #problem.optimize()
    Controller.model.problem=problem
    #print("problem.number_of_edits",problem.number_of_edits()) 
    # print("problem.edits as array",problem.sequence_edits_as_array()) 
    # print("problem.number_of_edits as features",problem.sequence_edits_as_features(feature_type="changed codon")) 
    features:list(SeqFeature)=problem.sequence_edits_as_features(feature_type="changed codon")
    sequenceText.insert(END,"\n"+problem.sequence) # replace can also be used
    sequenceText.tag_config("start", background="white", foreground="red")
    for feature in features:
        #print("feature:",feature.location)
        sequenceText.tag_add("start", "2."+str(feature.location.start), "2."+str(feature.location.end))
        #print("qualif:", feature.qualifiers)
    
    record = problem.to_record(with_sequence_edits=True) # TODO add record id ,record_id=Controller.model.
    changedFileName=Controller.model.lastFastaFile[:-3]+"_with_edits.gb"
    changedFile=open(changedFileName,'w')
    SeqIO.write(record, changedFile, "genbank")
    changedFile.close()
    messagebox.showinfo("Newly generated file "+changedFileName, str(problem.constraints_text_summary())+"\n"+ str(problem.objectives_text_summary()))
        #feature.qualifiers - A dictionary of qualifiers on the feature
    #print(problem.constraints_text_summary())
    #print(problem.objectives_text_summary())
    # final_record = problem.to_record(with_sequence_edits=True)
    # print("final_record"+final_record.seq)
    # from dnachisel import *

    # # DEFINE THE OPTIMIZATION PROBLEM

    # problem = DnaOptimizationProblem(
    #     sequence="AAAGGTCTCAAAAAAAAAAAAAAAAAAA",
    #     constraints=[
    #         AvoidPattern("BsaI_site"),
    #         #EnforceGCContent(mini=0.3, maxi=0.7, window=5),
    #         EnforceTranslation(location=(1, 16))
    #     ],
    #     objectives=[CodonOptimize(species='e_coli', location=(1, 16))]
    # )

    # # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE

    # problem.resolve_constraints()
    # problem.optimize()

    # # PRINT SUMMARIES TO CHECK THAT CONSTRAINTS PASS

    # print(problem.constraints_text_summary())
    # print(problem.objectives_text_summary())

    # # GET THE FINAL SEQUENCE (AS STRING OR ANNOTATED BIOPYTHON RECORDS)

    # final_sequence = problem.sequence  # string
    # final_record = problem.to_record(with_sequence_edits=True)

