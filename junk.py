
from brickpackage.Util import *
from brickpackage.process import *
 

b:AvoidPattern=AvoidPattern("BsaI_site")
print(b.__class__)

x:AvoidPattern=AvoidPattern("XXXI_site")

print( b.pattern.name)
print( x.pattern.name)
print( b.shorthand_name)
print( x.shorthand_name)
print( b.pattern)
print( x.pattern)
# shorthand_name = "no"  # will appear as, for instance, @no(BsmBI_site)
# pat = SequencePattern.from_string(line)                     
# print(ap)
# print(isinstance(pat, AvoidPattern))
# # try:
# #     print(pat.enzyme_site) 
# # except AttributError:           
# #     messagebox.showEror("Error","unknown enzyme: "+listString)
# #     return