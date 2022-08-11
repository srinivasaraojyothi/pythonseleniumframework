FROM ubuntu:latest
#RUN apk add git 
RUN apt-get update && apt-get install -y --no-install-recommends\
    git\
    python3.9\
    python3-pip
RUN git config --global http.sslverify false     
RUN git clone https://github.com/srinivasaraojyothi/pythonseleniumframework.git
RUN cd ./pythonseleniumframework && git checkout dockertest && git pull origin dockertest
#RUN git checkout main
# ./pythonseleniumframework
WORKDIR  pythonseleniumframework
RUN pip install -r requirements.txt
ENV PYTHONPATH=/pythonseleniumframework
ENV tag "m"
ENV browser chrome
ENV exenv qc
ENV platform web
#CMD ["sh", "-c", "pytest -m ${tag}  -rA  --alluredir allurereports --b=${browser} --e=${exenv} --t=${platform} -v"]