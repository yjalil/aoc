include .env
export $(shell sed 's/=.*//' .env)

setup:
	pip uninstall aoc
	pip install -e .

run:
	uvicorn api.main:app --host ${HOST} --port ${PORT} --reload & \
	sleep 2 && \
	xdg-open "http://${HOST}:${PORT}/docs"

stop:
	@pkill -f uvicorn

input:
	python api/get_input.py $(year) $(day)

solve:
	python api/solution.py $(year) $(day) $(part) $(file)

test:
	pytest -q api/tests/
