Real-Time Public Transport Tracking for Small Cities

This project provides a real-time public transport tracking system prototype that helps users see live locations of public transport vehicles (buses, vans, etc.) on a map.

  Features
- Real-time display of vehicle locations on a map
- Auto-refresh every 5 seconds
- Vehicle info (ID + last updated time)
- Simple simulation of GPS data
┌──────────────┐      HTTP API     ┌──────────────┐      WebSocket/API     ┌──────────────┐
│ GPS Device   │ ───────────────▶ │ Backend      │ ◀──────────────────── │ Frontend App│
│ (Smartphone) │                  │ (Flask API) │                      │ (Web Map)  │
└──────────────┘                  └──────────────┘                      └──────────────┘
         │                                  │
         │                                  │
         │                                  ▼
         │                          ┌──────────────┐
         └─────────────────────────▶│ Database     │
                                    │ (SQLite)    │
                                    └──────────────┘
