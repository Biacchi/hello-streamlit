# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="Finance", page_icon="💵")
st.title("Stock Price Analysis")

# Introduction
st.write("Welcome to the Stock Price Analysis App! Select a ticker to see its historical data.")

# Some ticker names
ticker_names = [
    'AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'FB', 'NFLX', 'NVDA', 'ADBE', 'PYPL',
    'JPM', 'V', 'JNJ', 'PG', 'UNH', 'MA', 'INTC', 'HD', 'VZ', 'DIS',
    'CRM', 'BAC', 'KO', 'CMCSA', 'XOM', 'PEP', 'CSCO', 'T', 'WMT', 'ABNB',
    'NVAX', 'ZM', 'SHOP', 'MRNA', 'UBER', 'LYFT', 'SQ', 'ROKU', 'TWTR', 'SNAP'
]

options = st.selectbox('Choose a ticker', ticker_names)

try:
    # Getting the data from the selected ticker
    tickerData = yf.Ticker(options)

    # Allow date selection
    start_date = st.date_input("Select start date", datetime(2010, 1, 1))
    end_date = st.date_input("Select end date", datetime.today())

    # Fetch historical data
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    if not tickerDf.empty:
        st.subheader("Stock Data Overview")
        st.write(tickerDf.describe())  # Display basic statistics
        
        # Visualizations
        st.subheader("Historical Stock Price")
        st.line_chart(tickerDf.Close)
        
        st.subheader("Volume")
        st.line_chart(tickerDf.Volume)

    else:
        st.warning("No data found for the selected ticker or date range.")

except Exception as e:
    st.error("An error occurred: {}".format(str(e)))
