https://stackoverflow.com/questions/9510474/pip-uses-incorrect-cached-package-version-instead-of-the-user-specified-version
https://stackoverflow.com/questions/27308288/uwsgi-unrecognized-option-https
sudo apt install libssl-dev
then
#pip install uwsgi
pip install uwsgi --force-reinstall --no-cache-dir
