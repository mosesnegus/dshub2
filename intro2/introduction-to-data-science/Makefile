default:
		docker run -it --rm \
		-v `pwd`:/home/jovyan \
		jupyter/datascience-notebook \
		jupyter nbconvert --config doc/nbconvert_config.py

book:
		docker run -it --rm \
		-v `pwd`:/home/jovyan \
		bookbook \
		python -m bookbook.latex --pdf --template doc/custom.tplx
