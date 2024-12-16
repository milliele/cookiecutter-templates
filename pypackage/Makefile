BAKE_OPTIONS=--no-input

help:
	@echo "help 	Show this help"
	@echo "bake 	Generate project using defaults under path ``tests/output_data/``"
	@echo "deps 	Install all the dependencies for testing"

bake:  # Generate project using defaults
	pipx run cookiecutter $(BAKE_OPTIONS) -f . -o tests/output_data/

deps:
	pip install -r requirements.txt