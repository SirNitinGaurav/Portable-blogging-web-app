# use the `mongo` image
FROM mongo
# copy the app directory into the container
COPY /app /app
RUN set -xe \
    && apt-get update -y \
    && apt-get install python3-pip -y 
# equip it with all the packages and installs needed to run the flask app (packages are defined in app/requirements.txt. `pip install -r app/requirements.txt`)
RUN pip3 install -r /app/requirements.txt
# expose the port flask app will run on
EXPOSE 5000











