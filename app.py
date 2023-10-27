from flask import Flask,render_template
app=Flask(__name__)

thumbnail_list=[{"thumbnail":"/static/images/thumbnail-1.jpg",
                 "description":"Man is enjoying the beach view",
                 "views":"2M Views",
                 "channel":"Beach View",
                 "uploaded":"5days ago"},

                 {"thumbnail":"/static/images/thumbnail-2.jpg",
                 "description":"A beautiful lake view",
                 "views":"1M Views",
                 "channel":"Lake view",
                 "uploaded":"7days ago"},

                 {"thumbnail":"/static/images/thumbnail-3.jpg",
                 "description":"World's most beautiful city is Newyork",
                 "views":"1M Views",
                 "channel":"Newyork City",
                 "uploaded":"2days ago"},

                 {"thumbnail":"/static/images/thumbnail-4.jpg",
                 "description":"Mountain view with fog and breeze",
                 "views":"1M Views",
                 "channel":"Mountain",
                 "uploaded":"2days ago"}]

@app.route('/')
def func():
    return render_template("index.html",list1=thumbnail_list)

if __name__=="__main__":
    app.run(debug=True)