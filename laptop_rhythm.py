# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html')

@app.context_processor
def data():
    def wrap():
        from evt_proc import EventProc
        return [i for i in EventProc().today_rhythm()]
        #return grouping((i for i in EventProc().today_rhythm()))
    return dict(data=wrap)

if __name__ == '__main__':
    app.run(debug=True)
