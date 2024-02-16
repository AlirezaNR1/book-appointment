# Smart Interactive Display for Student-Professor Communication

## Introduction
In universities, communication between students and professors is vital. Especially in environments where professors have private rooms, creating an efficient and automatic communication system can greatly help to improve this communication. This project uses Internet of Things (IoT) technology to enable students to communicate quickly and effectively with their professors.

## Objectives 
The main goal of this project is to create an intelligent communication system to improve and facilitate communication between students and professors in the university. Using this technology, students can submit their requests without waiting and professors can provide their answers without wasting time. This project increases the quality of communication between university members and helps to improve the educational environment. Another feature of this system is that professors can also announce their status on the LCD screen. This feature allows teachers to specify their current status. This information allows students to see and determine the right time to interact with professors.

![image](https://github.com/AlirezaNR1/book-appointment/assets/59292708/af4354f4-fad9-4924-9a18-0172f694d775)


## Architecture 
![image](https://github.com/AlirezaNR1/book-appointment/assets/59292708/0b44b73e-8876-4dbd-bb17-f6c05688ca0c)

## Hardware Components
1. **ESP32:**
   - Network: Enables connection to routers for data transmission.
   - Data Processing: Supports basic input processing from sensors for complex computations.
   - Web Server: Allows access to HTML pages or development languages.
   - Compatibility with application libraries: Supports libraries related to keypad and LCD.

2. **RFID Sensor:**
   - Used for student identification and authentication.
   - Enables access to student information for effective communication between students and professors.
   
3. **Proximity Switch:**
   - Detects the presence of people near the screen.
   - Automatically turns on the screen when people are detected, conserving energy when not in use.
   
4. **LCD & Keypad:**
   - LCD screen displays the status of desired professors.
   - Students use the keypad to select professors and view their current status.
   - Provides an intuitive interface for students to navigate and interact with the system.

## Process Details

### Application Registration Process by Students:
1. **Student Registration:**
   - Ferdowsi University students can register their application by scanning their student card.
   - Non-students can register by entering their name and email.
2. **Authentication:**
   - After authentication, users can select the desired professor from the list and view their schedule and current attendance status.
3. **Meeting Request:**
   - Users can request a meeting time with the professor based on their availability.
   - They can attach an explanation to the request.
4. **Confirmation:**
   - If the request is accepted, a confirmation email will be sent to the student.
  
     ![Picture1](https://github.com/AlirezaNR1/book-appointment/assets/59292708/d19dc04b-0388-43f3-8f6a-321a54388022)


### Professors' Monitoring and Access Process:
1. **Login:**
   - Professors log in to their account.
2. **Status Update:**
   - Professors can set their current attendance status to be displayed on the LCD.
3. **Remote Door Access:**
   - Professors can remotely open the room door.
4. **Meeting Requests:**
   - Professors can view and accept or reject registered meeting requests.
5. **Confirmed Meetings:**
   - Professors can view the list of confirmed meetings.
6. **Schedule Management:**
   - Professors can view and make changes to their weekly schedule.
