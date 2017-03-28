FROM jupyter/scipy-notebook:latest

USER root
RUN apt-get update
RUN apt-get install -y python-qt4
#USER jovyan

# Launchbot labels
LABEL name.launchbot.io="LoukidesFractions"
LABEL workdir.launchbot.io="/usr/workdir"
LABEL 8888.port.launchbot.io="Jupyter Notebook"

# Set the working directory
WORKDIR /usr/workdir

# Expose the notebook port
EXPOSE 8888

# Start the notebook server
CMD jupyter notebook --no-browser --port 8888 --ip=*
