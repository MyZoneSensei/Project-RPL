from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Pertanyaan dan jawaban
questions = [
    {
        "question": "Apakah anda merasa bahagia ketika berada di dekat orang yang anda cintai? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda sering memikirkan orang yang anda cintai dalam keseharian anda ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa nyaman untuk berbagai perasaan anda kepada orang yang anda cintai ? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda percaya bahwa hubungan cinta membutuhkan komitmen yang tulus ? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa penting untuk menunjukkan kasih sayang secara rutin kepada orang anda cintai ? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa dicintai dengan orang anda sukai ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda percaya bahwa cinta dapat membuat seseorang menjadi lebih baik ? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa terdorong untuk mendukung dan membantu dengan orang anda sukai dalam situasi apa pun ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa cintai sejati tidak membutuhkan alasan yang jelas, tetapi dirasakan dengan tulus ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": " Apakah anda percaya bahwa komunikasi yang baik adalah kunci untuk mempertahankan cinta ? ",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": "Apakah anda merasa hubungan cinta yang sehat membutuhkan saling pengertian ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },
    {
        "question": " Apakah anda percaya bahwa cinta adalah salah satu alasan utama untuk merasa bahagia dalam hidup ?",
        "options": ["Sangat Setuju", "Setuju", "Tidak Setuju", "Sangat Tidak Setuju"],
        "scores": [4, 3, 2, 1]
    },

]

# Penyimpanan skor
user_score = 0
current_question = 0

@app.route('/')
def home():
    global user_score, current_question
    user_score = 0
    current_question = 0
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    global user_score, current_question

    if request.method == 'POST':
        # Tambahkan skor dari jawaban
        selected_option = int(request.form['option'])
        user_score += questions[current_question]['scores'][selected_option]
        current_question += 1

        if current_question >= len(questions):
            return redirect(url_for('result'))

    question_data = questions[current_question]
    return render_template('question.html', question=question_data, q_num=current_question + 1, total=len(questions))

@app.route('/result')
def result():
    # Menentukan mood berdasarkan skor
    if user_score <= 15:
        mood = "Sedih"
        playlist = "https://open.spotify.com/playlist/19FMU3pqbHqLCyTASa4fLn?si=UF4OWrTeTW2pJzx3SQPlOQ&pi=a-bsZnq3PDTLaP"
    elif user_score <= 24:
        mood = "Bahagia"
        playlist = "https://open.spotify.com/playlist/7BYxGOGbrSZjZ2YbN9XItq?si=XaJlHFHCRe6rRKK5-n5ozg&pi=a-uxofV2jrTUab"
    elif user_score <= 32:
        mood = "Excited"
        playlist = "https://open.spotify.com/playlist/0M4I4oJEA7E4Odw3czf60b?si=fq2dedh5QBWAMduIclQntw&pi=a-OdPf8gb1QZuF"
    else:
        mood = "Lovin"
        playlist = "https://open.spotify.com/playlist/5ZHxYuLhwM94XAtWU16E9L?si=43563b67e48a4b4c"

    return render_template('result.html', mood=mood, playlist=playlist)

if __name__ == '__main__':
    app.run(debug=True)
