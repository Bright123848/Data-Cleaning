# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:57:15 2025

@author: BrightBwayo
"""

import streamlit as st
import pandas as pd
import numpy as np
import Function as fx

st.subheader('My Data Cleaning App')

data = pd.read_excel('Lyamujungu_August_Data (1).xlsx')

df = fx.Clean(data)

st.write(df.shape)
st.write(df.head())

col1, col2, col3 = st.columns (3)
with col1:
    #show loan amount
    st.write('Loan_amount')
    amount = df['Loan_amount'].sum()
    st.write(amount)
    
with col2:
    #Show Number of Loans
    number = df['Borrower_ID'].count()
    st.metric('Number of youths is:',number)  
    
    
    
    
    
    
    
    
    


#show loan amount
st.write('Loan_amount')
amount = df['Loan_amount'].sum()
st.write(amount)

#Show Number of Loans
st.write('Number of Loans')
number = df['Borrower_ID'].count()
st.write(number)

#Show Number of Youth
st.write('Number of Youths')
mask = df['Age']<=35
youths = df[mask]['Borrower_ID'].count()
st.write(youths)


#Show Number of Youth
st.write('Number of Women')
mask = df['Gender']=='Female'
women = df[mask]['Borrower_ID'].count()
st.write(women)



#Show Number of Young Women
st.write('Number of Young Women')
mask = (df['Gender']=='Female')&(df['Age']<=35)
youngwomen = df[mask]['Borrower_ID'].count()
st.write(youngwomen)


df.to_excel("data")