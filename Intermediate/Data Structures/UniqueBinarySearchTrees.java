class UniqueBinarySearchTrees{
    public int numTrees(int n)
    {
      int [] dp=new int[n+1];
        dp[0]=0;
        dp[1]=1;
        for(int i=2;i<=n;i++)
        {
            dp[i]+=dp[i-1]*dp[n-i];
        }
        System.out.println(dp[2]);
        return dp[n];
    }
}
