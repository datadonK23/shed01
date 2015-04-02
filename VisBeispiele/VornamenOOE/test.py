from bokeh.sampledata.unemployment1948 import data

# pandas magic
df = data[data.columns[:-2]]
df2 = df.set_index(df[df.columns[0]].astype(str))
df2.drop(df.columns[0], axis=1, inplace=True)
df3 = df2.transpose()

print(df3)