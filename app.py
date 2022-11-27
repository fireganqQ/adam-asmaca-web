from flask import Flask, render_template, request, session
import random as _r

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class trivia:
	def __init__(self):
		self.words = self.readWords()

	def readWords(self):
		return open("words.siü", "r", encoding="utf8").readlines()
	def addLetter(self, wList: list):
		return ''.join(wList)



class imgPath:
	def __init__(self):
		self.lvl1 = imgPath.lvl1(self)
		self.lvl2 = imgPath.lvl2(self)
		self.lvl3 = imgPath.lvl3(self)
		self.lvl4 = imgPath.lvl4(self)
		self.lvl5 = imgPath.lvl5(self)
		self.lvl6 = imgPath.lvl6(self)
		self.lvl7 = imgPath.lvl7(self)
		self.lvl8 = imgPath.lvl8(self)
	def lvl1(self):
		return "/static/img/lvl1.png"
	def lvl2(self):
		return "/static/img/lvl2.png"
	def lvl3(self):
		return "/static/img/lvl3.png"
	def lvl4(self):
		return "/static/img/lvl4.png"
	def lvl5(self):
		return "/static/img/lvl5.png"
	def lvl6(self):
		return "/static/img/lvl6.png"
	def lvl7(self):
		return "/static/img/lvl7.png"
	def lvl8(self):
		return "/static/img/lvl8.png"


@app.route('/', methods=["POST", "GET"])
def index():
	start = False
	char = ""
	lvlImg = imgPath().lvl1
	alertMsg = False

	if request.method == "POST":
		if 'start' in request.form:
				session['start'] = True
				session['word'] = (_r.choice(trivia().words).lower()).replace("\n", "").replace(" ", "")
				print(session['word'])

				session['char'] = "-"*len(session["word"])
				session['img'] = imgPath().lvl1
				session['remainder'] = 0
		elif 'save' in request.form:
			if session['start']:
				getLetter = request.form['word']

				print("**", getLetter)

				if getLetter.lower() in list(session['word']):
					__a__ = list(session['char'])
					__a__[session['word'].index(getLetter.lower())] = getLetter.lower()
					session['char'] = trivia().addLetter(__a__)


					__a__ = list(session['word'])
					__a__[session['word'].index(getLetter.lower())] = "-"
					session['word'] = trivia().addLetter(__a__)

				elif getLetter.replace(" ", "") == "":
					pass

				else:
					session['remainder'] = session['remainder'] +1
					print(session['remainder'])
					if session['remainder'] == 1:
						session['img'] = imgPath().lvl2

					elif session['remainder'] == 2:
						session['img'] = imgPath().lvl3

					elif session['remainder'] == 3:
						session['img'] = imgPath().lvl4

					elif session['remainder'] == 4:
						session['img'] = imgPath().lvl5

					elif session['remainder'] == 5:
						session['img'] = imgPath().lvl6

					elif session['remainder'] == 6:
						session['img'] = imgPath().lvl7

					elif session['remainder'] == 7:
						session.clear()
						start = False
						char = ""
						lvlImg = imgPath().lvl1
						alertMsg = 'Tüm Haklarınızı Kullandınız!'


	if 'start' in session:
		start = session['start']
		char = session['char']
		lvlImg = session['img']

	return render_template('index.html', user_play=start, img_url=lvlImg, char=char, alertMsg=alertMsg)

app.run(debug=True)