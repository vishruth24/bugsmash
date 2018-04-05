                    
#include <iostream>
using namespace std;

int main()
{
    long long k=0,i=0,n=0,a1=0,b1=0;
    cin>>n;
    long long a[n],b[n];
    for(i=0;i<n;i++)
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

        while(k<n-1)
        {
             a1+=a[k];
            b1+=b[k];
            cout<<a1<<" "<<b1<<endl;
            k++;
        }
       
    }
    else if(a1>b1)
    {
        cout<<a1<<endl;
        cout<<"0"<<" "<<b1-b[0]<<endl;

        a1=b1=0;
        a1+=a[0];
        cout<<a1<<" "<<"0"<<endl;

        while(k>n-1)
        {

         b1+=b[k];
            a1+=a[k];
            cout<<a1<<" "<<b1<<endl;
k++;
        }
       
    }

}



    
    
    
    
    