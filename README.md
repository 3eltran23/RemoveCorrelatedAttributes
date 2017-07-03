# RemoveCorrelatedAttributes
This program remove higlhy-correlated attributes from a dataset(arff file). 


To remove highly correlated descriptors the procedure is as follows: for each pair of descriptors, the Spearman's correlation coefficient $$\rho$$ is measured.  The pairs of descriptors with $$\rho$$ value greater than 0.98 is depurated by removing one of two descriptors.
 
 The command line to run the program is as follows:
 
 
 Python3.6 [path‑to removeCorrelatedAttributes.py] ‑i [path‑to-‑arff-training-dataset] ‑o [path-to-output‑filename].
 
 
