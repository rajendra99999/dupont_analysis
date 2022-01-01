#!/usr/bin/env python
# coding: utf-8

# In[1]:


class dupont:
    def __init__ (self,sales,ebit,interest,tax,asset,equity):
        self.sales=sales
        self.ebit=ebit
        self.interest=interest
        self.tax=tax
        self.asset=asset
        self.equity=equity
        
    def base_cal(self):
        self.ebt=self.ebit-self.interest
        self.pat=self.ebt-self.tax
        print('ebt is {}, pat is about {}'.format(self.ebt,self.pat))
    
    def pl_analysis(self):
        self.base_cal()
        self.interest_burdan=self.ebt/self.ebit
        self.tax_burdan=self.pat/self.ebt
        self.ebit_margin=self.ebit/self.sales
        print('''profit and loss analysis is follows\n\t interst burden --> {}\n\t tax burdan --> {}\n\t ebit margin --> {}'''
              .format(round(self.interest_burdan,2),round(self.tax_burdan,2),round(self.ebit_margin,2)))
    
    def resource_utilization(self):
        
        ''' it calculate resource utilization level'''
        self.pl_analysis()
        self.npm=self.interest_burdan*self.tax_burdan*self.ebit_margin
        self.ato=self.sales/self.asset
        print('''resource utilization say\n\t net profit margin is {}\n\t and asset turnover ratio is about {} '''
              .format(round(self.npm,2),round(self.ato,2)))
    
    def bs_analysis(self):
        self.resource_utilization()
        self.roa=self.npm * self.ato
        self.leverage=self.asset/self.equity
        print('''balance sheet analysis give information like\n\t return on asset is about{}\n\t company leverage is {} time'''
             .format(round(self.roa,2),round(self.leverage,2)))
    
    def investor_return(self):
        self.bs_analysis()
        self.roe=self.roa*self.leverage
        print('return on equity for given data is {}'.format(round(self.roe*100,2)))


# In[ ]:




