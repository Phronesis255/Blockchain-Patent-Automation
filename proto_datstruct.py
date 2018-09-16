#Prototype of Block object and Data Structure on the Blockchain
import json
from collections import OrderedDict
import hashlib as hasher
import datetime as date
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        sha = hasher.sha256()
        src = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(src.encode('utf-8'))
        return sha.hexdigest()

obj_list = []
d_struct0 = {
    "p_Holder_ID": None,
    "p_Title": None,
    "p_Abstrct": None,
    "p_Desc": None
}

'''
d_struct0["p_Holder_ID"] = 4598745
d_struct0["p_Title"] = "Creating Schizophrenic Consumers"
d_struct0["p_Abstrct"] = "FDJVNSLVNSLVNSK,VNKLSVBJSMVEMLVJLkvdsjvljsdvjdslv jl;lj sfjlvjlsflvj jds lNVJLDSVLJSVLSJ"
d_struct0["p_Desc"] = "lfvnslvnsknv. dedsjscbsc.\n slvl sv jlv\n slvlbvbjvl"
obj_list.append(d_struct0)
print(d_struct0)
print(json.dumps(d_struct0, indent=2))
d_struct1 = {
    "p_Holder_ID": [],
    "p_Title": [],
    "p_Abstrct": [],
    "p_Desc": []
}
#THE QUESTION BECOMES: A LIST OF SETS, like d_struct0 or this_nodes_transactions or 
# a set of lists like d_struct1 or new_block_data
ord_struct = OrderedDict()
ord_struct["p_Holder_ID"] = None
'''