import pandas as pd #alias
import functions
adict = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df2 = pd.DataFrame(adict)
functions.print_it('original dictionary', adict)
functions.print_it('Created from a dictionary', df2)
# create another dataframe from a dictionary and print it <<< TO DO
skdict={'product name':['apple','banana','cherry'],'product price':[5,2,3]}
sake=pd.DataFrame(skdict)
functions.print_it('raw data',skdict)
functions.print_it('new dataframe',sake)