cd `dirname "$0"`
cd ..

git pull
python _scripts/daily_build.py
git add mt_report _data

git commit -m "daily report"
git push origin master

