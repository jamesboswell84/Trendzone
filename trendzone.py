
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
st.write(keywords)
# create a pytrends object
pytrends = TrendReq(requests_args = {'headers': {'Cookie': f'NID=ffD__G26sG0WTVmL7aLkVCNqw6KwdP5QAOpuWR1212OQQ-p4grH4lT9RpgY-AYgklQ8qOzXpSKxX22MSOU5Y7wKcmmG81tlXuH-D6CcUDOH8P13u5VMlqGgZK8GrUcO3P3DolzFA4-v1jwfwUJx0aaFbPBQENGJA4BFQMy6IJSpX4DAKsdZbn3goSyZMT43MndyW-BgkHW4bQje2NU0vstTJLg3pBMWFDFUDbFgUOHy7LPSaeFnmItE6xCX5jph7f29uY-liW8PxNJkzsdwl5NblhNkHajbB_ZNTQyF2CkHnSoQsNSn07Zu2e48gWyf764cqjPdLKH5iKotZpWKO-CSu5010A8pjt2KKNfPYlLoax1vlUDV7bQ6C5_t9dHEFFuqnUHiN7eLhEUUIxo350EqmHZZZ8qznfgh2sy65G9GmoQ4AJKCHEPk7aHHRm9YLTRYQzABbJ5fbsKLebjGFpDj5-JlYl7J-iR0QrxdV2eUe6ZdR5a7QJIpopUrY5vQ2bZk6-6CzNGvGYtH88ayk6s079ez7UZFxEXQCANq3ea2V4ZHow5MGoqGlwKVg_s4-VWkGxWi4atn0Cydb4W7b9bODMIEzpDXnPDakHo0onQLosYmVDAPYwIJLJqgw0ws_SnHRxN2cEmaqnCwKrJKVc25eRinaTnMdUsvGxhc4oGiiQc82QxjsQXkJh5AWlHmnzcavzZI432cuAP4HWGOiC_nQUP-bjCQM35Qoq9qNBzJtJryB5HCshJ-rnD8b5qAkxyJeytrn02tiRTRtFo44xo1j_vlUd9U4EacqzXGNTkfVdb-OvzLFilRVyla2LgwXlmA015B-v99v8yvx3EngcUc2OgthEVuJb1_pvLKEyPEJwElrKXcUWVg6_uTc8DSve6sIGBLwcVIbrRwYBZb4suaB9atREaCD4xrSLZuVtXg8271ajlVZ-ZMdKgZVAw-2Xb1ztq-JIotblmgyCEvpjS3H0CmxDSKz5w'}})

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

