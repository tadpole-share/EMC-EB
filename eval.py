# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:40:41 2017

For evaluation of a submission
S: results file
R: reference file

@author: Esther
"""

import pandas as pd
from evalOneSubmissionExtended import evalOneSub

# Input files
S = pd.read_csv('./IntermediateData/TADPOLE_Submission_Leaderboard_EMC-EB1.csv')
R = pd.read_csv('./Data/TADPOLE_LB4.csv')

#S = pd.read_csv('./IntermediateData/TADPOLE_Submission_EMC-EB1.csv')
#S = pd.read_csv('./IntermediateData/TADPOLE_Submission_EMC-D3-EB1.csv')
#R = pd.read_csv('./IntermediateData/D4_dummy.csv')

# Evaluation
mAUC, bca, adasMAE, ventsMAE, adasWES, ventsWES, adasCPA, ventsCPA, adasEstim, trueADASFilt = evalOneSub(R,S)

#print mAUC, adasMAE, ventsMAE
print 'Diagnosis:'
print 'mAUC = ' + "%0.3f" % mAUC,
print 'BAC = ' + "%0.3f" % bca
print 'ADAS:'
print 'MAE = ' + "%0.3f" % adasMAE, 
print 'WES = ' + "%0.3f" % adasWES,
print 'CPA = ' + "%0.3f" % adasCPA 
print 'VENTS:'
print 'MAE = ' + "%0.3e" % ventsMAE,
print 'WES = ' + "%0.3e" % ventsWES,
print 'CPA = ' + "%0.3f" % ventsCPA 
