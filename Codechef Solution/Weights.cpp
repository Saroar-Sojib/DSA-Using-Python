#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	cin>>t;
	while(t--){
		ll x,a,b,c;
		cin>>x>>a>>b>>c;
		if (x==a or x==b || x==c){
			cout<<"YES"<<endl;
		}
		else if((a+b)==x || (a+c)==x || (a+b+c)==x || (b+c)==x)
		{
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
	return 0;

}