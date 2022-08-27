#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	cin>>t;
	while(t--){
		ll n;
		cin>>n;
		ll even_value = n/2,odd_value = n/2;
		if(n%2!=0){
			odd_value+=1;
		}
		cout<<2*(even_value*odd_value)<<endl;
		
	}
	return 0;

}