apply_migrations(){
    echo applying migrations
    python3 manage.py migrate
    python3 manage.py makemigrations
}

#!/usr/bin/env bash
set -e
if [[ -d venv ]]; then
    echo venv folder already created
else
    echo venv folder not found, creating in progress...
    python3 -m venv venv
    echo launching venv
    source venv/bin/activate

    echo installing requirements
    pip install -r requirements.txt
fi

echo launching venv
source venv/bin/activate

apply_migrations

if [[ -f db.sqlite3 ]]; then
    echo local db found
else
    echo filling up local db, making migrations
    python3 fill_local_db.py
    apply_migrations
fi

cd currency_ex_front
if [[ -d node_modules ]]; then
    echo node_modules found, full npm install not executed
else
    echo node_modules not found, running npm install
    npm install
fi