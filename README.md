# test-QA

# How to run this test
* Make sure you have `python3-venv` installed. If you don`t, follow the instructions on the link --> https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/
* Create a virtual environment under /test-QA
```
python3 -m venv ./venv
```
* Activate the virtual environment
```
source venv/bin/activate
```
* Install the requirements
```
pip install -r requirements.txt
```
* Download geckodriver and copy it to the PATH /venv/bin
* Open terminal in /BBD folder and run behave
```
behave
```
