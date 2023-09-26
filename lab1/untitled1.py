#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:57:52 2023

@author: Hp
"""

import pandas as pd
import matplotlib.pyplot as plt


# read the csv file
sales = pd.read_csv('yearly_sales.csv')

# examine the imported dataset
sales.head()
sales.describe()

# plot num_of_orders vs. sales
sales.plot(x='num_of_orders', y='sales_total', style='o')