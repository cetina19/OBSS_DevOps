mem=$(sshpass -pCLmngSys34 ssh -p 8022  int1-devops@int1-devops.obss.io uptime | echo $(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }'))
disk=$(sshpass -pCLmngSys34 ssh -p 8022  int1-devops@int1-devops.obss.io uptime | echo $(df -h | awk '$NF=="/"{printf "%.2f", $5}'))
ram=$(sshpass -pCLmngSys34 ssh -p 8022  int1-devops@int1-devops.obss.io uptime | echo $(free | awk '/Mem/{printf("%.2f"), $3/$2*100}'| awk '{print $3}' | cut -d. -f1))

memUsage=$(printf "%.0f" "$mem")
diskUsage=$(printf "%.0f" "$disk")
ramUsage=$(printf "%.0f" "$ram")

threshold=$1

if [[ $memUsage -lt $threshold || $diskUsage -lt $threshold || $ramUsage -lt $threshold ]]; then
  echo "Don't send email."

else
  sender="alper8540@gmail.com"
  receiver="alper8540@gmail.com"
  password="jlyjvfrdkaurezwn"

  subject="testing"

  echo "testline1\ntestline2\ntestline3" > tempfile.txt                
  body=$(cat tempfile.txt)         

  rm tempfile.txt

  if [ -z "$2" ]; then 


      curl -s --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
      --mail-from $sender \
      --mail-rcpt $receiver\
      --user $sender:$password \
      -T <(echo -e "From: ${sender}
  To: ${receiver}
  Subject:${subject}

  ${body}")

  else

      file="$2"
      
      MIMEType=`file --mime-type "$file" | sed 's/.*: //'`
      curl -s --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
      --mail-from $sender \
      --mail-rcpt $receiver\
      --user $sender:$gapp \
      -H "Subject: $sub" -H "From: $sender" -H "To: $receiver" -F \
      '=(;type=multipart/mixed' -F "=$body;type=text/plain" -F \
        "file=@$file;type=$MIMEType;encoder=base64" -F '=)'
      
  fi
fi