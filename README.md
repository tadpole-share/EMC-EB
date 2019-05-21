# Survival branch 
Esther Bron - e.bron@erasmusmc.nl

Different types of predictions:
- for the final TADPOLE dataset (a,b) or for the leaderboard dataset. (c,d)
- based on multiple timepoints (longitudinal data) (a,c) or one timepoint (crossectional data) (b,d)

## a. Final submissions longitudinal data: 

1. script_dataPrep.py with setting: leaderboard = 0
2. TADPOLE_SVR.py with settings: leaderboard = 0, d3 = 0 

Inputs: TADPOLE_D1_D2.csv, D4_dummy.csv (Fake reference standard to test validity of output), FeatureIndices.csv (Result of feature selection performed in R)
Intermediates: LongTADPOLE.csv (Training and Test data),  ToPredict_D2.csv (IDs van test set)
Outputs: TADPOLE_Submission_EMC-EB1.csv

## b. Final submissions crossectional data: 

1. script_dataPrep_D3.py 
2. TADPOLE_SVR.py with settings: leaderboard = 0, d3 = 1 

Inputs: TADPOLE_D1_D2.csv, TADPOLE_D3.csv
Intermediates: LongTADPOLE_D3.csv (Test set), LongTADPOLE_D1.csv (Training set)
Outputs: TADPOLE_Submission_EMC-D3-EB1.csv

## c. Leaderboard submissions longitudinal data: 

1. script_dataPrep.py with setting: leaderboard = 1
2. TADPOLE_SVR.py with settings: leaderboard = 1, d3 = 0 

Inputs: TADPOLE_D1_D2.csv, TADPOLE_LB1_LB2.csv,  TADPOLE_LB4.csv (Reference standard test set), FeatureIndices.csv (Result of feature selection performed in R)
Intermediates: LongTADPOLE.csv (Training and Test data),  ToPredict.csv (IDs van test set)
Outputs: TADPOLE_Submission_Leaderboard_EMC-EB1.csv

## d. Leaderboard submissions crosssectional data: 
Not implemented (leaderboard = 1, d3 = 1).


## My results:

### a. Longitudinal (Ref: D4_dummy.csv)
[[111 120  75]
 [135 106  71]
 [ 96 106  76]]
Diagnosis:
mAUC = 0.503 BAC = 0.496
ADAS:
MAE = 5.368 WES = 4.692 CPA = 0.492
VENTS:
MAE = 8.584e-03 WES = 8.283e-03 CPA = 0.499

### b.  Crossectional D3 (Ref: D4_dummy.csv)
[[ 72 186  48]
 [ 78 198  36]
 [ 62 170  46]]
Diagnosis:
mAUC = 0.513 BAC = 0.520
ADAS:
MAE = 0.947 WES = 0.921 CPA = 0.473
VENTS:
MAE = 9.545e-04 WES = 9.616e-04 CPA = 0.482

### c. Longitudinal leaderboard (Ref: TADPOLE_LB4.csv)
[[194   1   0]
 [ 54  96   0]
 [  6  49  17]]
Diagnosis:
mAUC = 0.840 BAC = 0.901
ADAS:
MAE = 4.541 WES = 4.168 CPA = 0.490
VENTS:
MAE = 3.513e-03 WES = 3.304e-03 CPA = 0.494