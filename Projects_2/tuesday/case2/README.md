# Week 3 Monday

# Output

Started by user alper_cetin
Obtained Jenkinsfile from git http://52.59.214.22/alper-cetin/simpleapp.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/cpp_pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
The recommended git tool is: NONE
using credential a07b1468-6e90-44d2-985d-c82791ef8770
 > /usr/bin/git rev-parse --resolve-git-dir /var/jenkins_home/workspace/cpp_pipeline/.git # timeout=10
Fetching changes from the remote Git repository
 > /usr/bin/git config remote.origin.url http://52.59.214.22/alper-cetin/simpleapp.git # timeout=10
Fetching upstream changes from http://52.59.214.22/alper-cetin/simpleapp.git
 > /usr/bin/git --version # timeout=10
 > git --version # 'git version 2.30.2'
using GIT_ASKPASS to set credentials 
 > /usr/bin/git fetch --tags --force --progress -- http://52.59.214.22/alper-cetin/simpleapp.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > /usr/bin/git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision a9a1ae9b3d951ccdb27d7273cfc02f06a20e3077 (refs/remotes/origin/main)
 > /usr/bin/git config core.sparsecheckout # timeout=10
 > /usr/bin/git checkout -f a9a1ae9b3d951ccdb27d7273cfc02f06a20e3077 # timeout=10
Commit message: "Dockerization"
 > /usr/bin/git rev-list --no-walk 72c91f584550bf508d1ab1608e13416c758e15a2 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Connecting the branch)
[Pipeline] git
The recommended git tool is: NONE
using credential gitlabID
 > /usr/bin/git rev-parse --resolve-git-dir /var/jenkins_home/workspace/cpp_pipeline/.git # timeout=10
Fetching changes from the remote Git repository
 > /usr/bin/git config remote.origin.url http://52.59.214.22/alper-cetin/simpleapp.git # timeout=10
Fetching upstream changes from http://52.59.214.22/alper-cetin/simpleapp.git
 > /usr/bin/git --version # timeout=10
 > git --version # 'git version 2.30.2'
using GIT_ASKPASS to set credentials 
 > /usr/bin/git fetch --tags --force --progress -- http://52.59.214.22/alper-cetin/simpleapp.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > /usr/bin/git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision a9a1ae9b3d951ccdb27d7273cfc02f06a20e3077 (refs/remotes/origin/main)
 > /usr/bin/git config core.sparsecheckout # timeout=10
 > /usr/bin/git checkout -f a9a1ae9b3d951ccdb27d7273cfc02f06a20e3077 # timeout=10
 > /usr/bin/git branch -a -v --no-abbrev # timeout=10
 > /usr/bin/git branch -D main # timeout=10
 > /usr/bin/git checkout -b main a9a1ae9b3d951ccdb27d7273cfc02f06a20e3077 # timeout=10
Commit message: "Dockerization"
[Pipeline] echo
Branch connection is established
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build the app)
[Pipeline] sh
+ g++ simpleapp.cpp -o simpleapp
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test the app)
[Pipeline] sh
+ chmod +x simpleapp
[Pipeline] sh
+ ./simpleapp Alper 100 10 2 n
sh: 1: cls: not found
sh: 1: cls: not found

		========WELCOME TO CASINO WORLD=======



What's your Name : 

Enter the starting balance to play game : $		======CASINO NUMBER GUESSING RULES!======
	1. Choose a number between 1 to 10
	2. Winner gets 10 times of the money bet
	3. Wrong bet, and you lose the amount you bet



Your current balance is $ 100
Hey, Alper, enter amount to bet : $Guess any betting number between 1 & 10 :Oops, better luck next time !! You lost $ 10

The winning number was : 3

Alper, You have balance of $ 90


-->Do you want to play again (y/n)? 




Thanks for playing the game. Your balance is $ 90

[Pipeline] sh
+ ./simpleapp Alper 200 10 8 n
sh: 1: cls: not found
sh: 1: cls: not found

		========WELCOME TO CASINO WORLD=======



What's your Name : 

