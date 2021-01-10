from flask import Flask, render_template
from functions import read_demo_data

app = Flask(__name__)


@app.route('/')
def run_demo():
    data = read_demo_data()
    return render_template('wb.html', len=len(data.index), robots=data['Machine_Name'], status=data['status'],
                           task=data['Page_Name'], description=data['Process_Name'], progress=data['progress'],
                           num=data['numerator'], den=data['denominator'], start=data['Time Started'])


if __name__ == '__main__':
    app.run(use_reloader=True)
