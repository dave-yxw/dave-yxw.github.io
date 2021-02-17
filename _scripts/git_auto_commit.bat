cd /d %~dp0
cd ..

python _scripts/daily_build.py

git pull
git add mt_report _data

git commit -m "daily report"
git push origin master

