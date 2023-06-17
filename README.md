### How to start the project on a local machine:

Clone the repository and enter into directory:

```
git clone 
```

```
cd what_to_watch
```

Create and activate virtual environment:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

or for Windows users:

```
source env/Scripts/activate
```

Install requirements from requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Apply migrations to the DB of the project:

```
flask db upgrade
```

Run the project:

```
flask run
```

Also, you can fill DB from opinions.csv:

```
flask load_opinions
```