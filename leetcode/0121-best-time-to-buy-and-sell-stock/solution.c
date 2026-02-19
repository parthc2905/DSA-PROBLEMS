int maxProfit(int* prices, int pricesSize) {
    int buyPrice = prices[0], profit = 0 ;
    
    for(int i=1;i<pricesSize;i++){
        if (buyPrice>prices[i]){
            buyPrice  = prices[i];
        }
        profit = fmax(profit,prices[i]-buyPrice);
    }
    return profit;

}
