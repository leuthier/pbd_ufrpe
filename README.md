### Projeto de Banco de Dados (2017.1) (Python + Tweepy API + Naive Bayes + MySQL)
>Bacharelado em Sistemas de Informação - UFRPE <br>
#### Twitter: [@pbd_ufrpe](https://twitter.com/pbd_ufrpe)

#### Index
  * [1) How to create/execute](https://github.com/leuthier/pbd_ufrpe#1-how-to-createexecute)
  * [2) Objectives](https://github.com/leuthier/pbd_ufrpe#2-objectives)
  * [3) Team](https://github.com/leuthier/pbd_ufrpe#3-team)
  * [4) Questions?](https://github.com/leuthier/pbd_ufrpe#4-questions)
  * [5) References](https://github.com/leuthier/pbd_ufrpe#5-references)
  

#### 1) How to create/execute
* 1.1) It's necessary a phone number at your Twitter account to register an application: [Phone Number](https://twitter.com/settings/add_phone?edit_phone=true)

* 1.2) Create an application at Twitter: (New application)[https://apps.twitter.com/app/new]

* 1.3) Copy your tokens: https://apps.twitter.com/app/

* 1.4) Install pip module: [How do I install pip on Windows](http://www.stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows)
* 1.4.1) If you're using a Python 3.4, save this [(link here)](https://bootstrap.pypa.io/get-pip.py) as .py and run. Pip will dowload automatically.

* 1.5) Verify pip already installed to your Python version:
```
$ pip --version
``` 
* 1.5.1) If you dont know how to change your python version at cmd look at: [This question](http://stackoverflow.com/questions/18058389/how-to-switch-between-python-2-7-to-python-3-from-command-line)

* 1.6) Install those python libs at cmd or terminal:
```
$ python -m pip install --upgrade pip
$ pip install tweepy
```
cp (python version) - cp34 or cp36<br>
win - 32 or 64 bits<br>
Its necessary to [download a numpy](https://pypi.python.org/pypi/numpy) at your python and windows version before continue
Navigate to your numpy location
example:
```
C:\Users\Aluno> cd downloads
C:\Users\Aluno\Downloads> pip install numpy-1.13.1+mkl-cp34-cp34m-win32.whl
$ pip install nltk
$ pip install scipy
$ pip install sklearn
$ pip install geopy
$ pip install matplotlib
``` 

* 1.6) Run [Script VouDeQue.sql](https://github.com/leuthier/pbd_ufrpe/blob/master/Script%20VouDeQue.sql) at MySQL to create a new schema. If necessary change adress or password connection visit [DataBase.py](https://github.com/leuthier/pbd_ufrpe/blob/master/persistencia/DataBase.py) and choose equals at MySQL.

* 1.7) Change your tokens at [tweepyExample.py](https://github.com/leuthier/pbd_ufrpe/blob/master/tweepyExample.py) and run project to search tweets and classify with your own sentiment analysis. Choose 1- Positive, 2- Negative, 3- Neutral.

* 1.8) All tweets found will be at [doc.py](https://github.com/leuthier/pbd_ufrpe/blob/master/doc.py), just run this archive to save at MySQL.

* 1.9) In case of trouble try this tutorial: [Miniconda tutorial](https://drive.google.com/open?id=1qobuMvhqyO0DCQH8Bu_lIpD8UM9RE0nEOc-LjvZDXEo)

#### 2) Objectives
- [x] Search tweets about Uber, Cabify or 99Pop using Python and Twitter API
- [x] Store tweets to MySQL
- [x] Sentiment Analysis using Naive Bayes
- [x] Make queries and graphs based on last searches at a database

#### 3) Use Case Document
https://drive.google.com/open?id=0By7Vlsi01ABLSFFCc2NiNFVuX1k

#### 4) Team
- [Ariana Lima](https://github.com/arianalima)<br>
- [Bernardo Jr](https://github.com/bernardojr123)<br>
- [Bruna Vasconcelos](https://github.com/brunapvasconcelos)<br>
- [Victor Leuthier](https://github.com/leuthier)<br>

#### 5) Questions
[pbd2017[dot]1[at]gmail[dot]com](mailto:pbd2017.1@gmail.com)

