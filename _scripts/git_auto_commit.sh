cd `dirname "$0"`
cd ..

git pull
git add mt_report _data
git commit -m "daily report"
git push origin master

