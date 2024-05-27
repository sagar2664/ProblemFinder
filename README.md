## setup the Projects
1. clone the reprojectory
```bash
git clone git@github.com:Debraj-Das/ProblemFinder.git
```
2. go to ProblemFinder directory `cd ProblemFinder`
3. setup the virtual enviroment
```bash
# windows
python -m venv .venv 
# linux and mac
virturalenv .venv
```
4. install nessary module
```bash
pip install -r requirements.txt
```
5. check the Projects
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py check
```
6. start the server
```bash
python manage.py runserver
```
