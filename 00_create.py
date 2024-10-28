import pandas as pd #alias
import functions
df1 = pd.DataFrame()
functions.print_it('Empty dataframe', df1)
#creating from a dictionary
adict = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
df2 = pd.DataFrame(adict)
functions.print_it('original dictionary', adict)
functions.print_it('Created from a dictionary', df2)
#creating from a list
data = [1,2,3,4,5]
df3 = pd.DataFrame(data)
functions.print_it('original list', data)
functions.print_it('creating from a list', df3)
# creating from a list of lists
data = [['Alex', 10], ['Bob', 12], ['Ali', 13]]
df4 = pd.DataFrame(data)
functions.print_it('original list of lists', data)
functions.print_it('creating from a list of lists', df4)
df5 = pd.DataFrame(columns=['column1','column2'], 
                   index=[x for x in range(11,21)], 
                   data=[(x, 2) for x in range(20,30)])
functions.print_it('Two columns and 10 rows', df5)
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades_df = pd.DataFrame(grades_dict)
grades_df.index = ['test1', 'test2', 'test3']
functions.print_it('Dictionary entries', grades_df)
# Creating a dictionary with produce items and quantities in two different carts
data = {
    'Produce Item': ['Apples', 'Bananas', 'Oranges'],
    'Cart_1': [7, 15, 15],
    'Cart_2': [8, 12, 'NaN']
}
produce_df = pd.DataFrame(data)
functions.print_it('Dictionaries to:', produce_df)

