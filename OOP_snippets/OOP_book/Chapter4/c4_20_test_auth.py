try:
    import OOP_book.Chapter4.c4_19_authorizor as auth
except ModuleNotFoundError as e:
    import c4_19_authorizor as auth
finally:
    print('Play around bob/password')

# Set up a test user and permission
try:
    auth.authenticator.add_user("bob", "password")
    auth.authorizor.add_permission("test program")
    auth.authorizor.add_permission("change program")
    auth.authorizor.permit_user("test program", "bob")
except Exception as e:
    print('Test user and permissions already initialized, play with them')


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "password": self.change_password,
            "quit": self.quit,
            "logout": self.logout
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(
                    username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def logout(self):
        if auth.authenticator.is_logged_in(self.username):
            auth.authenticator.logout(self.username)
        else:
            print('Not logged in.')

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(
                permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(
                e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def change_password(self):
        if auth.authenticator.is_logged_in(self.username):
            auth.authenticator.change_password(self.username)
        else:
            print('log in first')
            self.login()

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
\tPlease enter a command:\n
\tlogin         Login
\tlogout        Logout
\ttest          Test the program
\tchange        Change the program
\tpassword      Change your password
\tquit          Quit
""")
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(
                        answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


Editor().menu()
