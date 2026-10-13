# Drone App Project Report

## Project Overview
This project explores a drone-assisted rescue support system for emergency situations such as earthquakes, building collapses, or large-area search operations. The goal is not to promise perfect indoor detection, but to create a useful tool that helps responders narrow down search areas faster.

## Problem Statement
After a disaster, people may be trapped and unable to communicate. Rescue teams need better ways to search large areas quickly. A drone can help scan the environment and collect signal-related data that may indicate the presence or location of a device or emergency beacon.

## Core Concept
A drone flies a planned route and collects signal information. The software processes that data and marks possible hotspots on a map so rescue teams can focus their search.

## Main Purpose
The system should help rescue teams:
- cover more ground quickly,
- identify possible signal-rich zones,
- reduce time spent searching blindly,
- and support better decision-making in emergencies.

## Project Goals
- Build a simple and realistic first version.
- Keep the system useful, not overly complex.
- Focus on rescue support rather than perfect detection.
- Make the tool easy to operate during emergencies.

## Recommended MVP Features
1. Drone flight planning
   - Set a route or search area.
   - Start and stop the mission easily.

2. Signal logging
   - Record signal strength and location during flight.
   - Save timestamps for each reading.

3. Hotspot map
   - Show the strongest detected areas on a simple map.
   - Highlight zones for follow-up investigation.

4. Rescue team dashboard
   - Display recent mission results.
   - Allow quick review of possible signal locations.

5. Manual notes
   - Let operators add comments such as “debris field,” “possible movement,” or “check again.”

## Suggested Technology Stack
- Frontend: simple web dashboard for mission control
- Backend: Supabase or similar free service for storing mission data
- Mapping: map service for visualizing detection points
- Drone integration: basic flight control and telemetry support
- Hosting: Vercel

## Recommended Development Approach
1. Start with a web-based control dashboard.
2. Build simple mission data logging first.
3. Add map-based hotspot visualization.
4. Connect the system to drone telemetry in a later phase.
5. Keep the first version focused on signal mapping and rescue support.

## Risks and Challenges
- Signal detection may be affected by terrain, debris, and weather.
- Drone battery and flight time can limit range.
- The system should not overpromise accuracy.
- Real-world testing will be essential.

## Success Criteria
The first version is successful if it can:
- run a simple search mission,
- record signal data clearly,
- show possible hotspots on a map,
- and provide a useful starting point for rescue teams.

## Recommended Positioning
This project should be presented as a humanitarian search and rescue support tool. Its value is in helping responders act faster and more intelligently during critical situations.

## Next Step
The next step is to turn this concept into a more detailed MVP plan with:
- feature priorities,
- system architecture,
- and a simple implementation roadmap.
