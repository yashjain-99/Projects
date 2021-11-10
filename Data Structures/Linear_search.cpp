#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
int linearsearch(int arr[],int n, int k){
for (int i=0;i<n;i++){
    if(arr[i]==k){
        return i;
    }
}
return -1;
}
int main(){
int n;
int k;
int x;
cout<<"enter size of array:"<<endl;
cin>>n;
int arr[n];
cout<<"enter array elements"<<endl;
for (int i=0;i<n;i++){
    cin>>arr[i];
}
cout<<"enter element to search"<<endl;
cin>>k;
x=linearsearch(arr,n,k);
if(x==-1){
    cout<<"Element is not there"<<endl;

}
else{
cout<<"element "<<k<<" is at index: "<<x;
}
}
