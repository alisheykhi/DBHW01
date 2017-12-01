from flask import Flask, render_template
from studentItem import Item,ItemTable

app = Flask(__name__)

items = [Item('810196061','Ali', 'Sheykhi', 'Software Engineering'),
         Item('810196062','Hassan', 'Mirzai', 'Mathematics'),
         Item('810196063','Amir Hossein', 'Mohammadi', 'Civil Engineering'),
         Item('810196064','Reza', 'Erfani', 'Telecommunication'),
         Item('810196065','Setare', 'Salari', 'Pharmacy'),
         Item('810196066','Ghazal', 'Salari', 'Medicine')]

table = ItemTable(items)

#print(table.__html__())

@app.route('/')
def index():
    return render_template('index.html', table=table)

if __name__ == "__main__":
    app.run(host="0.0.0.0")