

__author__ = 'Geoffrey Nyaga'

import sys
sys.path.append('../')
from API.db_API import write_to_db


rhoSL = 0.0023769

write_to_db('rhoSL',rhoSL)


#testing main line 37 replace later
paxWeight = 0
crewWeight = 220
payloadPax = 0


write_to_db('paxWeight',paxWeight)
write_to_db('crewWeight',crewWeight)
write_to_db('payloadPax',payloadPax)






