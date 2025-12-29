1  ls
    2  mkdir devops
    3  ls
    4  ls -l
    5  cd devops/
    6  pwd
    7  histry
    8  touch newfile.txt
    9  ls
   10  cd ..
   11  ls
   12  touch myfile.txt
   13  ls
   14  ls 0l
   15  ls -l
   16  clear
   17  ls
   18  rm -f myfile.txt
   19  ls
   20  mkdir ck
   21  ls
   22  rm -f ck/
   23  rm -r ck/
   24  mkdir ck
   25  rmdir ck/
   26  ls
   27  cd devops/
   28  ls
   29  cd ..
   30  cat devops/newfile.txt
   31  echo "This i sthe my first file "
   32  echo "This i sthe my first file "> devops/newfile.txt
   33  cat devops/newfile.txt
   34  cd devops/
   35  head newfile.txt
   36  ls
   37  pwd
   38  ls
   39  touch ck.txt
   40  ls
   41  cp ck.txt /home/ubuntu/
   42  cd ..
   43  ls
   44  cd devops/
   45  ls
   46  mkdir cloud
   47  ls
   48  mv c
   49  mv ck.txt /cloud
   50  ls
   51  mv cloud/ LinuxCloud
   52  ls
   53  wc newfile.txt
   54  ls -l
   55  history
   56  1  ls
   57  ls
   58  echo "This is a my first file and this is the soft link line ">newfile.txt
   59  cat newfile.txt
   60  pwd
   61  ln -s /home/ubuntu/devops/newfile.txt  Soft-link-file
   62  ls
   63  ls -ltr
   64  cut -b 1 newfile.txt
   65  cut -b 1-4 newfile.txt
   66  vi myfile.txt
   67  cat myfile.txt
   68  ls
   69  df
   70  df -h
   71  free
   72  top
   73  du
   74  du .
   75  ls -a
   76  ls -al
   77  ps
   78  fuser
   79  free
   80  nohup free -h
   81  ls
   82  cat nohup.out
   83  nohup df -h
   84  cat nohup.out
   85  head nohup.out
   86  head -n 5 nohup.out
   87  tail -n 5 nohup.out
   88  vmstat
   89  vmstat -a
   90  history
   91 bash
    5  which git
    6  which cp
    7  id
    8  sudo
    9  cat /etc/passwd
   10  sudo shutdown
   11 sudo reboot
   11 apt
   12 yum
   13 dnf
   14 pacman 
   15 portage
   16 useradd
   17 whoami
   18 su - super user
   19 passwd
   20 userdel
   21 groupadd
   22 gpasswd -a, -m
   23 groupdel

   <!-- > file permission commands -->
   1 Umask
   2 is - l
   3 chmod
   4 chown command
   5 chgrp command
   
   <!-- > compression commads -->
   1 zip, gunzip, and gzip command
   2 tar, untar command
   
   <!-- > file transfer commad -->
   1 SCP command(copy file)
   2 rsync command



  1  ls
    2  exit
    3  sudo su
    4  ls
    5  pwd
    6  uname
    7  uptime
    8  date
    9  who
   10  whomi
   11  whoami
   12  which python
   13  bash
   14  which bash
   15  which git
   16  which cp
   17  id
   18  sudo
   19  cat /etc/passwd
   20  history
   21  apt
   22  sudo apt install python 3
   23  sudo apt install python
   24  sudo apr-get install python
   25  sudo apt-get install python
   26  sudo apt-get update
   27  sudo apt-get install python
   28  sudo apt install docker.io
   29  which docker
   30  sudo apt remove docker.io
   31  sudo useradd -m chhagankumawat
   32  cd ..
   33  ls
   34  sudo passwd chhagankumawat
   35  su chhagankumawat/
   36  su chhagankumawat
   37  whoami
   38  cat /etc/passwd
   39  sudo userdel chhagankumawat
   40  ls
   41  pwd
   42  sudo useradd ck
   43  sudo useradd ck1
   44  sudo useradd ck2
   45  sudo groupadd devops
   46  cat /etc/passwd
   47  cat /etc/group
   48  sudo gpasswd -a ck1 devops
   49  sudo gpasswd -a ubuntu devops
   50  cat /etc/group
   51  sudo groupadd tester
   52  cat /etc/group
   53  sudo gpasswd -m ck2, ck
   54  sudo gpasswd -m ck2, ck tester
   55  sudo gpasswd -m ck2,ck tester
   56  sudo gpasswd -M ck2,ck tester
   57  cat /etc/group
   58  id
   59  ls
   60  history
   61  ls -l
   62  chmod 777 devops
   63  chmod 777 devops/
   64  ls  -l
   65  history
   66  chmod 777 devops/
   67  sudo chmod 777 devops/
   68  ls -l
   69  sudo chmod 700 ck.txt
   70  ls -l
   71  ls
   72  history
   73  uamks
   74  umask
   75  cat .bashrc
   76  ls -l
   77  sudo chown ck ck.txt
   78  ls -l
   79  touch mk.php
   80  mkdir cloud
   81  ls
   82  which zip
   83  zip
   84  sudo apt istall zip
   85  sudo apt install zip
   86  ls
   87  ls devops/
   88  zip devops/
   89  zip -r devops.zip devops/
   90  zip -r dev.zip devops/
   91  sudo zip -r dev.zip devops/
   92  ls
   93  cd cloud/
   94  ls
   95  mkdir unzip
   96  ls
   97  pwd
   98  cd dev.zip cloud
   99  cd ..
  100  ls
  101  cd dev.zip cloud/unzip/
  102  cp dev.zip cloud/unzip/
  103  ls
  104  cd cloud/
  105  ls
  106  cd unzip/
  107  ls
  108  unzip dev.zip
  109  ls
  110  history
  111  ls
  112  tar -cvzf dev.tar.gz devops/
  113  ls
  114  pwd
  115  cd ..
  116  ls
  117  pwd
  118  cd cloud/
  119  cd unzip/
  120  ls
  121  cp dev.tar.gz /home/ubuntu/devops
  122  ls
  123  cd .. ..
  124  cd ../..
  125  ls
  126  cd devops/
  127  ls
  128  tar -xvzf dev.tar.gz
  129  ls
  130  cd ..
  131  ls
  132  cat HD05.pdf
  133  ls
  134  pwd
  135  cd ..
  136  ls -l
  137  cd ubuntu/
  138  ls
  139  history


 scp -i .\Ubuntu.pem .\ck1\ ubuntu@ec2-13-220-31-46.compute-1.amazonaws.com:/home/ubuntu  (file Local to server transfer)

 scp -i Ubuntu.pem -r ubuntu@ec2-13-220-31-46.compute-1.amazonaws.com:/home/ubuntu .  (file and server to local transfer)

 rsync -e " ssh -i Ubuntu.pem -avz /folder name/ ubuntu@ec2-13-220-31-46.compute-1.amazonaws.com:/home/ubuntu/


 1 ping
 2 netstate
 3 ifconfig
 4 mtr (My Trace route)
  ls
    2  exit
    3  sudo su
    4  ls
    5  pwd
    6  uname
    7  uptime
    8  date
    9  who
   10  whomi
   11  whoami
   12  which python
   13  bash
   14  which bash
   15  which git
   16  which cp
   17  id
   18  sudo
   19  cat /etc/passwd
   20  history
   21  apt
   22  sudo apt install python 3
   23  sudo apt install python
   24  sudo apr-get install python
   25  sudo apt-get install python
   26  sudo apt-get update
   27  sudo apt-get install python
   28  sudo apt install docker.io
   29  which docker
   30  sudo apt remove docker.io
   31  sudo useradd -m chhagankumawat
   32  cd ..
   33  ls
   34  sudo passwd chhagankumawat
   35  su chhagankumawat/
   36  su chhagankumawat
   37  whoami
   38  cat /etc/passwd
   39  sudo userdel chhagankumawat
   40  ls
   41  pwd
   42  sudo useradd ck
   43  sudo useradd ck1
   44  sudo useradd ck2
   45  sudo groupadd devops
   46  cat /etc/passwd
   47  cat /etc/group
   48  sudo gpasswd -a ck1 devops
   49  sudo gpasswd -a ubuntu devops
   50  cat /etc/group
   51  sudo groupadd tester
   52  cat /etc/group
   53  sudo gpasswd -m ck2, ck
   54  sudo gpasswd -m ck2, ck tester
   55  sudo gpasswd -m ck2,ck tester
   56  sudo gpasswd -M ck2,ck tester
   57  cat /etc/group
   58  id
   59  ls
   60  history
   61  ls -l
   62  chmod 777 devops
   63  chmod 777 devops/
   64  ls  -l
   65  history
   66  chmod 777 devops/
   67  sudo chmod 777 devops/
   68  ls -l
   69  sudo chmod 700 ck.txt
   70  ls -l
   71  ls
   72  history
   73  uamks
   74  umask
   75  cat .bashrc
   76  ls -l
   77  sudo chown ck ck.txt
   78  ls -l
   79  touch mk.php
   80  mkdir cloud
   81  ls
   82  which zip
   83  zip
   84  sudo apt istall zip
   85  sudo apt install zip
   86  ls
   87  ls devops/
   88  zip devops/
   89  zip -r devops.zip devops/
   90  zip -r dev.zip devops/
   91  sudo zip -r dev.zip devops/
   92  ls
   93  cd cloud/
   94  ls
   95  mkdir unzip
   96  ls
   97  pwd
   98  cd dev.zip cloud
   99  cd ..
  100  ls
  101  cd dev.zip cloud/unzip/
  102  cp dev.zip cloud/unzip/
  103  ls
  104  cd cloud/
  105  ls
  106  cd unzip/
  107  ls
  108  unzip dev.zip
  109  ls
  110  history
  111  ls
  112  tar -cvzf dev.tar.gz devops/
  113  ls
  114  pwd
  115  cd ..
  116  ls
  117  pwd
  118  cd cloud/
  119  cd unzip/
  120  ls
  121  cp dev.tar.gz /home/ubuntu/devops
  122  ls
  123  cd .. ..
  124  cd ../..
  125  ls
  126  cd devops/
  127  ls
  128  tar -xvzf dev.tar.gz
  129  ls
  130  cd ..
  131  ls
  132  cat HD05.pdf
  133  ls
  134  pwd
  135  cd ..
  136  ls -l
  137  cd ubuntu/
  138  ls
  139  history
  140  ping google.com
  141  netstat
  142  sudo install net-tools
  143  sudo apt install net-tools
  144  netstat
  145  ls
  146  tracerpoute youtube.com
  147  traceroute youtube.com
  148  sudo apt install traceroute
  149  which traceroute
  150  sudo apt install inetutils-traceroute
  151  traceroute youtube.com
  152  traceroute vtc3pl.com
  153  tracepath vtc3pl.com
  154  clear
  155  mtr
  156  mtr vtc3pl.com
  157  nslookup vtc3pl.com
  158  telnet vtc3pl.com:80
  159  telnet vtc3pl.com
  160  telnet vtc3pl.com 80
  161  hostname
  162  cat /tec/hosts
  163  cat /etc/hosts
  164  ip
  165  ip address show
  166  iwconfig
  167  sudo apt install wireless-tools
  168  iwconfig
  169  ss
  170  dig vtc3pl.com
  171  whois vtc3pl.com
  172  sudo apt install whois
  173  whois vtc3pl.com
  174  history
  175  arp
  176  ifplugstatus
  177  sudo apt install ifplugd
  178  ifplugstatus
  179  route
  180  curl
  181  curl -x https://ir-example.mir.prod.reco.microsoft.com/Reco/V1.0/New?modeling=adw&Count=5
  182  curl -x GET https://fake-json-api.mock.beeceptor.com/users
  183  mkdir download
  184  cd download/
  185  ls
  186  wget https://file-examples.com/wp-content/storage/2017/02/file-sample_100kB.doc
  187  ls
  188  cat file-sample_100kB.doc
  189  ls
  190  iptables
  191  iptabled
  192  sudo ip tables
  193  sudo ip table
  194  sudo ip table --list-rules
  195  sudo iptables --list-rules
  196  watch
  197  watch mtr
  198  watch top
  199  nmap
  200  sudo apt  install nmap


