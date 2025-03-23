#include <iostream>
#include <string>
using namespace std;

// AI Model for Apple Device Recommendation
class AppleAI {
public:
    string recommend_device(int budget, string type, string performance, string battery) {
        if (type == "iphone") {
            if (budget >= 1000) return "iPhone 15 Pro Max";
            if (budget >= 800) return "iPhone 14 Pro";
            return "iPhone SE";
        }
        else if (type == "macbook") {
            if (performance == "yes" && budget >= 2000) return "MacBook Pro M3 Max";
            if (budget >= 1300) return "MacBook Air M2";
            return "MacBook Air M1";
        }
        else if (type == "ipad") {
            if (budget >= 1200) return "iPad Pro M2";
            if (budget >= 600) return "iPad Air";
            return "iPad 9th Gen";
        }
        return "Unknown Device";
    }
};

int main() {
    AppleAI ai;
    int budget;
    string type, performance, battery;

    cout << "Enter your budget (in $): ";
    cin >> budget;

    cout << "What device do you want? (iphone/macbook/ipad): ";
    cin >> type;

    cout << "Do you need high performance? (yes/no): ";
    cin >> performance;

    cout << "Do you need long battery life? (yes/no): ";
    cin >> battery;

    cout << "Recommended Device: " << ai.recommend_device(budget, type, performance, battery) << endl;

    return 0;
}
