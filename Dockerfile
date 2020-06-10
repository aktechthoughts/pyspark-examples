# Adopted from https://github.com/sebnyberg/pyspark-alpine

FROM openjdk:8-jdk-alpine

ENV HADOOP_VERSION 2.7.3
ENV HADOOP_HOME /usr/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop

ENV SPARK_VERSION 2.4.6
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"

ENV PYSPARK_PYTHON python3
ENV PYSPARK_DRIVER_PYTHON=python3

ENV PATH $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$SPARK_HOME/bin
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.7-src.zip:$PYTHONPATH

# hadoop
RUN set -ex \
  && apk add --no-cache bash \
  && apk add --virtual .fetch-deps --no-cache ca-certificates wget curl \
  && curl -sL --retry 3 \
  "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
  | gunzip \
  | tar -x -C /usr/ \
  && rm -rf $HADOOP_HOME/share/doc \
  && chown -R root:root $HADOOP_HOME \
  # sparkdocker run -it -v $(pwd):/code sebnyberg/pyspark-alpine
  && curl -sL --retry 3 \
  "https://www.apache.org/dyn/mirrors/mirrors.cgi?action=download&filename=spark/spark-${SPARK_VERSION}/${SPARK_PACKAGE}.tgz" \
  | gunzip \
  | tar x -C /usr/ \
  && mv /usr/$SPARK_PACKAGE $SPARK_HOME \
  && chown -R root:root $SPARK_HOME
  # cleanup
  # && apk del .fetch-deps \
  # && apk del .conda-deps

# Add pip & virtualenv
RUN apk add --update \
    python3 \
    python3-dev \
    py-pip \
    build-base \
  && pip3 install --upgrade pip \
  && pip3 install virtualenv \
  && rm -rf /var/cache/apk/*

COPY conf ${SPARK_HOME}/conf

#CMD ["/bin/bash"]
