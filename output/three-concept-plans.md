# Three concept directions for the rescue signal project

## 1. Phone-based rescue beacon app
### Goal
Create a simple mobile web app that helps people send or receive a rescue signal during an emergency.

### Core idea
A person can trigger a rescue beacon from their phone. Nearby phones with the app can detect the signal and report that a beacon was seen nearby.

### MVP features
- One-tap beacon activation
- Basic location and timestamp logging
- Nearby-device detection report
- Simple map or list of detections
- Basic emergency note field

### Best for
- Fastest first version
- Simple deployment on any phone with internet
- Low cost and easy testing

### Strengths
- Easiest to build
- Most realistic first prototype
- Can be used by responders, volunteers, and families

### Limits
- Not a guaranteed underground locator
- Accuracy depends on signal strength and environment

---

## 2. Drone-assisted search system
### Goal
Use a drone to scan a larger area and help locate a signal source more efficiently after a disaster.

### Core idea
The drone flies a planned route and collects signal data. The software marks stronger signal zones so rescue teams can focus their search.

### MVP features
- Pre-set flight path
- Signal strength logging
- Map view of detected hotspots
- Simple alert when a signal is strong
- Manual rescue team review of the results

### Best for
- Covering large or hard-to-reach areas
- Supporting rescue teams in the field
- Extending the phone-based version

### Strengths
- Better area coverage
- Useful for large disaster zones
- Stronger search support than a phone-only approach

### Limits
- Needs hardware and testing
- More complex than the phone version
- Still not a perfect locator

---

## 3. Call-triggered rescue detection concept
### Goal
Use an incoming call or emergency ring as a trigger for detection.

### Core idea
When a trapped person’s phone receives a call, the ringing signal can be detected by a nearby drone, receiver, or app. The system can mark the area where the strongest response appears.

### MVP features
- Emergency call or ring trigger
- Detection of signal response
- Logging of strongest signal area
- Simple map or zone marking
- Optional alert to responders

### Best for
- A more specific rescue workflow
- A simple, practical prototype for signal-based search
- Testing a trigger-based system before wider automation

### Strengths
- Gives the system a clear event to detect
- Easier than continuous passive scanning
- Strong story for a prototype and demonstration

### Limits
- Depends on the phone being reachable and active
- Signal quality may vary widely
- Still needs real-world testing

---

## Recommended path
The best way to build this is:
1. Start with the phone-based rescue beacon app.
2. Use it as the foundation for the rescue workflow.
3. Add the drone system later as a search support layer.
4. Test the call-triggered approach as an optional feature once the base system works.

## Suggested product framing
Present the project as a humanitarian rescue support tool, not as a perfect locator. The first goal is to help responders narrow down search areas quickly and safely.
