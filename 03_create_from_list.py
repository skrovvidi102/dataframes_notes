import pandas as pd #alias
import functions
data = [1,2,3,4,5]
df3 = pd.DataFrame(data)
functions.print_it('original list', data)
functions.print_it('creating from a list', df3)
# create another dataframe from a list and print it <<< TO DO
data2=['saketh','krovvidi','M00373896']
df123=pd.DataFrame(data2)
functions.print_it('ori',data2)
functions.print_it('new',df123)