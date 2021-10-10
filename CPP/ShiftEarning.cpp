//using c++ and please explain to me the calculation.
//Write a program that computes the earnings per shift for a security guard. A security guard charges $15 per hour before midnight and $20 after midnight. The program reads the starting time in hours and minutes and the ending time in hours and minutes. All times are between 6:00 pm, and 5:59 am, using a 12-hour clock. For example, you should consider hour 8 as 8 pm and hour 2 as 2am.
//The program should check the validity of the inputs as follows.
//1) Hours are from 0-11 (0 for midnight).
//2) Minutes are from 0-59.
//3) The start time must be before midnight.
//4) The end time must be after the start time.
//The program should display specific warnings regarding the above when the user submits invalid input; the program should prompt the user to re-enter the times again. The program should output the total hours worked and the total earnings per shift.
//Example: >7h 0m to 2h 0m You have worked 7 hours in this shift, earning $115.

#include <iostream>  // standard input and output library
using namespace std;
//main function
int main(){
    int hour, mints, endhour, endmints;  //taking user input from user about shift time
    cout<<"Input starting hours: ";
    cin>> hour;
    cout<<"Input starting minutes: ";
    cin>> mints;

    cout<<"\nInput ending hours: ";
    cin>> endhour;
    cout<<"Input ending minutes: ";
    cin>> endmints;
    
    int hourpm, houram, mintspm, mintsam;
    //hours
    //calculating number of hours of shift before midnight
    if(hour>=6 && hour<12){
        if(mints>0){
            hourpm = 12 - (hour+1);
        }
        else{
            hourpm = 12-hour;
        }      
    }
    else{
        cout<<"Input correct time";
    }
    //calculating number of hours of shift after midnight
    if(endhour>=0 && endhour<6){
        houram = endhour-0;
    }
    else{
        cout<<"Input correct time";
    }
    
    //minutes
    //calculating number of minutes of shift before midnight
    if(mints>0 && mints<60){
        mintspm= 60-mints;
    }
    else{
        mintspm=mints;
    }
    //calculating number of minutes of shift after midnight
    if(endmints>0 && endmints<60){
        mintsam= endmints-0;
    }
    
    // converting minutes into hours
    float mintoHourAM, mintoHourPM;
    mintoHourPM = (float)mintspm/60;
    mintoHourAM = (float)mintsam/60;

    // calculating shift charge before midnight and after midnight separately
    float chargeAM, chargePM, totalCharge;
    chargePM = ((float)hourpm + mintoHourPM) * 15;
    chargeAM = ((float)houram + mintoHourAM) * 20;
    
    // calculating total shift charge
    totalCharge = chargePM + chargeAM;
    cout<<"\nTotal charge: "<<totalCharge;
    
    // calculating total shift hour
    float totalhours;
    totalhours = hourpm + mintoHourPM + houram + mintoHourAM;
    cout<<"\nTotal hours of work: "<<totalhours;
    
}
