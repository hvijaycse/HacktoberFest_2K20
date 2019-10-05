#include <stdio.h>
#include <stdlib.h>
// constants
#define PAYRATE 12.00
#define TAXRATE_300 .15
#define TAXRATE_150 .20
#define TAXRATE_REST .25
#define OVERTIME 40

int main()
{ // Declare variables
    int hours=0;
    double GrossPay=0;
    double Taxes=0;
    double NetPay=0;

    printf("No of working hours in a week :");

    scanf("%d", &hours);

// Calculate GrossPay
    if(hours<=40)
    {
        GrossPay=hours*PAYRATE;
    }
    else
    {
        GrossPay=40*PAYRATE;
        double OverTime=(hours-40)*(PAYRATE*1.5);
        GrossPay+=OverTime;
    }

    // Calculate Taxes

    if(GrossPay<=300)
    {
        Taxes=GrossPay*TAXRATE_300;
    }
    else if(GrossPay>300 && GrossPay<=450)
    {
        Taxes=300*TAXRATE_300;
        Taxes+=(GrossPay-300)*TAXRATE_150;
    }

    else if(GrossPay>450)
    {
        Taxes=300*TAXRATE_300;
        Taxes+=150*TAXRATE_150;
        Taxes+=(GrossPay-450)*TAXRATE_REST;
    }




    NetPay=GrossPay-Taxes;

    printf("Grosspay are %.2f\n", GrossPay);
     printf(" Taxes are %.2f\n", Taxes);
      printf("Netpay are %.2f\n", NetPay);



    return 0;
}
