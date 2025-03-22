
# write a script that takes a list of keywords and gets google trends data for the last 5 years and saves to csv
# input keywords haribo, pringles, walkers, cadbury, nestle, mars, galaxy, lindt, toblerone
# output: keywords.csv
# the csv file should have the following columns:
# date, keyword, value
# date is in the format YYYY-MM-DD
# keyword is the keyword
# value is the search interest value
# the script should be able to handle up to 50 keywords
# hint: you can use pytrends library to get google trends data
# pip install pytrends
# note: you may need to install pandas and lxml

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

# add streamlit input box where you can add up to 25 keywords
st.title("Google Trends Scraper")
st.write("Enter up to 25 keywords separated by commas")
# if keywords in the input box have line break, then split by comma and take the first 25 keywords
keywords = st.text_area("Keywords")
keywords = keywords.replace("\n", ",")
keywords = keywords.split(",")[:25]
#keywords = ["haribo", "pringles", "walkers", "cadbury", "nestle", "mars", "galaxy", "lindt", "toblerone"]

# create a pytrends object
pytrends = TrendReq(retries=3)

# create an empty dataframe
df = pd.DataFrame()

if st.button("Get Trends"):
    for keyword in keywords:
        # get the data
        pytrends.build_payload([keyword], timeframe='today 5-y')
        data = pytrends.interest_over_time()
        df = pd.concat([df, data])

# remove the match column
    df = df.drop(columns=["isPartial"])

# group by date, but keep all columns
    df = df.groupby("date").sum()

# reset the index
    df = df.reset_index()

# save the data via a streamlit download button
# create a download
    st.write("Download the data")
    st.write(df)
    st.write("Click the button below to download the data")
    st.write("Right click and save as keywords.csv")
    st.write("This will save the data to your local machine")
    st.write("You can open the file in Excel or Google Sheets")
    st.write("You can also use the data for further analysis")

# download the data
    csv = df.to_csv(index=False)
    st.markdown(f'<a href="data:file/csv;base64,{csv}">Download csv file</a>', unsafe_allow_html=True)




#df.to_csv("c:/Users/44754/Documents/Python Scripts/google trends/keywords.csv", index=False)

# end

