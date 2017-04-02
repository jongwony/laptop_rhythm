# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#pd.date_range(datetime.today().date() - timedelta(days=1), periods=24, freq='H'))
#print(df.query('ID == 506'))
#print(df)
#print(df)

