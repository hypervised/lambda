# lambda

# To build the zip file that contains the pre-compiled modules do the following:

docker run -v /some/path/on/your/mac:/mnt -it amazonlinux:latest /bin/bash
yum upgrade -y
yum install python3 -y
yum install zip -y
python3 -m venv function-env
ls function-env/lib/python3.7/site-packages/
source function-env/bin/activate
pip3 list -l
pip3 install prettytable 
pip3 list -l
deactivate
cd /function-env/lib/python3.7/site-packages
zip -r9 /mnt/rps.zip .
Ctrl d to exit and kill container
zip -g rps.zip rock_paper_scissors.py

# To setup the lambda function:

Create a new python 3.7 lambda function
add the env var OPPONENT and set it to sassy kind or yoda
set the Handler to rock_paper_scissors.lambda_handler
set the timeout to 10 seconds
create a test event using the format below
{
	"round1": "rock",
	"round2": "paper",
	"round3": "scissors"
}
