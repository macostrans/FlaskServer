import plotly.graph_objs as go
import plotly.offline as pyo
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    df = pd.read_excel(r"https://docs.google.com/spreadsheets/d/1NQAgiLylrdEYLjGWXdc8J3Ns3YmNYZLjVldAf8Mm_kE/export?format=xlsx",sheet_name="index")
    trace = go.Table(columnwidth=[2, 8, 5, 3, 8], header=dict(values=df.columns), cells=dict(values=[df[name] for name in df.columns]))
    data = [trace]
    layout = go.Layout(title=dict(text="Table of Contents", x=0.5, y=0.9, xanchor="center", yanchor="top"))
    fig = go.Figure(data=data, layout=layout)
    html_plot = pyo.plot(fig, filename='plotted_file.html', auto_open=False)
    with open('plotted_file.html', 'r') as f:
        html = f.read()
        return html

@app.route('/test')
def ByeWorld():
    return "Bye Bye Cruel World2"

if __name__ == '__main__':
    app.run(port=5000, debug= True)