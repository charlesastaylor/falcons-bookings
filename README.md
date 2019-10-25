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
- Ask to be added as contributer

___

### Dan's Wishlist

> **Easy Registration** - Email, First Name, Surname, password

> **Front End**:
Login/Register to view
Date/Session Selector - Show Date, Time, Location, Cost
User roles (members have early booking, different costs per age group, only 2nd squad see 2nd squad sessions and games etc.
Squad members see the sessions 24hours before everyone else. For a a Monday session could book the Sunday from 7pm a week in advance, so would see two

> **User Account**:
Show Current Bookings
Show Current Credit 

> **Admin**:
Tie in with the register
Allow admin override post session (not signed up in advance)
Confirm attendance & payment amount
Add/Remove Sessions
Re-Occurring sessions, link to google cal?

### TODO:
- [x] Canel bookings up to 3 hours before session
- [x] Toast flash messages
- [ ] Move todo list/dan's wishlist to trello
- [ ] Send emails on different thread ([flask mega tutorial section](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support), [SO question](https://stackoverflow.com/questions/27345291/sending-async-email-with-flask-security))
- [ ] Admin session page
- [ ] Waiting list once session full -> email notification if someone cancels
- [ ] Fix python debug server - doesn't work since configuring real servers
