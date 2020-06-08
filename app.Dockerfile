FROM aktechthoughts/jupyter_web:latest

COPY config ${SPARK_HOME}/conf

RUN pip install findspark

COPY /app/ /app
RUN mkdir /app/config

WORKDIR /app

#CMD ["/bin/bash"]
