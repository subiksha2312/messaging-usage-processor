
# Messaging Usage Processor
# Developed by Subiksha Suresh, NIT Trichy, 3rd Sem EEE

# Problem Statement - Oracle CX Marketing Product team gets SMS, MMS,
# Mobile App Messaging usage volumes in different CSV files. These
# CSV files have different data columns.
# This file reads all the CSV files in a given directory and it transforms
# all of those files into a standard format (standard set of columns)
# consolidates data across all of the CSV files into one single CSV file output

import pandas as pd
import glob
import os

path = os.getcwd()
usage_files = glob.glob(os.path.join(path, "csvfiles", "*.csv"))

outData = pd.DataFrame(columns = ['gsiSubId','Tenant','Usage','CHANNEL','SVCTYPE'])

for uFile in usage_files:

    print("Processing File - ", uFile)

    inputData = pd.read_csv(uFile, usecols = ['gsiSubId','Tenant','Usage'])

    # As of now, this works only on Unix based OS. Need to refactor this to work on Windows as well
    fName = uFile.split("/")[-1]
    channelName = fName.split("_")[0]
    svcType = fName.split("_")[1].split(".")[0]

    inputData["CHANNEL"] = channelName
    inputData["SVCTYPE"] = svcType
    keep_col = ['gsiSubId','Tenant','Usage','CHANNEL','SVCTYPE']

    outData = outData.append(inputData[keep_col], ignore_index = False)


outData.to_csv("usage.csv", index=False)
