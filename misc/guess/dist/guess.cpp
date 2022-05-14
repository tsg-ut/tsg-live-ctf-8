#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <linux/unistd.h>
#include <unistd.h>
#include <iostream>
#include <string>
#include <thread>
#include <cstdlib>
#include <chrono>

void win(){
  using namespace std;
  cout<<"you win!\n"<<getenv("FLAG")<<endl;
  cout.flush();
  syscall(__NR_exit_group, 0);
}

void guess_checker(std::string s){
  using namespace std;
  cerr<<"Got:"<<s<<endl;
  int fd = open("/tmp/password",O_RDONLY);
  if(s.size()>20){
    close(fd);
  }
  if (!(fcntl(fd, F_GETFL) < 0)) {
    system("pwgen 50000 -s -1 -N1|tail -c 20 > /tmp/password");
    string pass;
    char c;
    while(read(fd,&c,1)==1&&c!='\n'){
      pass+=c;
    }
    cerr<<"Expected:"<<pass<<endl;
    if(s==pass){
      win();
    }
  }else{
    cout<<"Wrong Password"<<endl;
    cout.flush();
    this_thread::sleep_for(chrono::microseconds(500));
  }
  close(fd);
}
int main(int argc, char const* argv[])
{
  system("touch /tmp/password");
  using namespace std;
  while(true){
    cout<<"guess password:";
    cout.flush();
    string s;
    getline(cin,s);
    thread(guess_checker,s).detach();
  }
  return 0;
}
