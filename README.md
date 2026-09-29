# OceanSync – PRAGATI

**Polar Research Autonomous Gateway And Tracking Infrastructure**

Smart India Hackathon 2026 | Problem Statement **SIH26065** | Theme: Robotics and Drones | Category: Hardware | Team: **OceanSync**

**Problem Statement:** Autonomous Low Cost Ocean Observation Platform for Polar and Southern Oceans (Ministry of Earth Sciences / NCPOR)

## Demo Video
File: `OceanSync_Dashboard_Demo.mp4` (open the file in this repository and use the Raw or Download option to play it).

## Live Dashboard
The web dashboard (React + Vite) is in a separate repository:
https://github.com/UnnatiBhardwaj26/OceanSync

## The Problem
Winter, under-ice and remote regions of the Southern Ocean are under-sampled because of cost, power and communication limits. Existing floats are expensive, use a lot of energy for continuous transmission, and depend on costly satellite links.

## Our Solution: Distributed Sensor Pods + One Gateway Buoy
- Multiple low-cost sensor pods float independently and report over **LoRa** to one shared gateway buoy.
- Only the gateway buoy carries the expensive long-range radio (Iridium / satellite uplink).
- The gateway aggregates, validates and timestamps data, and uses **edge AI** to prioritize data before sending it to the cloud.
- Pods and the gateway store data on SD/flash memory during communication gaps and forward it once the connection is restored.

**Data flow:** Sensor Pods → LoRa → Gateway Buoy → Satellite / GSM → Cloud Storage & Processing → Live Dashboard

## Key Features
- **Shared communication:** one gateway serves many pods, which reduces power use.
- **Low-cost and scalable:** more pods can be added without adding expensive radios.
- **Reliable network:** if one pod is lost, the others keep collecting data.
- **Store-and-forward resilience:** no data loss during communication gaps.
- **Low-power operation:** solar plus battery, with deep sleep between readings.

## Technologies Used
| Component | Technology |
|---|---|
| Pod MCU | ESP32-S3 |
| Temperature | TMP117 (marine probe) |
| Pressure / Depth | MS5837-30BA (0-30 bar) |
| IMU | ICM-42688-P (wake-on-motion) |
| GNSS | u-blox MAX-M10S |
| Radio (pod to gateway) | Semtech SX1262 LoRa |
| Uplink (gateway) | GSM/LTE (prototype), Iridium RockBLOCK (deployment) |
| Power | Solar + BQ25570 MPPT + cold-rated battery |
| Dashboard | React + Vite |

## Repository Structure
```
OceanSync-SIH2026/
├── src/                          # Software package (sensors, launch files)
├── ocean_environment/            # Simulation environment (wave world and models)
├── OceanSync_Dashboard_Demo.mp4  # Demo video
└── README.md
```

## How to Run the Dashboard
```bash
git clone https://github.com/UnnatiBhardwaj26/OceanSync.git
cd OceanSync
npm install
npm run dev
```
Then open the local URL shown in the terminal (usually http://localhost:5173).

## Impact
- Wider coverage of remote, hard-to-reach regions
- Lower operational cost through shared gateway hardware
- Long-term monitoring for months to years
- Better data for research, policy and forecasting

**Who benefits:** researchers and scientists, government agencies, maritime and shipping, climate and environmental organizations, academic institutions.

## References
- Argo Programme: https://argo.ucsd.edu
- Polar Argo: https://argo.ucsd.edu/expansion/polar-argo/
- India-Argo (INCOIS): https://incois.gov.in/site/datainfo/OON.jsp
- SOOS: https://www.soos.aq
- SOCCOM (MBARI): https://www.mbari.org/project/soccom/

## Team OceanSync
- Nishtha Verma
- Unnati Bhardwaj
- Himanshi Vashney
- Uma Sharma
- Harshita Singh
- Krati Maheshwari
