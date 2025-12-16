from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page' 
  return render_template('index.html',title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Satayu Boonmuang'
  gmail = 'std.68122420115@ubru.ac.th'
  mobile = '0928190620'
  age = 21
  return render_template('about.html', title=title, name=name, gmail=gmail, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['กะเพราหมู', 'กะเพราไก่', 'กะเพราเนื้อ', 'กะเพราทะเล', 'กะเพรารวม']
  return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favorite/sport')
def favorite_sport():
  title = 'Favorite Sport Page'
  sport = ['ฟุตบอล', 'เทนนิส', 'อีสปอร์ต']
  return render_template('favorite_sport.html', title=title, sport=sport)

@app.route('/favorite/movie')
def favorite_movie():
  title = 'Favorite Movie Page'
  movie = ['อเวนเจอร์ส', 'อินเตอร์สเตลลาร์', 'สตาร์ เทรค', 'อพอลโล 13', 'ฟาสแอนฟีเรียส']
  return render_template('favorite_movie.html', title=title, movie=movie)