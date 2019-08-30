import os
from flask import Flask, flash, render_template, redirect, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "supertopsecretprivatekey"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # show the upload form
        return render_template('home_page.html')

    if request.method == 'POST':
        # check if a file was passed into the POST request
        if 'image' not in request.files:
            flash('No file was uploaded.')
            return redirect(request.url)

        image_file = request.files['image']

        # if filename is empty, then assume no upload
        if image_file.filename == '':
            flash('No file was uploaded.')
            return redirect(request.url)

        # if the file is ok
        if image_file:
            passed = False
            try:
                filename = image_file.filename
                filepath = os.path.join('/tmp/fuzzvis/', filename)
                image_file.save(filepath)
                passed = True
            except Exception:
                passed = False

            if passed:
                return redirect(url_for('predict', filename=filename))
            else:
                flash('An error occurred, try again.')
                return redirect(request.url)
