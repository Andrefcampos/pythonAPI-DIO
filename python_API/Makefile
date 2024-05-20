run:
	@fastapi dev workout_api/main.py

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m ${d}

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head