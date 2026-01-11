#Use official python image
FROM python:3.12-slim

#set working directory
WORKDIR /student

#Copy all files to container
COPY . .

#command to run python file
CMD ["python", "student_details.py"]