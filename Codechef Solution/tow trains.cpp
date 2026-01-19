#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		vector<int>vec,temp;
		vec.push_back(0);
		temp.push_back(0);
		int sum =0;
		for(int i=0;i<n-1;i++)
		{
			int k;
			cin>>k;
			sum+=k;
			vec.push_back(sum);
			temp.push_back(k);
		}
		for(int i=0;i<n-1;i++){
			int dif = vec[i+1]-temp[i];
			if (dif>0){
				temp[i+1]+=temp[i]+dif;
			}
			else{
				temp[i+1]+=temp[i];
			}

		}
		cout<<temp[n-1]<<endl;
	}
	return 0;

}