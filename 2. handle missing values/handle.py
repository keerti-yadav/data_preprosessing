//check in dataset
1. pandas doesn't understand ?/ any other strings so we need to replace it
2. df.replace('?', np.nan, inplace=true) //inplace krne se vo actual dataset m bhi changes hojayenge
3. df.isnull()  // bool value ka dataset return krega -- false== jaha not null true== null value
4. df.notnull() // isnull ka opp
5. missing_data= df.isnull()
      for column in headers :
        print(column)
        print(missing_data[column].value_counts())

6. how to deal missing value :
    1. drop missing values - 1. whole row/column
    2. replace - 1. mean--(jb outliers chote h)/median--(jb outliers bade ho) 2. freq(mode) - for category
    3. leave as it is
7. data ko dekh k consider kro ki konsa type lgana h


avgnum= df['column name '].astype("float").mean()
df['colname'].replace(np.nan, avgnum, inplace=true)


df['col-name'].value_counts().idmax() --most freq

df.dropna(subset=['col-name'] , inplace=true, axis=0) 

//if index present - reset it == df.reset(drop=true, inplace=true)
