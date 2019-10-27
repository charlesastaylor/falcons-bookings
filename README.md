# falcons-bookings

Training session booking system for [Northampton Falcons Basketball Club](http://www.northamptonfalcons.co.uk/)

## Getting Started

### Prerequistes
- python>=3.6.8
- sqlite3 (used by default, free to set up another database engine)

### Initial setup
1. Clone repository: `git clone https://github.com/charlesastaylor/falcons-bookings.git`
2. Create python virtual environment:
    1. `cd falcons-bookings`
    2. `python3 -m venv venv`
4. Activate virtual environemnt: `source venv/bin/activate`
5. Install python requirements: `pip install -r requirements.txt`
6. Set up environemnt: `cp .flaskenv.default .flaskenv`
7. Create database: `flask db upgrade`

### Running
- (If not already done) `source venv/bin/activate`
- `flask run`
- (Optional) Run debug mail server: `flask mail-server`

### Updating
1. Make sure working direcotry is clean (commit/shelve local changes)
2. (If not already done) `source venv/bin/activate`
3. `git pull`
4. `pip install -r requirements.txt`
5. `flask db upgrade`

___

## Contributing

- [Create a PR](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
- Ask to be added as collaborator
