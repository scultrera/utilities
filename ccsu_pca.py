
"""
Some utilities for PCA to use it more like a clustering technique. 
I learned this in Grad school at Central Connecticut State University (CCSU), thus the name.

I want to be able to:
- create PCA solutions for groups of features
- For each PCA solution, I want to dataframes
    -- Feature weights x component
    -- component x eigenvalues, variance, cum variance

TODO:
- add OHE

"""

import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn import preprocessing



# -- Simple pca function which returns:
# -- pca object
# -- dataframe of features_weights
# -- dataframe of eigenvalues/component metrics
def get_pca(p_df, p_n_components=None, p_scale=True, p_column_list = [] ):
    

    if p_column_list:
        print("column list")
        if not set(p_column_list) <= set(p_df.columns):
            raise ("Invalid column list")
        p_df = p_df[p_column_list]
    else:
        p_column_list = p_df.columns

    if p_scale:
        df_pca_data = pd.DataFrame(preprocessing.scale(p_df),columns = p_column_list) 
    else:
        df_pca_data = p_df


    #-- get column count
    if p_n_components is None:
        p_n_components = len(df_pca_data.columns)
    if p_n_components > len(df_pca_data.columns):
        p_n_components = len(df_pca_data.columns)
    
    # PCA
    pca = PCA(n_components=p_n_components)
    pca.fit_transform(df_pca_data)

    #-- build list of component column names
    pca_column_names = ['PCA_' + str(i).zfill(2) for i in range(p_n_components) ]

    #-- build the two output dataframes from the pca object
    df_feature_weights = pd.DataFrame(np.transpose(pca.components_),columns=pca_column_names, index=df_pca_data.columns)
    df_variance = pd.DataFrame(
        {
            'eigenvalue' : pca.explained_variance_,
            'proportion' : pca.explained_variance_ratio_
        },
        index = pca_column_names
    )
    
    df_variance['cumulative'] = df_variance['proportion'].cumsum()
    
    return pca, df_feature_weights, df_variance
