FROM ubuntu:latest
#RUN apk add git 
RUN apt-get update && apt-get install -y --no-install-recommends\
    git\
    python3.9\
    python3-pip\
    vim
ENV gitrepo https://github.com/srinivasaraojyothi/pythonseleniumframework.git   
ENV gitbranch dockertest
RUN git config --global http.sslverify false     
RUN git clone ${gitrepo}
RUN cd ./pythonseleniumframework && git checkout ${gitbranch} && git pull origin ${gitbranch}
#RUN git checkout main
# ./pythonseleniumframework
WORKDIR  pythonseleniumframework
RUN pip install -r requirements.txt
ENV PYTHONPATH=/pythonseleniumframework
ENV tag "tt"
ENV browser chrome
ENV exenv qc
ENV platform web
CMD ["sh", "-c", "pytest -m ${tag}  -rA  --alluredir allurereports --b=${browser} --e=${exenv} --t=${platform} -v"]