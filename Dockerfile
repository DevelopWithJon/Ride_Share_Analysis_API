FROM jupyter/datascience-notebook

ADD main.ipynb .

CMD ["jupyter", "./main.ipynb"]