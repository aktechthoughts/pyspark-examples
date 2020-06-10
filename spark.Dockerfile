FROM aktechthoughts/alpine-spark:1

RUN pip3 install findspark  boto3

COPY conf ${SPARK_HOME}/conf
COPY /app/ /app

WORKDIR /app

#CMD ["/bin/bash"]
