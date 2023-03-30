#!/usr/bin/env python
# coding: utf-8

# In[270]:


'''The client would like Govini's help to illuminate 
what the Department actually spent on major GCS programs, specifically, 
the Abrams tank (e.g., M1A1), Bradley fighting vehicle (e.g., M2A1), and 
Stryker armored personnel carrier (e.g., M1130). The client wants an analysis of 
FY16 through FY20 federal contract data for these programs that summarizes prominent 
vendors, funding/contracting offices, agencies, and outlines of key technologies, 
products, and services acquired. Additionally, the client would like to understand 
what future acquisitions for each of these programs may look like given where they 
are in their life cycles, and what potential risks may be associated with the 
management of the programs. 

Your response should include, but is not limited to, the following elements:
1) Solutions to the following pain points the client has previously encountered in their data, including:
●	Vendor name normalization
●	Misidentified or unidentified GCS contracts and vendors
2) Assessment of spending trends, key technologies, programs, vendors, and any other elements you found most interesting about the market (e.g., current acquisition life cycle status of the GCS programs and what it means for future investments; or past/future federal budget alignment within each program). This assessment can utilize external sources to supplement findings in the data.* 
3) The assessment should include a conclusion with key takeaways and one or two interesting insights that the client can use to inform their acquisition decisions.
4) Commented-code or a short summary of methodology used to clean/normalize, organize, and/or transform the data. 
'''



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv 

gv_df = pd.read_csv("ground_vehicles.csv")


gv_df['Vendor  Name'].fillna('', inplace=True)


gv_df.loc[gv_df['Vendor  Name'].str.contains('Stryker'), 'Vendor  Name'] = 'StrykerCO.'

gv_df.loc[gv_df['Vendor  Name'].str.contains('Bradley'), 'Vendor  Name'] = 'BAE Systems'

gv_df.loc[gv_df['Vendor  Name'].str.contains('Abrams'), 'Vendor  Name'] = 'R Abrams'



gv_df['Fiscal Year'].fillna(0, inplace=True)
gv_df['Fiscal Year'] = gv_df['Fiscal Year'].astype(int)

year = 2021

mask = gv_df['Fiscal Year'] == year

dates_2021 = gv_df.loc[mask]


print(dates_2021)
    



# In[ ]:




