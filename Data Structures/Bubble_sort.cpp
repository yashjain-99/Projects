#include<iostream>
using namespace std;
void bs(int a[])
{
int i,j,temp;
for(i = 0; i<10; i++) {
        for(j = i+1; j<10; j++)
        {
            if(a[j] < a[i])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
cout <<"Sorted Element List \n";
for(i = 0; i<10; i++) {
   cout <<a[i]<<"\t";
}
}
int main ()
{
   int i;
   int a[10] = {4,7,2,9,8,1,3,5,6,10};
   cout <<"Input list ";
   for(i = 0; i<10; i++) {
      cout <<a[i]<<"\t";
   }
cout<<endl;
bs(a);
return 0;
}
