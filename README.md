# Mo-Choo
Winner of the BlackRock Technical Challenge HackKings 2022

# BlackRock Challenge Description
The 21st century has seen technological advancements radically change the way we interact
with and view the world. For example, it has witnessed the exponential growth of social
media, the birth of Web3.0, and the widespread utilization of blockchain technology.
At BlackRock, we are committed to a better future. We are also a fintech, innovating to take
advantage of the latest technology and trends.
## Example Projects
* With social media becoming increasingly pervasive, can it be used for microfinancing,
allowing us to reach more demographics and better identify potential entrepreneurs?
(See Nobel Peace Prize 2006 for the impact of microfinancing)
* What if we were able to use blockchain in order to trace cotton's origin in the retail
industry? As the blockchain is unalterable, it would empower customers to be able to
buy fair products with confidence
### Deliverables
* Demo and/or link to your product (e.g., website link, demo of application or API,
documentation, etc.)
* One paragraph taking us through your idea and how it fits into our challenge
### Resources
* Data Set Repository: https://www.kaggle.com/
* Technical classes: https://openclassrooms.com/en/
* Public APIs: https://github.com/public-apis/public-apis
How can we take advantage of the changing
technological landscape to contribute to a better
future?

# What it Mo-Choo
Burnout is a main occupational problem among healthcare workers, especially after the pandemic outbreak. According to the report from WHO presented on 5 October 2022, 23-46% of healthcare workers were suffering from anxiety, while 21-37% were suffering from depression. The main causes of burnout were increased contact with contagious patients, a lack of personal protective equipment, and work stress. Moreover, 54 percent say too much of their time is spent on non-nursing tasks such as paperwork according to Nuffield Trust.
 
To solve the pain points the healthcare workers face, we developed a real-time hand gesture recognition application, which allowed nurses to use the touchless interface via gestures. Without touching the device, nurses not only increase their work efficiency but also improve hygiene since they no longer have to take off their gloves to touch the screen. The application reduces the work stress of nurses and their risk of infection, which creates a better medical environment for the public.

For this project's backend we're developing on python using Computer Vision Technology as well as Machine Learning models. To that end, we're using Open-CV, a real time computer vision and Image Processing Framework. The library allows us to create a video capture object that will be one of the building block of our back-end. Once we have the image, we need to start the hand gesture recognition process.Therefore, we build a gesture recognizer using both MediaPipe and Tensorflow. MediaPipe is a customized machine learning solution framework developed by Google and is open source and light-weight. It comes with pre-trained ML solutions including hand recognition. The Tensorflow pre-trained model we're using here recognizes 9 hand gestures, namely: okay, stop, peace, call me, fist, rock, smile, thumbs up and thumbs down. These 9 gestures will be used as commands on our interface. If time allowed, we could potentially improve the model by creating more classes (so more training data and more hand gestures) or allowing for multiple hand detection.

On top of the current demoed application, we can think of many more use cases where this would be useful and efficient. The gesture recognition system can build a bridge between deaf-mute people and the rest of the world. For instance, drive through technology is currently mainly driven by speech despite the camera being present. Through the gesture recognition system, purchasing from a drive through can be completed by executing a series of simple hand gestures when signing/speaking is difficult. Last but not least and given the pandemic situation, this system could also be used to efficiently reduce the contacts with surfaces/devices by converting touch-based commands to touch-free command in many industries where hygiene is a key point (catering, hospitals, food factories, ...). 
We present to you Mo-Choo, our augmented reality interface turning non-touch screens into touch (less) screens

## Watch a Demo
https://youtu.be/1ni2TS9kOqQ


## Bibliography
* Thanks to Tech-Vidvan for the tutorial and base source code: https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/
* Link to MediaPipe Hands to understand the algorithm: https://google.github.io/mediapipe/solutions/hands.html
