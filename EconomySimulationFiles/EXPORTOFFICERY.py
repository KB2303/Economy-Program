###############
import random #
import math   #
import os     # 
###############

#######################ALL STATISTICS ACCURATE AS OF 5/12/22, SOME APPLIED FROM 2021 DATA FROM OECD.
random.seed
Year=1960
MIGRATIONPERCENT=0.03
VAT=0.05
EXPORTS=207069000000
IMPORTS=219713000000
BALANCE=EXPORTS-IMPORTS
POPULATION=67330000000#2021
WORKINGPOPULATION=round(0.485*POPULATION,2)
LABOURFORCE=round(0.821*WORKINGPOPULATION,2)
UNEMPLOYED=WORKINGPOPULATION*0.046
WORKFORCEPRODUCTIVITY=0.7724
GDP=LABOURFORCE*WORKFORCEPRODUCTIVITY