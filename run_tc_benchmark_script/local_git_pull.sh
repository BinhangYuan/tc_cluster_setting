cd ~/tc_cluster_setting

if [ $# -eq 0 ]
then
  git pull
else
  token=$1
  git pull https://"${token}"@github.com/BinhangYuan/tc_cluster_setting.git
fi