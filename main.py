import smtplib
import sys
import json

def get_logon(jsonfile):
    d = json.load(open(jsonfile))
    account = list(d.keys())[0]
    password = d[account]
    return (account, password)

def main():
    account, password = get_logon('password.json')
    print(account,password)
    with open('payload.txt', 'r') as f:
        f = f.read()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(account, password)
        for recipient in open('recipients.txt', 'r'):
            print("Sending msg: {} to acct: {}".format(f, recipient))
            server.sendmail(account, recipient, f)
    server.quit()

if __name__ == '__main__':
    main()