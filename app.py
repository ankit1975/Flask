
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/index')
def index():
    name = request.args.get('name')
    return render_template('index.html', name = name)
    
@app.route('/skill')
def skill():
    from anki import seperate as yt 
    vid = yt.spliturl('Python Developer')
    return render_template('skill.html', skill = vid)

@app.route('/')
def video():
    vid = request.args.get('vid')
    # print(vid)

    if vid == None:
        vid = 'yVZIrQn-J0w'
    return render_template('video.html', vid = vid)

@app.route('/covidslot')
def covidslot():
    from flask import request as req
    pincode = req.args.get('pincode')                                                       
    date = req.args.get('date')

    link = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
    from urllib import request
    from bs4 import BeautifulSoup
    URL = link
    html = request.urlopen(URL).read()
    r = BeautifulSoup(html,'html.parser')
    #soup = BeautifulSoup(html,'html.parser')

    import json
    dictr = json.loads(r.text)
    rkey = dictr.keys()
    rvalue = list(dictr.values())

    # for i in range(len(rvalue[0])):
    #     print(rvalue[0][i])

    return render_template('covidslot.html',
                          rvalue=rvalue,
                          ran=range(len(rvalue[0])),
                          )

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)