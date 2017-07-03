from scipy.io import arff
from optparse import OptionParser
import numpy as np
import pandas as pd




##########################parser = OptionParser()
parser = OptionParser()
parser.add_option("-i", "--iputArffFile", dest="ifile")
parser.add_option("-o", "--outputFile", dest="ofile")

(options, args) = parser.parse_args()
data, meta = arff.loadarff(options.ifile)


# convert arff to Dataframe with pandas
dataset = pd.DataFrame(data)

#################################
#       6. Correlation between attributes                 #
###########################################################
def removeHCorrAtt(df_corr,dataset,cutoff):
    #create a mask to ignore self-
    mask = np.ones(df_corr.columns.size) - np.eye(df_corr.columns.size)
    df_corr = mask*df_corr

    drops = []
    #loop through each variable
    for col in df_corr.columns.values:
        #if we've already determined to drop the current variable, continue
        if np.in1d([col], drops):
            continue

        #find all the variables that are highly correlated with teh current variable
        # and add them to the drop list
        corr = df_corr[abs(df_corr[col]) > cutoff].index
        drops = np.union1d(drops,corr)
        datasetNew = dataset.copy()
        datasetNew.drop(drops,axis=1, inplace=True)
    return datasetNew,drops



#calculate the correlation matrix (ignore survived and passenger id field)
pd.set_option('display.width',100)
pd.set_option('precision', 3)
df_corr = dataset.corr(method='spearman')
datasetNew,drops=removeHCorrAtt(df_corr,dataset,0.98)
print ("nDropping", drops.shape[0], "highly correlated features(0.98).\n", drops)
datasetNew.to_csv(options.ofile, index = False)
