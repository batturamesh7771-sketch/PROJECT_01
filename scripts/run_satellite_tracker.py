"""
PROJECT 01: SGP4 Keplerian Satellite Orbit Propagator & Telemetry Engine
Author: ELONIKHIL (@batturamesh7771-sketch)
"""
import math
import csv
import datetime

EARTH_RADIUS_KM = 6378.137
MU_EARTH = 398600.4418 # km^3/s^2

class SatellitePropagator:
    def __init__(self, name, perigee_km, apogee_km, inclination_deg):
        self.name = name
        self.perigee_km = perigee_km
        self.apogee_km = apogee_km
        self.inclination_deg = inclination_deg
        
        self.semi_major_axis = EARTH_RADIUS_KM + (perigee_km + apogee_km) / 2.0
        self.eccentricity = (apogee_km - perigee_km) / (2.0 * self.semi_major_axis)
        self.orbital_period_sec = 2.0 * math.pi * math.sqrt((self.semi_major_axis ** 3) / MU_EARTH)
        self.mean_motion_rev_day = 86400.0 / self.orbital_period_sec

    def propagate_orbit(self, steps=360):
        records = []
        for i in range(steps):
            true_anomaly_rad = math.radians(i)
            # Distance from Earth center
            r_km = (self.semi_major_axis * (1.0 - self.eccentricity ** 2)) / (1.0 + self.eccentricity * math.cos(true_anomaly_rad))
            altitude_km = r_km - EARTH_RADIUS_KM
            
            # Orbital velocity v = sqrt(mu * (2/r - 1/a))
            velocity_kms = math.sqrt(MU_EARTH * ((2.0 / r_km) - (1.0 / self.semi_major_axis)))
            
            # Ground footprint radius (geometric line of sight)
            footprint_radius_km = math.acos(EARTH_RADIUS_KM / r_km) * EARTH_RADIUS_KM
            
            # Sub-satellite coordinates approximation
            lat_deg = math.degrees(math.asin(math.sin(math.radians(self.inclination_deg)) * math.sin(true_anomaly_rad)))
            lon_deg = (i * 1.5) % 360.0 - 180.0
            
            records.append({
                "Step": i,
                "True_Anomaly_deg": i,
                "Altitude_km": round(altitude_km, 2),
                "Velocity_kms": round(velocity_kms, 3),
                "Velocity_kmh": round(velocity_kms * 3600.0, 1),
                "Footprint_Radius_km": round(footprint_radius_km, 1),
                "Latitude_deg": round(lat_deg, 3),
                "Longitude_deg": round(lon_deg, 3)
            })
        return records

if __name__ == "__main__":
    print("=" * 60)
    print("PROJECT 01: Running Keplerian Orbit Propagators...")
    print("=" * 60)
    
    iss = SatellitePropagator("ISS (ZARYA)", 415.0, 422.0, 51.64)
    print(f"ISS Orbital Period: {iss.orbital_period_sec / 60.0:.2f} min ({iss.mean_motion_rev_day:.2f} revs/day)")
    telemetry = iss.propagate_orbit(180)
    print(f"Generated {len(telemetry)} telemetry steps.")
