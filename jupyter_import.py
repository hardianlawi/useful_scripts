%cd ..
%load_ext nb_black
%load_ext autoreload
%load_ext google.cloud.bigquery
%autoreload 2

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import datatable as dt
import tensorflow as tf

import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

%matplotlib inline

plt.style.use('seaborn')

plt.rcParams["figure.figsize"] = [20.0, 10.0]
plt.rcParams["agg.path.chunksize"] = 10000
plt.rcParams["legend.frameon"] = True
sns.set_style("whitegrid", {'grid.linestyle': '--'})

pd.options.display.max_columns = 200


def inspect(df):
    print('df size:', df.shape)
    display(df.head())
    print("\nStatistics")
    display(df.describe([.05, .25, .5, .75, .95, .99]))
    print("\nMissing values")
    display(df.isnull().sum())
    print(f"Any missing values: {df.isnull().any()}")
    display(df.dtypes)


# Load from BQ
# %%bigquery sg_reward_log --params {"start_date": '2020-12-02', "end_date": '2020-12-18'}

# Hide ALL Codes
# http://blog.nextgenetics.net/?e=102
# https://chris-said.io/2016/02/13/how-to-make-polished-jupyter-presentations-with-optional-code-visibility/
from IPython.display import HTML

HTML('''<script>
code_show=true;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')