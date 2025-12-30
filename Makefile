.PHONY: help venv install run dev freeze clean

help:
	@echo "make dev     - create venv (if needed), install deps, run server"
	@echo "make install - install backend deps"
	@echo "make run     - run backend server"
	@echo "make freeze  - write backend/requirements.lock.txt"
	@echo "make clean   - remove venv + caches"

venv:
	@test -d .venv || python3 -m venv .venv

install: venv
	@. .venv/bin/activate && pip install -r backend/requirements.txt

run:
	@. .venv/bin/activate && uvicorn backend.app.main:app --reload

dev: install run

freeze: install
	@. .venv/bin/activate && pip freeze > backend/requirements.lock.txt

clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
