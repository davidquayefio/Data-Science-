import yfinance as yf
import streamlit as st

st.title("Simple Stock Price App")
st.write("Google closing price and volume from 2014 to 2025.")

ticker_symbol = "GOOGL"
ticker_data = yf.Ticker(ticker_symbol)

# The end date is exclusive, so 2026-01-01 includes all of 2025.
ticker_df = ticker_data.history(start="2014-01-01", end="2026-01-01")

if ticker_df.empty:
    st.error("No stock data was returned. Check your internet connection and try again.")
else:
    st.subheader("Closing Price")
    st.line_chart(ticker_df["Close"])

    st.subheader("Trading Volume")
    st.line_chart(ticker_df["Volume"])