#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		ll n;
		cin>>n;
		vector<int>vec;
		bool find = false;
		for(int i=1;i<=sqrt(n);i++)
		{
			if((n-2*i)%(2+i)==0 && 2*i!=n){
				find = true;
				break;
			}
		}
		if(find==true){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}


	}
	return 0;

}