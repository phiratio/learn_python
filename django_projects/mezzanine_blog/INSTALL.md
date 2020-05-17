sudo apt install mysql-server python-mysqldb mysql-client libmysqlclient-dev
install venv and activate it
pip install mezzanine
follow instructions from here https://pypi.org/project/mysqlclient/
sudo mysql -u root
create user 'user'@'localhost';
grant all privileges on *.* to 'user'@'localhost';
alter user 'user'@'localhost' identified by 'password';
mysql -u user -p
create database dbname;
update your databases config file (mezzanine got local one also!)
python manage.py createdb

Extra stuff:
python manage.py collecttemplate
rename templates -> tempdrafts
create templates inside theme app
