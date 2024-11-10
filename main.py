from flask import Flask, render_template, request, session, send_from_directory, redirect, url_for
from flask_socketio import SocketIO, emit
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'
socketio = SocketIO(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

current_page = 1
unique_id = None
filename = None

@app.route("/", methods=["GET", "POST"])
def admin():
    global current_page, unique_id, filename

    if request.method == "POST":
        file = request.files['file']
        if file:
            unique_id = os.urandom(8).hex()
            filename = secure_filename(f"{unique_id}.pdf")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['unique_id'] = unique_id
            session['filename'] = filename
            current_page = 1

    return render_template("admin.html", unique_id=unique_id)

@app.route("/viewer/<unique_id>")
def viewer(unique_id):
    return render_template("viewer.html", filename=f"{unique_id}.pdf")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@socketio.on('change_page')
def handle_change_page(data):
    global current_page
    current_page = data['page']
    emit('update_viewer', {'page': current_page}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
