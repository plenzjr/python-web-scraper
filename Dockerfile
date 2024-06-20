# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

# Install pip requirements
COPY ./lululemon/requirements.txt /app/requirements.txt
COPY ./lululemon/start.sh /app/start.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
