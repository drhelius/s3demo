FROM registry.access.redhat.com/ubi8/python-39

USER 0
ADD app.py requirements.txt ./
RUN chown -R 1001:0 ./
USER 1001

RUN pip install -U "pip>=19.3.1" && \
    pip install -r requirements.txt

CMD python app.py