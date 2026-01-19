#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		vector<ll>arr1(n);
		vector<ll>arr2(n);
		for(int i=0;i<n;i++){
			cin>>arr1[i];
		}
		ll x=0,y=0;
		for(int i=0;i<n;i++){
			cin>>arr2[i];
			x+=(arr1[i]-arr2[i]);
			y+=abs(arr1[i]-arr2[i]);
		}
		if(x!=0) cout<<-1<<endl;
		else if(y%2!=0) cout<<-1<<endl;
		else cout<<y/2<<endl;
	}
	return 0;

}