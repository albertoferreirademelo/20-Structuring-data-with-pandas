import pandas as pd

years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]
number = 0

df = pd.read_excel ("raw_file_T2.xlsx")
raw_df = pd.read_excel("raw_file_T.xlsx")

#print (df.head())
#final_df = pd.DataFrame(columns=["Foretag", "Ar", "Antal Anstalda", "S:kortfristiga Skulder", "S:långfristiga Skulder", "Arets Resultat"])
#final_df = pd.DataFrame(columns=["Foretag", "Ar", "Senaste årsrapporten", "Avkastning", "Nettoomsattning(tkr)", "kortfristiga skulder", "langfristiga skulder", "totala tillgangar", "forsaljningstillvaxten"])
final_df = pd.DataFrame(columns=["Foretag", "Ar", "Avkastning", "Nettoomsattning(tkr)", "kortfristiga skulder", "langfristiga skulder", "totala tillgangar", "forsaljningstillvaxten"])
#final_df = pd.DataFrame(columns=["Foretag", "Org. nr", "Senaste arsredovisning", "Ar", "Avkastning", "Nettoomsattning(tkr)", "kortfristiga skulder", "langfristiga skulder", "totala tillgangar", "forsaljningstillvaxten"])
#print (df["Volkswagen Finans Sverige AB"].values[0:9])
#print (df["Volkswagen Finans Sverige AB"].values[9:18])
#print (df["Volkswagen Finans Sverige AB"].values[18:27])
#print (df["Volkswagen Finans Sverige AB"].values[27:])

#final_df.loc[0] = ["test", "2010", df["Volkswagen Finans Sverige AB"].values[0:9],  ]

for company in df:
    #print (company)
    #print (df[company].values[0])
    #print (df[company].values)
    #total = []
    for i in range(len(years)):
        #print (raw_df[company["orgnr"]])
        final_df.loc[number] = [company, years[i], df[company].values[i], df[company].values[i+9], df[company].values[i+18], df[company].values[i+27], df[company].values[i+36], df[company].values[i+45]]
        #final_df.loc[number] = [company, years[i], df[company].values[i]]
        number = number+1


final_df.to_csv("edited_ROA.csv")
#print (final_df)




''' ORIGINAL
for company in df:
    #print (df[company].values)
    total = []
    for i in range(len(years)):
        final_df.loc[number] = [company, years[i], df[company].values[i], df[company].values[i+9], df[company].values[i+18]]
        #final_df.loc[number] = [company, years[i], df[company].values[i]]
        number = number+1


final_df.to_csv("edited_ROA.csv")
#print (final_df)


'''