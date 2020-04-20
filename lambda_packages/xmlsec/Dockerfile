FROM lambci/lambda:build-python3.8

RUN yum makecache fast && yum -y update && \
      yum install -y sudo python-pip

WORKDIR /workon

ADD build.sh /workon

RUN ["chmod", "+x", "/workon/build.sh"]

# The build script signatures are not always the same, and may require small tweaks
# but are mostly similar
RUN cd /workon && /bin/bash -x build.sh "xmlsec" "1.3.3" "python3.8"
