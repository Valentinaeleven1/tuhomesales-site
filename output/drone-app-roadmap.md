# Drone App MVP Roadmap

## Goal
Create a simple, realistic first version of a drone-assisted rescue support system that can:
- plan a search mission,
- collect signal data,
- and show possible hotspot locations on a map.

## Phase 1: Define the MVP
### Objective
Lock the scope to a simple, useful first version.

### Tasks
- Define the main user: rescue team operator.
- Define the main job: start a mission and review possible signal zones.
- Decide the first mission flow:
  1. Create mission
  2. Start data collection
  3. View map of results
  4. Review hotspots
- Keep the first version focused on mapping and reporting, not full autonomous detection.

### Deliverable
A short MVP scope document with the core features and success criteria.

---

## Phase 2: Build the Web Dashboard
### Objective
Create the basic interface for the operator.

### Features
- Mission creation screen
- Start/stop mission button
- Live data view
- Map view for plotted points
- Basic mission summary panel

### Tech choices
- Frontend: simple web app
- Hosting: Vercel
- Backend: Supabase for mission storage

### Deliverable
A working dashboard that can create a mission and store basic data.

---

## Phase 3: Add Mission Data Logging
### Objective
Store the information collected during a search mission.

### Features
- Save mission metadata
- Save signal readings with timestamp and location
- Save notes from the operator
- Show recent mission history

### Deliverable
A working database-backed mission logging system.

---

## Phase 4: Add Signal Hotspot Visualization
### Objective
Turn collected data into something useful for rescue teams.

### Features
- Plot signal readings on a map
- Show the strongest areas visually
- Highlight possible hotspots
- Allow filtering by mission or time

### Deliverable
A simple map-based view that helps operators understand where to focus.

---

## Phase 5: Connect Drone Telemetry
### Objective
Add support for real drone mission data.

### Features
- Receive drone location data
- Sync mission path with collected readings
- Show drone position on the map
- Save telemetry with each signal point

### Deliverable
A connected version where the dashboard can display drone movement and readings together.

---

## Phase 6: Testing and Validation
### Objective
Validate the workflow in a safe environment.

### Tasks
- Test the dashboard with simulated data
- Test mission creation and logging
- Test map visualization
- Review whether the workflow is clear for rescue operators

### Deliverable
A tested prototype that is ready for limited real-world demos.

---

## Phase 7: Refinement and Next Features
### Objective
Improve the experience based on feedback.

### Possible next features
- Offline support for low-connectivity areas
- Better hotspot scoring
- Alert notifications
- More advanced mapping
- Support for multiple drones or teams

### Deliverable
A refined version of the product with a stronger rescue workflow.

---

## Suggested Timeline
### Weeks 1–2
- Scope the MVP
- Set up the project structure
- Build the dashboard shell

### Weeks 3–4
- Add database and mission logging
- Build the first map view

### Weeks 5–6
- Connect drone telemetry
- Test mission flow

### Weeks 7–8
- Improve usability and prepare for demo

---

## Recommended Drone Hardware
### Target drone characteristics
- 30+ minutes of flight time
- stable GPS-based flight
- easy mission control
- portable and simple to operate
- ability to carry a lightweight sensor or logger

### Suggested model range
- **DJI Mini 4 Pro**: best for easiest prototyping, lightweight, ~30–34 min flight time
- **DJI Air 3**: stronger stability and range, ~46–50 min flight time
- **DJI Mini 3 Pro**: budget-friendly and easy to use, ~34 min flight time
- **Autel Evo Nano+**: portable, user-friendly, good for lightweight setups

### Future upgrade options
- **DJI Mavic 3 Classic / Mavic 3 Pro**: more payload capacity and better stability
- **Autel Evo II**: useful if adding extra detection hardware later

---

## Drone payload and Raspberry Pi setup
### Payload structure
- Use a small payload package that includes:
  - Raspberry Pi 4 Model B or Raspberry Pi Zero 2 W
  - small USB GPS receiver
  - USB power bank or lightweight 5V supply
  - signal sensor module (such as an RTL-SDR dongle or Bluetooth/Wi-Fi receiver)
  - compact enclosure or mount for drone attachment

### Attachment considerations
- The payload should be lightweight and balanced.
- Secure the unit to the drone with a small mounting plate, foam padding, or drone accessory mount.
- Keep the total added weight under the drone’s payload capacity.
- Use rubber straps, zip ties, or custom brackets designed for the drone model.

### Practical fast option
- Buy a Raspberry Pi kit with power supply.
- Load the rescue signal program and logging software on it.
- Send the complete payload kit to the drone operator.
- They mount it on the existing GPS-capable drone and fly missions.

### Signal detection note
- You do not need to decode the phone call itself.
- The goal is to detect the electromagnetic or wireless signal pattern associated with the phone’s activity.
- A low-cost receiver can look for a beacon-like signal from the phone or a separate emergency transmitter.
- For a first practical prototype, use a custom detectable signal rather than relying on raw cellular call decoding.

---

## Success Criteria for the MVP
The MVP is successful if it can:
- create a mission,
- collect and store signal data,
- display possible hotspots on a map,
- and provide a clear workflow for rescue teams.
