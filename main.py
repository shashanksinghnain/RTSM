# import numpy as np
import pandas as pd 
import seaborn as sns
# import matplotlib.pyplot as plt
# from statsmodels import api as sm
# import statsmodels.formula.api as smf

col_list = ['#ea2c62', '#ff9a8c', '#a20a0a']
sns.set_palette(col_list)

credit_df = pd.read_csv("Credit.csv", index_col=0)

credit_df.Gender = credit_df.Gender.astype('category')
credit_df.Student = credit_df.Student.astype('category')
credit_df.Married = credit_df.Married.astype('category')
credit_df.Ethnicity = credit_df.Ethnicity.astype('category')

active_credit_df = credit_df.loc[credit_df.Balance>0,].copy()



sns_plot = sns.regplot(x='Limit',
           y='Rating',
           data=credit_df,
           scatter_kws={'alpha':0.2},
           line_kws={'color':'black'})




# plt.savefig('plot8_multi.png')

sns_plot.figure.savefig("plot4_limitrating.png")

