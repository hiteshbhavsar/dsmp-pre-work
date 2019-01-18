# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-','Agender')
gender_count=data['Gender'].value_counts()
#Code starts here 
data.plot.bar()
#print(data)




# --------------
#Code starts here
import pandas as pd
data=pd.read_csv(path)
alignment=data['Alignment'].value_counts()
plt.pie(alignment,labels=alignment.index)


# --------------
#Code starts here
import pandas as pd
sc_df=pd.DataFrame(data,columns=['Strength','Combat'])
#sc_covariance=sc_df.cov()
'''
m_str=sc_df['Strength'].mean()
m_combat=sc_df['Combat'].mean()
dif_combat=sc_df['Strength']-m_str
dif_str=sc_df['Combat']-m_combat
mult=dif_str*dif_combat
summation=sum(mult)
sc_covariance=summation/len(sc_df)
'''
sc_covariance=float('{:2f}'.format(sc_df.Strength.cov(sc_df.Combat)))
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
#print('Covariance ',sc_covariance)
#print('Std strength ',sc_strength)
#print('Std combat',sc_combat)
sc_pearson=float(sc_covariance/(sc_strength*sc_combat))
#print('New Calculated Value ', sc_df.Strength.cov(sc_df.Combat))
#print('-'*21)
ic_df=pd.DataFrame(data,columns=['Intelligence','Combat'])
ic_covariance=ic_df.Intelligence.cov(ic_df.Combat)
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/((ic_intelligence*sc_combat))



# --------------
#Code starts here

total_high=data['Total'].quantile(0.99)
super_best=data[data['Total']>total_high]
super_best_names=super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here
ax_1=plt.boxplot(data['Speed'])
plt.title('Speed')
ax_2=plt.boxplot(data['Intelligence'])
plt.title('Intelligence')
ax_3=plt.boxplot(data['Power'])
plt.title('Power')


