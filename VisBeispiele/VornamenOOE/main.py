import numpy as np
import pandas as pd
from bokeh.charts import CategoricalHeatMap

raw_data = pd.read_csv("./data/OOE_Haeuf_Vornamen.csv", sep=";")

def getDataPerYear(df, year):
    "getting a df with namek number and sex per year"
    temp = df[df.YEAR == int(year)]
    temp_df = pd.concat([temp["GIVEN_NAME"], temp["NUMBER"], temp["SEX"]],
                        axis=1)
    temp_df.columns = ["Name", "Haeuf", "SEX"]
    return temp_df

def getDataPerSex(df, sex):
    "getting a df with name and number for each sex"
    temp = df[df.SEX == int(sex)]
    temp_df = pd.concat([temp["Name"], temp["Haeuf"]], axis=1)
    temp_df.columns = ["Name", "Haeuf"]
    return temp_df

def mergeDF(df1, df2, sex):
    "merging dataframes"
    if sex == 1:
        return df1.merge(df2, how="outer", on="Name")
    elif sex == 2:
        return df1.merge(df2, how="outer", on="Name")

# getting male and female data
data_m = {}
data_f = {}

for i in range(2004, 2014):
    keys_m = "data" + str(i).rjust(2, "0") + "m"
    keys_f = "data" + str(i).rjust(2, "0") + "f"
    values_m = getDataPerSex(getDataPerYear(raw_data, i), 1)
    values_f = getDataPerSex(getDataPerYear(raw_data, i), 2)
    data_m[keys_m] = values_m
    data_f[keys_f] = values_f

# merging to final df
df_final_m = pd.DataFrame(columns=["Name", "Haeuf"])
df_final_f = pd.DataFrame(columns=["Name", "Haeuf"])


for key in data_m.keys():
    df_final_m = mergeDF(df_final_m, data_m[key], 1)

for key in data_f.keys():
    df_final_f = mergeDF(df_final_f, data_f[key], 2)

# cleaning final df
col_names_m = ["fixme", "Name", "2009", "2012", "2007", "2013", "2006", "2008",
             "2010", "2005", "2011", "2004"]
col_names_f = ["fixme", "Name", "2004", "2011", "2012", "2005", "2007", "2008",
             "2010", "2006", "2013", "2009"]
new_col_names = ["fixme", "Name", "2004", "2005", "2006", "2007", "2008",
                 "2009", "2010", "2011", "2012", "2013"]


df_final_m = df_final_m[:69]
df_final_f = df_final_f[:65]

df_final_m.columns = col_names_m
df_final_m = df_final_m.reindex(columns=new_col_names)
df_final_m.fillna(0, inplace=True)
df_final_m["sum"] = df_final_m.sum(axis=1)
df_final_m.sort("sum", ascending=False, inplace=True)
df_final_m.drop(["fixme", "sum"], 1, inplace=True)

df_final_f.columns = col_names_f
df_final_f = df_final_f.reindex(columns=new_col_names)
df_final_f.fillna(0, inplace=True)
df_final_f["sum"] = df_final_f.sum(axis=1)
df_final_f.sort("sum", ascending=False, inplace=True)
df_final_f.drop(["fixme", "sum"], 1, inplace=True)

df_final_m2 =df_final_m.set_index(df_final_m[df_final_m.columns[0]].astype(str))
df_final_m2.drop(df_final_m.columns[0], axis=1, inplace=True)

df_final_f2 =df_final_f.set_index(df_final_f[df_final_f.columns[0]].astype(str))
df_final_f2.drop(df_final_f.columns[0], axis=1, inplace=True)

# filter top 25 names
df_final_m2 = df_final_m2.head(n=25)
df_final_f2 = df_final_f2.head(n=25)

# plot categorial heatmap
pal_m = ["#f7fcf0", "#e0f3db","#ccebc5", "#a8ddb5", "#7bccc4", "#4eb3d3",
          "#2b8cbe", "#0868ac", "#084081"]
pal_f = ["#fff7f3", "#fde0dd", "#fcc5c0", "#fa9fb5", "#f768a1", "#dd3497",
         "#ae017e", "#7a0177", "#49006a"]


output_m = CategoricalHeatMap(df_final_m2, palette=pal_m, 
                              title="Männl. Vornamen", filename="output_m.html")
output_f = CategoricalHeatMap(df_final_f2, palette=pal_f,
                              title="Weibl. Vornamen", filename="output_f.html")

#output_test.show()