Enter the starting balance to play game : $		======CASINO NUMBER GUESSING RULES!======
	1. Choose a number between 1 to 10
	2. Winner gets 10 times of the money bet
	3. Wrong bet, and you lose the amount you bet



Your current balance is $ 200
Hey, Alper, enter amount to bet : $Guess any betting number between 1 & 10 :Oops, better luck next time !! You lost $ 10

The winning number was : 3

Alper, You have balance of $ 190


-->Do you want to play again (y/n)? 




Thanks for playing the game. Your balance is $ 190

[Pipeline] sh
+ ./simpleapp Alper 20 10 5 n
sh: 1: cls: not found
sh: 1: cls: not found

		========WELCOME TO CASINO WORLD=======



What's your Name : 

Enter the starting balance to play game : $		======CASINO NUMBER GUESSING RULES!======
	1. Choose a number between 1 to 10
	2. Winner gets 10 times of the money bet
	3. Wrong bet, and you lose the amount you bet



Your current balance is $ 20
Hey, Alper, enter amount to bet : $Guess any betting number between 1 & 10 :Oops, better luck next time !! You lost $ 10

The winning number was : 4

Alper, You have balance of $ 10


-->Do you want to play again (y/n)? 




Thanks for playing the game. Your balance is $ 10

[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Dockerize the app)
[Pipeline] sh
+ docker build --rm -f Dockerfile.yml -t dockercpp:latest .
#2 [internal] load build definition from Dockerfile.yml
#2 sha256:3dc1521b1a03081e49f7108df10e0576c1acecbd39951313fc6da01bbc30dafd
#2 transferring dockerfile: 177B done
#2 DONE 0.1s

#1 [internal] load .dockerignore
#1 sha256:596cee33501bd833e404dd660b3dd7909501ca5aab78379d78fac603a41d3242
#1 transferring context: 2B done
#1 DONE 0.1s

#3 [internal] load metadata for docker.io/library/gcc:10.2
#3 sha256:4ba732196c314cdfb0e307402cfe46b31001f63ee5325a802eac66a3a854d817
#3 DONE 6.3s

#8 [1/4] FROM docker.io/library/gcc:10.2@sha256:c448e92bcadb9dce6a23b9672df25fb5aec490222d78a32199857a49215a1d69
#8 sha256:19b0433b561e868d9d883066388a7a893d06a97ed82aa20d226c5d830884ef32
#8 resolve docker.io/library/gcc:10.2@sha256:c448e92bcadb9dce6a23b9672df25fb5aec490222d78a32199857a49215a1d69 0.1s done
#8 ...

#7 [internal] load build context
#7 sha256:27217a9537971b4d445200daffafb7924c3b7c9755066defc3e7edfc3045f4e3
#7 transferring context: 263.56kB done
#7 DONE 0.2s

#8 [1/4] FROM docker.io/library/gcc:10.2@sha256:c448e92bcadb9dce6a23b9672df25fb5aec490222d78a32199857a49215a1d69
...
...
#8 DONE 607.3s

#6 [2/4] COPY . /usr/src/dockertestcpp
#6 sha256:ac6c7f457f5c73980e8f103316e00f56fd68b97e7a69eb6bf2917ee0b2e24e9b
#6 DONE 5.5s

#5 [3/4] WORKDIR /usr/src/dockertestcpp
#5 sha256:4f713cfb18c7f8343621ab6ba62ceae41b47d8e5421b75c90a327c1f802a0b14
#5 DONE 0.2s

#4 [4/4] RUN g++ -o simpleapp simpleapp.cpp
#4 sha256:9358892425dd665e6ab6511b7887eae1cc86f6b011ed9dc68aea963d9783822b
#4 DONE 0.8s

#9 exporting to image
#9 sha256:a4075ccb5567dddd53435eac98c773ec2c14f6e7a422f3cf9fc17f760587a344
#9 exporting layers
#9 exporting layers 0.3s done
#9 writing image sha256:242ede38fea26e2a8f6f2b02ce038a05bf9e8cafbc567d3bfeb9b1c69b9b1e3c 0.0s done
#9 naming to docker.io/library/dockercpp:latest 0.0s done
#9 DONE 0.3s
[Pipeline] echo
Dockerized
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS