import pandas_datareader as web
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

fd = open("crypto_list_alphabetical.txt", 'r')
# fd = open("crypto_list_by_marketcap.txt", 'r')
crypto = fd.read().splitlines()
selected_crypto = []


def calc_correlation(start_str, end_str):
    currency = "USD"
    metric = "Close"
    start = dt.datetime.strptime(start_str, "%Y-%m-%d")
    end = dt.datetime.strptime(end_str, "%Y-%m-%d")

    col_names = []

    first = True

    for ticker in selected_crypto:
        data = web.DataReader("{0}-{1}".format(ticker, currency), "yahoo", start, end)
        if first:
            combined = data[[metric]].copy()
            col_names.append(ticker)
            combined.columns = col_names
            first = False
        else:
            combined = combined.join(data[metric])
            col_names.append(ticker)
            combined.columns = col_names

    combined = combined.pct_change().corr(method="pearson")
    sns.heatmap(combined, annot=True, cmap="coolwarm")
    plt.title('Pearson Correlation Chart')
    plt.show()
    plt.clf()
    plt.close('all')
