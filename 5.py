!apt-get install openjdk-8-jdk-headless -qq
!wget -q https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
!tar xf hadoop-3.3.1.tar.gz

import os
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-8-openjdk-amd64'
os.environ['HADOOP_HOME'] = '/content/hadoop-3.3.1'
os.environ['HADOOP_CONF_DIR'] = '/content/hadoop-3.3.1/etc/hadoop'
os.environ['PATH'] = os.environ['HADOOP_HOME'] + '/bin:' + os.environ['PATH']

# Configure HDFS
!cp /content/hadoop-3.3.1/etc/hadoop/core-site.xml /content/hadoop-3.3.1/etc/hadoop/core-site.xml.bak
!cp /content/hadoop-3.3.1/etc/hadoop/hdfs-site.xml /content/hadoop-3.3.1/etc/hadoop/hdfs-site.xml.bak
!echo -e '<configuration><property><name>fs.default.name</name><value>hdfs://localhost:9000</value></property></configuration>' > /content/hadoop-3.3.1/etc/hadoop/core-site.xml
!echo -e '<configuration><property><name>dfs.replication</name><value>1</value></property></configuration>' > /content/hadoop-3.3.1/etc/hadoop/hdfs-site.xml

# Format HDFS
!hdfs namenode -format

# Verify HDFS is running
!jps