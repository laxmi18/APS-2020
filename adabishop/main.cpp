#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, x, y;
	cin >> t;
	for (int i=0;i<t;i++){
	    cin >> x;
	    cin >> y;
	}
	int arr[]={1,7,2,8,8,2,7,1,4,4,1,1,2,2,1,3,3,1,4,2,5,1,1,5,4,8,8,4,6,6,8,8,7,7,6,8,8,6};
	int z=19;
	if(x==4&&y==4){
	    cout << z << endl;
	    for(int k=0;k<=37;k+=2){
	        cout << arr[k] << ' '<< arr[k+1] << endl;
	    }
	}
	else if(x==y && x!=4){
	    cout << z+1 << endl;
	    cout << 4 << ' '<< 4 << endl;
	    for(int k=0;k<=37;k+=2){
	        cout << arr[k] << ' '<< arr[k+1] << endl;
	    }
	}
	else if(x+y==8 && x!=4){
	    cout << z+1 << endl;
	    cout << 4<< ' '<<4 << endl;
	    for(int k=0;k<=37;k+=2){
	        cout << arr[k]<< ' '<< arr[k+1] << endl;
	    }
	}
	else{
	    cout << z+2 << endl;
	    cout << int((x+y)/2)<< ' '<<int((x+y)/2) << endl;
	    cout << 4<< ' '<<4 << endl;
	    for(int k=0;k<=37;k+=2){
	        cout << arr[k]<< ' '<< arr[k+1] << endl;
	    }
	}
	return 0;
}
