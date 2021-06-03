from flask import Flask, render_template, request
app = Flask(__name__, template_folder='client/templates')
from link_extractor import from_website


@app.route("/", methods=['GET', 'POST'])
def link_extractor():
       if request.method == 'GET':
           return render_template('index.html')
       else:
           #print("after post")
           links = request.form['input_links']
           each_link = from_website(links)
           #print(each_link)
           return render_template('index.html', each_link=each_link)



if __name__ == '__main__':
    app.run(debug=True)
