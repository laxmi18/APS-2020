#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int> vec[4];
    for(int i=1;i<=100;i++){
       for(int j=i+1;j<=100;j++){
         int x=__builtin_popcount(i)%2;
         int y=__builtin_popcount(j)%2;
         int in=0;
         in|=(x<<1);
         in|=(y<<0);
         int v=__builtin_popcount(i^j)%2;
         vec[in].push_back(v);
      }
    }
      for(int i=0;i<4;i++){
         for(int j=0;j<vec[i].size();j++) cout<<vec[i][j] << " ";
         cout << endl;
      }
   return 0;
}
