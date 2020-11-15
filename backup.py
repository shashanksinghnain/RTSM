import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels import api as sm
import statsmodels.formula.api as smf

col_list = ['#ea2c62', '#ff9a8c', '#a20a0a']
sns.set_palette(col_list)

credit_df = pd.read_csv("Credit.csv", index_col=0)

credit_df.Gender = credit_df.Gender.astype('category')
credit_df.Student = credit_df.Student.astype('category')
credit_df.Married = credit_df.Married.astype('category')
credit_df.Ethnicity = credit_df.Ethnicity.astype('category')

# credit_df.describe()

# credit_df.head()

# credit_df.describe(include=['category'])


active_credit_df = credit_df.loc[credit_df.Balance>0,].copy()
# active_credit_df.Balance.describe() 

# credit_df['Active'] = np.where(credit_df['Balance']>0, 'Yes', 'No')  
# credit_df.Active.describe()

# numeric_credit_df = credit_df.select_dtypes(include=['int64', 'float64'])
# plt.figure(figsize=(8,8))
# plt.matshow(credit_df.corr(), cmap=plt.cm.Reds, fignum=1)
# plt.colorbar()
# tick_marks = [i for i in range(len(numeric_credit_df.columns))]
# plt.xticks(tick_marks, numeric_credit_df.columns)
# plt.yticks(tick_marks, numeric_credit_df.columns)

# sns_plot = sns.regplot(x='Limit',
#            y='Rating',
#            data=credit_df,
#            scatter_kws={'alpha':0.2},
#            line_kws={'color':'black'},
#            color = "r")

# sns_plot = sns.distplot(active_credit_df.Balance, color="r")

mod0 = smf.ols('Balance ~ Income + Rating + Cards + Age + Education + Gender + Student + Married + Ethnicity', data = credit_df).fit()

active_mod0 = smf.ols('Balance ~ Income + Rating + Cards + Age + Education + Gender + Student + Married + Ethnicity', data = active_credit_df).fit()

mod1 = smf.ols('Balance ~ Income + Rating + Age + Student', data = credit_df).fit()

sns_plot = sns.regplot(x='Limit',
          y='Balance',
          data=active_credit_df,
          line_kws={'color':'black'},
          lowess=True)



# plt.savefig('plot8_multi.png')

sns_plot.figure.savefig("plot13_best.png")

