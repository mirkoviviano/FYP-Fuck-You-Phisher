# FYP - Fuck You Phisher

I really hate phishing. With this tool you can send multiple fake emails and password to phishers. It executes HTTP POST requests on the web page you are supposed to enter your real credentials. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You will need Python > 3.5.x and these modules
* requests
* glob
* itertools
* random
* string

### Installing

Clone the repository by typing 


```
git clone https://github.com/mirkoviviano/FYP-Fuck-You-Phisher.git
```
or downloading the ZIP.

### Execution

Type
``` 
python FYP.py
```
and it will ask you for parameters.

### Parameters
You need the name value of the HTML input on the phisher website. 
For example:
``` 
<input type="text" name="email_address" placeholder="Email"/>
```
"email_address" is what you are looking for. Do the same with password. 

You can find these two paramenters either looking in the HTML or ispecting the Network request.

## Built With

* [Python](https://www.python.org/)

## Contributing and support

Feel free to contribute and give me tips. I am here to learn.

Support me on 
	[![ko-fi](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/P5P7KJLY)
    or
	[![Patreon](https://ibb.co/efShm9)](https://www.patreon.com/mirkoviviano)

## Authors

* **Mirko Viviano** - [https://github.com/mirkoviviano](https://github.com/mirkoviviano)