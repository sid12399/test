import json


class Handler:


    def __init__(self, working_user):

        self.working_user = working_user


    def file_to_json_string(self, file):

        json_string = json.loads(file.read())

        return json_string


    def open_file(self):

        try:
            file = open("data.json", 'r')
            data = Handler.file_to_json_string(self, file)
            file.close()
            return data

        except IOError:
            print ("Filename invalid.")


    def save_to_file(self, json_string):

        file = open('data.json', 'w+')
        file.write(json_string)
        file.close()

    def get_password(self, website_name):

        data = Handler.open_file(self)

        try:
            return data['Users'][self.working_user][website_name]

        except:
            return ("Password not found.")


    def add_password(self, website, pwd):

        data = Handler.open_file(self)

        data['Users'][self.working_user][website] = pwd

        Handler.save_to_file(self, json.dumps(data))

        return ("User added successfully.")



    def find_user(self, username):

        data = Handler.open_file(self)

        return data['Users'].has_key(username)


    def del_pwd(self, website_name):

        data = Handler.open_file()

        data['Users'][self.working_user][website_name] = -1


    def add_user(self, master_pwd):

        data = Handler.open_file(self)

        print self.working_user
        data['Users'][self.working_user] = {"Master" : master_pwd}
        Handler.save_to_file(self, json.dumps(data))

        return ("Congratulations! Account successfully created.")
