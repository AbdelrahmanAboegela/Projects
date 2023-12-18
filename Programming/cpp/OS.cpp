#include <iostream>
#include <queue>
#include <thread>
#include <chrono>

struct Process {
    int processNumber;
    bool isActive;

    Process(int processNumber) : processNumber(processNumber), isActive(true) {}
};

int main() {
    std::queue<Process> processQueue;
    int counter = 0;
    
    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Sleep for 0.1 seconds
        
        // Create a new process and add it to the tail of the queue
        if (counter % 3 == 0 && processQueue.size() < 10) {
            Process newProcess(counter);
            processQueue.push(newProcess);
            std::cout << "Process " << newProcess.processNumber << " created at time " << counter << std::endl;
        }
        
        // Terminate the process at the tail of the queue
        if (counter % 7 == 0 && !processQueue.empty()) {
            Process terminatedProcess = processQueue.back();
            terminatedProcess.isActive = false;
            processQueue.pop();
            std::cout << "Process " << terminatedProcess.processNumber << " terminated at time " << counter << std::endl;
        }
        
        // Service the process at the front of the queue
        if (!processQueue.empty()) {
            Process servicedProcess = processQueue.front();
            if (servicedProcess.isActive) {
                std::cout << "Process " << servicedProcess.processNumber << " serviced at time " << counter << std::endl;
            } else {
                std::cout << "Process " << servicedProcess.processNumber << " dequeued at time " << counter << std::endl;
                processQueue.pop();
            }
        } else {
            std::cout << "CPU is idle at time " << counter << std::endl;
        }
        
        // Increment the counter
        counter++;
    }
    
    return 0;
}



// #include <iostream>
// #include <queue>
// #include <chrono>
// #include <thread>

// using namespace std;

// struct Process {
//     int processNumber;
//     string status;
// };

// int main() {
//     queue<Process> processQueue;
//     int counter = 0;
    
//     while (true) {
//         // wait for 0.1 second
//         this_thread::sleep_for(chrono::milliseconds(100));
        
//         // create new process if counter%3=0
//         if (counter % 3 == 0 && processQueue.size() < 10) {
//             Process newProcess;
//             newProcess.processNumber = counter;
//             newProcess.status = "active";
//             processQueue.push(newProcess);
//             cout << "Process " << newProcess.processNumber << " created at time " << counter << endl;
//         }
        
//         // terminate process if counter%7=0
//         if (counter % 7 == 0 && !processQueue.empty()) {
//             Process terminatedProcess = processQueue.back();
//             terminatedProcess.status = "terminated";
//             processQueue.pop();
//             cout << "Process " << terminatedProcess.processNumber << " terminated at time " << counter << endl;
//         }
        
//         // service process if there are processes in the queue
//         if (!processQueue.empty()) {
//             Process servicedProcess = processQueue.front();
//             processQueue.pop();
//             servicedProcess.status = "terminated";
//             cout << "Process " << servicedProcess.processNumber << " serviced at time " << counter << endl;
//         } else {
//             // CPU is idle
//             cout << "CPU is idle at time " << counter << endl;
//         }
        
//         // increment counter
//         counter++;
//     }
    
//     return 0;
// }
