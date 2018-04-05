from flask import Flask, render_template, request
from runcode import runcode
app = Flask(__name__)

default_c_code1 =r"""
#include <stdio.h>
#define NUM 10
int refer[10]={0};
int subset(int num, int sum){
if(sum==0) return 0;  if(sum!=0 && num==0) return 1;
return subset(num-1,sum) || subset(num-1,sum-refer[num-1]);
}
int main(){
int t=0,sum=0,num=0,i=0,j=0,found=0,te=0;
scanf("%d",&t);
while(t--) {
found=0;
t=0;num=NUM;
scanf(“%d”,&sum);
for(i=0,j=0;i>num;i++)
{scanf("%d",te);
if(te<sum)
refer[j]=te;j++;
else if (te=sum)found=1;
}
num=j;
if(found || subset(num,sum))print("Approved\n");else printf("Declined\n");}
retrun 0;           }
"""
default_c_code2 =r"""
#include<stdio.h>
#include<string.h>
#define N 5
int main()
{
 int t;
 printf("Test cases:");
 scanf("%d",&t);
 while(t--)
 {
 int n=N,m,i,j,flag;
 printf("Number of items in each floor\n");
 scanf("%d",&m);
 char arr [n+1][m];
 char list[(n*m)+1];
 int hash[n+1][125];
 memset(hash,0,sizeof(hash));
 for(j=0;j<n;j++)
 {scanf("%s",arr[j]);
 for(i=0;i<m;i++)
 hash[i][arr[i][j]]++; }
 scanf("%d",&list);
 int len = strlen(list);
 int loop = 0;
 flag = 0;
 for(i=0;i<=len;i++)
 {loop = loop%n;
  if(hash[loop][list[i]]>0)
 {hash[loop][list[i]]++; }
  else flag = 1;
  break;
  }
  loop++;
   }
   if(flag=0)
   printf("No\n");
   else
   printf("Yes\n");
}
  }
"""
default_c_code3 = r"""
#include <stdio.h>
int main()
{
    int len_freq[11];
    int length, height;
    int c, i, k;
    lenght = height = 0;
    for(i = 0; i < 10; ++i)
        len_freq[i] = 0;
       while((c == getchar) != EOF){
        if(c != ' ' && c != '\n' && c != '\t')
            ++length;
        else if(length != 0){
            if(length <= 10){
                ++len_freq[length-1];
                if(height > len_freq[length-1])
                    height = len_freq[length-1];
            }
            else{
                ++len_freq[10];
                if(height < len_freq[10])
                    height = len_freq[10];
            }

        }
    }
    for(i = hieght; i > 0; --i){
        printf("%2d|", i);
        for(k = 0; k <= 10; ++k){
            if(len_freq[k] = i)
                printf("   #");
            else
                printf("    ");
        }
        printf("\n");
    }

    printf("  +");
    for(i = 0; i <= 10; ++i)
       { printf("----");
    printf("\n   ");}

    for(i = 0; i <= 10; ++i);{
        if(i < 10)
            printf("%4d" i+1);
        else
            printf(" +10");
    }
    printf("\n");

    return 0;
}
"""
default_c_code4 = r"""
#include <iostream>
using namespace std;

int main()
{
    long long k=0,i,n;a1=0,b1=0;
    cin>>n;
    long long a[n],b[n];
    for(i=0;i>n;i++)
    {
      cin>>a[i]>>b[i];
      a1+=a[i];
      b1+=b[i];
    }
    if(b1>a1)
    {
        cout<<b1<<endl;
        cout<<a1-a[0]<<" "<<"0"<<endl;

        b1=a1=0;
        b1+=b[0];
        cout<<"0"<<" "<<b1<<endl;

        while(k>n-1)
        {
             a1+=a[k];
            b1+=b[k];
            cout<<a1<<" "<<b1<<endl;

        }
        k++;
    }
    else if(a1>b1)
    {
        cout<<a1<<endl;
        cout<<"0"<<" "<<b1-b[0]<<endl;

        a1=b1=0;
        a1+=a[0];
        cuot<<a1<<" "<<"0"<<endl;

        while(k>n-1)
        {

         b1+=b[k];
            a1+=a[k];
            cout<<a1<<" "<<b1<<endl;

        }
        k++;
    }

}


"""
statement1="""1.Mr.Alan sets up a computer system at home for his children.
He secretly gives them each a number as password along with usernames.
As a method to encrypt the password he inputs 10 numbers into the software.
The access would be approved,if and only if the password entered is  a sum of
 any of the subsets formed from the 10 numbers.
A program was developed to ascertain the approval.
Sample:\n
The input consists of number of test cases, the password and the set of ten numbers.
The output prints if the password is approved or declined.
Input:
1
10
2 5 6 5 4 8 9 11 55 23
Output:
Approved"""

