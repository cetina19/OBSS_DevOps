docker login -u alper.cetin -p AlperCetin2023 https://a16762aee6ff5485281190329b6c4efd-433642122.us-east-1.elb.amazonaws.com/
echo 'login successfull'
docker save -o ./temporary/source.tar a16762aee6ff5485281190329b6c4efd-433642122.us-east-1.elb.amazonaws.com/internship/alper_halis_case1_source:latest
docker tag alper_halis_case1_source:latest
docker push a16762aee6ff5485281190329b6c4efd-433642122.us-east-1.elb.amazonaws.com/internship/alper_halis_case1_target:latest
echo 'image1 is pushed'