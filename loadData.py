#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:43:48 2022

@author: furbina
"""

import pandas as pd
import numpy  as np


DataH=pd.read_csv("SolarWind.csv")
DataH.head()
DataH.dtypes
DataH['Ts_Valor'].describe()
