FROM ubuntu:18.04
RUN apt upgrade && apt update && apt install -y \
    software-properties-common \
    python3-pip \
    python3-dev  
ADD . DEEP-LEARNING-PROJECT/
RUN pip3 install --upgrade pip
# RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python && python3 -m ensurepip && pip3 install --no-cache --upgrade pip setuptools 
RUN cd DEEP-LEARNING-PROJECT && pip3 install  --no-cache -r requirements.txt
EXPOSE 5000
#RUN python3 -m spacy download en_core_web_sm
ENTRYPOINT [ "sh", "-c" ]
CMD ["cd DEEP-LEARNING-PROJECT/src && python3 ML_Pipeline/deploy.py"]

#docker build -t deep-learning-pipeline:latest . 
#docker run -p 5000:5000 deep-learning-pipeline:latest
#Testing Trigger