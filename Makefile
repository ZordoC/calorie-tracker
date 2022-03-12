format:
	black -l 100 anna_calories
	isort anna_calories
lint:
	pylint anna_calories