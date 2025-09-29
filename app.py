from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select_subject():
    if request.method == 'POST':
        subject = request.form.get('subject')
        subcategory = request.form.get('subcategory')
        if subject == 'science' and subcategory:
            return f'You selected Science > {subcategory.capitalize()}'
        elif subject:
            return f'You selected {subject.capitalize()}'
        else:
            return 'Please select a subject.'

    # Render form with subject dropdown; subcategory dropdown shown if science is chosen via JavaScript
    return render_template_string('''
        <html>
        <head>
          <script>
            function showSubcategory() {
                const subject = document.getElementById('subject').value;
                const sciSub = document.getElementById('science-sub');
                if(subject === 'science') {
                    sciSub.style.display = 'block';
                } else {
                    sciSub.style.display = 'none';
                }
            }
          </script>
        </head>
        <body>
          <form method="POST">
            <label for="subject">Select Subject:</label>
            <select name="subject" id="subject" onchange="showSubcategory()" required>
              <option value="">--Select--</option>
              <option value="science">Science</option>
              <option value="computer science">Computer Science</option>
              <option value="english">English</option>
              <option value="maths">Maths</option>
            </select>

            <div id="science-sub" style="display:none; margin-top:10px;">
              <label for="subcategory">Select Science topic:</label>
              <select name="subcategory" id="subcategory">
                <option value="">--Select--</option>
                <option value="physics">Physics</option>
                <option value="chemistry">Chemistry</option>
                <option value="biology">Biology</option>
              </select>
            </div>

            <br><br>
            <button type="submit">Submit</button>
          </form>
        </body>
        </html>
    ''')