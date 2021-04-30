import csv
users = list(csv.reader(open("report.csv")))

required_emails = ""

names_list = required_emails.split(", ")

emails_list_emails = []
emails_list_names = []


for user in users: 
    user_name = user[2] + " " + user[3]

    if user_name in required_emails:
        emails_list_emails.append(user[4])
        emails_list_names.append(user_name)


for name in names_list:
    if name not in emails_list_names:
        emails_list_names.append(name)
        emails_list_emails.append("----")


file = open ("Emails.csv", "w")
i =0 
while i < len(emails_list_emails): 
    new_record = emails_list_names[i] + ", " + emails_list_emails[i] + "\n"
    file.write(new_record)
    i+=1

file.close()




