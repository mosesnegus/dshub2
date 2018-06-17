FROM jupyter/datascience-notebook
RUN pip install bookbook

USER root
RUN apt-get update && apt-get install openssh-server -y
USER jovyan

RUN /opt/conda/bin/pip install bash_kernel
RUN /opt/conda/bin/python -m bash_kernel.install
