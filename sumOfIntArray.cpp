#include<iostream>
using namespace std;
int main(){
  int n, sum=0;
printf("Type the number of integers, n=  ");
cin>>n;
int arr[n];
cout<<"Type "<<n<<" integers"<<endl;

//taking input from user
for(int i=0;i<n;i++)
cin>>arr[i]; //storing in array 


  for(int i=0;i<n;i++){
    sum+=arr[i]; //Calculating some 
       }

//output
cout<<"The sum of the integers is "<<sum<<endl;
return 0;
}
