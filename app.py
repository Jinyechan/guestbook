from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import uuid

app = Flask(__name__)

guestbooks = []

@app.route("/", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        category = "일반"
        guestbook_id = str(uuid.uuid4())[:12]
        guestbooks.append({
            "title": title,
            "content": content,
            "category": category,
            "regdate": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "id": guestbook_id
        })
        return redirect(url_for("guestbook"))
    return render_template("guestbook.html", guestbooks=guestbooks)

@app.route('/delete/<string:id>', methods=["GET", "POST"])
def delete(id):
    global guestbooks
    guestbooks = [guestbook for guestbook in guestbooks if guestbook["id"] != id]
    return redirect(url_for('guestbook'))

if __name__ == "__main__":
    app.run(debug=True)
