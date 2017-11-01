# sendr
Spam automation from the command line

Usage:
After cloning this, you'll need to add three files to the sendr directory: a `password.json` file (containing the gmail account that we're sending emails from [it should be formatted like this: `{"accountname": "accountpass"}`]), a `payload.txt` file (containing the message to be sent to the recipient), and a `recipients.txt` file (containing the recipients, each on a newline).

Then run it by simply running the following command from the command line:
```
$ python3 main.py
```
And the program will print the emails out to the console as it sends them.

NOTE: Before running this for production, you must enable "less secure applications" in your gmail security preferences.

# TODO
* Add support for non-gmail accounts
* Add support for emails more complex than just plaintext