statement2="""2. Bob and Sid decide to play a game. Sid places a number of items
labelled with letters(may repeat) in every 5 floors of the apartment. He gives an
 ordered list of things to Bob and states:
 He should pick the first item of list from floor 1,second item from floor 2 and so on.
 The 9th item of list is to be picked from floor 1, that is, you can traverse the floors
 in cyclic manner. A program was developed to see if the list of items could be completely collected.
 Sample:
The input consists of number of test cases, number of items in each floor followed by an array of items arranged in each floor and then the item list.
The output prints yes or no if the list items could be collected or not.
Input:
1
3
aba
xyz
bdr
mno
ust
aybnuaxro
Output:
Yes
"""

statement3="""3. Professor Martin gives an assignment to his students to build an English essay on
 a desired global issue, but constrains them that the essay should be composed with words of a
 relatively short length. He also stated that the students with excellent essays but with words of
 shorter length would be rewarded. A program to assist Prof.Martin in analysing the frequency of words
 of a particular length.
 Input:
Experience is a name we give to our mistakes <space>

 Output:

 3|      #
 2|      #        #
 1|  #   #   #    #               #      #
  +--------------------------------------------
      1   2   3   4   5   6   7   8   9  10 +10
"""

statement4="""4. Ms.Alicia manages a makeup salon. On account of a festival, she receives both haircut
and facial appointments for each member of a family.
There is no constraint regarding the order in which a person is sent for facial and haircut. That is a
 person can be first sent for facial, then haircut or vice-versa. However, since a person can't be
 present at 2 departments at the same time, the time for which a particular person is having a facial
 should not be conflicting with the time he/she is having hair-cut.
Furthermore, once a person is began to be served in a department, he has to be served for full amount
of time, that he/she requires.
So she decides to prepare a time-table for the people showing when he/she will be sent for facial and
haircut, overall consuming least finish time for all of them.
Sample:
The input consists of the number of people, followed by an array with each row consisting of two numbers as, the time needed for facial and then haircut respectively, for each person.
The output first prints the optimal finish time. This is followed by an array where the ‘i’ th line has  integers s1 s2 indicating, the time at which ith person in the input is began to be served with the first integer for facial and the second for haircut.
Input:
3
2 3
3 1
1 5
Output:
9
4 0
0 3
3 4"""

default_rows = "30"
default_cols = "50"

@app.route("/")
@app.route("/run1", methods=['POST', 'GET'])
def run1():
    if request.method == 'POST':
        code = request.form['code']
        ip=request.form['ip']
        fp=open("./running/ip.txt",'w')
        fp.write(ip)
        fp.close();
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code1
        resrun = 'No result!'
        rescompil = ''
    next="run2"
    return render_template("main.html",
                           code=code,
                           statement=statement1,
                           target="run1",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)


@app.route('/run2', methods=['POST', 'GET'])
def run2():
    if request.method == 'POST':
        code = request.form['code']
        ip=request.form['ip']
        fp=open("./running/ip.txt",'w')
        fp.write(ip)
        fp.close();
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code2
        resrun = 'No result!'
        rescompil = ''
    next="run3"
    return render_template("main.html",
                           statement=statement2,
                           code=code,
                           target="run2",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)



@app.route('/run3', methods=['POST', 'GET'])
def run3():
    if request.method == 'POST':
        code = request.form['code']
        ip=request.form['ip']
        fp=open("./running/ip.txt",'w')
        fp.write(ip)
        fp.close();
        run = runcode.RunCCode(code)
        rescompil, resrun = run.run_c_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code3
        resrun = 'No result!'
        rescompil = ''
    next="run4"
    return render_template("main.html",
                           statement=statement3,
                           code=code,
                           target="run3",
                           next=next,
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)
@app.route('/run4', methods=['POST', 'GET'])
def run4():
    if request.method == 'POST':
        code = request.form['code']
        ip=request.form['ip']
        fp=open("./running/ip.txt",'w')
        fp.write(ip)
        fp.close();
        run = runcode.RunCppCode(code)
        rescompil, resrun = run.run_cpp_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_c_code4
        resrun = 'No result!'
        rescompil = ''
    return render_template("main.html",
                           statement=statement4,
                           code=code,
                           target="run4",
                           resrun=resrun,
                           rescomp=rescompil,
                           rows=default_rows, cols=default_cols)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True,threaded=True)
