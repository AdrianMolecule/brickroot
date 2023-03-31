from dnachisel import *
from brickmodule.util import *
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation, ExactPosition
from Bio.SeqRecord import SeqRecord
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

def process(fastaText, dnaString:str, avoidPatternList:list ):
    problem = DnaOptimizationProblem(
        dnaString,
        constraints=[
            #AvoidPattern("ApoI_site"),
            #AvoidPattern("NdeI_site"),
            AvoidPattern("BsaI_site"),
            #EnforceGCContent(mini=0.3, maxi=0.7, window=50),
            #EnforceTranslation()
            #EnforceTranslation(location=(500, 1400))
        ],
        objectives=[CodonOptimize(species='e_coli')] #, location=(500, 1400))]
    )

    # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE

    problem.resolve_constraints()
    #problem.optimize()

    # PRINT SUMMARIES TO CHECK THAT CONSTRAINTS PASS
    #print("initial sequence :"+dnaString)
    # GET THE FINAL SEQUENCE (AS STRING OR ANNOTATED BIOPYTHON RECORDS)
    #print("sequence_before  :"+problem.sequence_before )
    final_sequence = problem.sequence  # string
    #print("final_sequence   :"+final_sequence)
    print("problem.number_of_edits",problem.number_of_edits()) 
    # print("problem.edits as array",problem.sequence_edits_as_array()) 
    # print("problem.number_of_edits as features",problem.sequence_edits_as_features(feature_type="changed codon")) 
    features:list(SeqFeature)=problem.sequence_edits_as_features(feature_type="changed codon")
    fastaText.insert(END,"\n"+problem.sequence) # replace can also be used

    fastaText.tag_config("start", background="white", foreground="red")
    for feature in features:
        print("feature:",feature.location)
        fastaText.tag_add("start", "3."+str(feature.location.start), "3."+str(feature.location.end))
        print("qualif:", feature.qualifiers)
    

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

