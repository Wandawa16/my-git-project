import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset('tips')
#print(data)
plt.figure(figsize=(10,7))
sns.histplot(data['total_bill'],bins=20,color='blue')
plt.title('total bill')
plt.xlabel('total bill')
plt.ylabel('frequency')
plt.show()

plt.figure(figsize=(10,7))
sns.boxplot(x='day',y='tip',data=data ,hue='day' , palette='coolwarm')
plt.title('tips distribution per day')
plt.xlabel('day')
plt.ylabel('tips')
plt.show
plt.figure(figsize=(10,7))
sns.scatterplot(x='total_bill', y='tip', data=data, hue='sex')
sns.regplot( 
    x='total_bill',
    y='tip',
    scatter=False,
    data=data,
    scatter_kws={ 'color':'black','alpha':0.5},
    line_kws={'color':'red', 'linestyle':'--'

    }
   
)
plt.title('bills')
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.show()
