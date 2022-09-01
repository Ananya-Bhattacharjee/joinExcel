# importing the module
import pandas
  
# reading the files
f1 = pandas.read_excel("MTurkjoin.xlsx", sheet_name='Sheet2')
f2 = pandas.read_excel("MTurkjoin.xlsx", sheet_name='Sheet1')
  
# merging the files
f3 = f1[["ResponseId"]].merge(f2[["ResponseId", 
                                         "Q77_1",	"Q77_2",	"Q77_3",	"Q77_4",	"Q77_5", "Q71", "Q74", "Q75", "Q76"
]], 
                                     on = "ResponseId",
                                     how = "left")
  
# creating a new file
f3.to_excel("JoinResults2.xlsx", index = False)