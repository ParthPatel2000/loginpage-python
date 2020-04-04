import csv


def login(usrnm, passwd):
    newusr = True
    with open('mydb.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if usrnm == row['username']:
                # code for entering password here
                #
                if passwd == row['password']:
                    print('login complete')
                    newusr = False
                    return True
                    break
                else:
                    wrong_pass = 1
                    while wrong_pass < 3:
                        wrong_pass += 1
                        print('Wrong password, Renter the password for', usrnm, ':')
                        passwd = input()
                        if passwd == row['password']:
                            print('login complete')
                            newusr = False
                            return True
                            break
                    if wrong_pass == 3:
                        print('Wrong password was entered 3 times')
                        newusr = False
                        return False
                        break

        if newusr == True:
            print("username dosen't exist")
            newusr = input("New user? yes or no")
            if newusr == 'yes':
                signup(usrnm, passwd)
            elif newusr == 'no':
                return False


def signup(usrnm, passwd):
    usrexist = False
    header = ['username', 'password']
    with open('mydb.csv', 'r+', newline='') as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line['username'] == usrnm:
                print("username already Exist")
                login(usrnm, passwd)
                usrexist = True
                break
        if not usrexist:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerow({'username': usrnm, 'password': passwd})
            print("Signup complete")
            print('welcome', usrnm)


def changepass(usrnm, passwd):
    if login(usrnm, passwd):
        passwd = input("Enter the new Password")
        updated_dict = {}
        with open('mydb.csv', 'r+', newline='') as file:
            reader = csv.reader(file)
            update = dict(reader)
            update[usrnm] = passwd
        with open('mydb.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for key, values in update.items():
                writer.writerow([key, values])
            print("Password changed successfully")


def removing_duplicates():
    t = {}
    with open('mydb.csv', 'r+') as file:
        reader = csv.DictReader(file)
        # next(reader)
        for row in reader:
            key = row.pop('username')
            if key in t:
                continue
            t[key] = row['password']
    print(t)



