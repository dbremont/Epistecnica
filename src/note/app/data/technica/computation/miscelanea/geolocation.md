# Geolocation


> A computational procedure that infers or calculates the geographical coordinates (e.g., latitude, longitude, elevation) or spatial position of a target using data from signals (GPS, Wi-Fi, cellular, radio), sensors (IMU, camera, LiDAR), or network information (IP, access points, identifiers).
> 

## Method Space

| **Method** | **Description** | **Limits** | **Tags** |
| --- | --- | --- | --- |
| **GPS (Global Positioning System)** | Determines position using satellite signals received by the device. | Requires clear sky view; degraded in urban canyons or indoors. | `satellite`, `high-accuracy`, `outdoor` |
| **A-GPS (Assisted GPS)** | Uses network data (cell towers, servers) to speed up GPS lock and improve accuracy. | Still weak indoors; needs cellular network assistance. | `satellite`, `network-assisted`, `mobile` |
| **Cell Tower Triangulation** | Estimates location using distance to multiple cellular towers. | Lower accuracy (100–2000m); depends on tower density. | `cellular`, `triangulation`, `low-accuracy` |
| **Cell Tower Single-Tower ID** | Infers rough location based on the specific tower the device is connected to. | Very low precision; can span kilometers. | `cellular`, `coarse`, `coverage-area` |
| **Wi-Fi Positioning System (WPS)** | Uses nearby Wi-Fi access point IDs + signal strength mapped to large databases. | Accuracy varies with AP density; fails in rural areas. | `wifi`, `database`, `medium-accuracy` |
| **Bluetooth Beacons (BLE)** | Uses proximity to low-power beacons for indoor or micro-location. | Very short range; requires beacon infrastructure. | `bluetooth`, `indoor`, `proximity` |
| **IP Geolocation** | Maps IP address to geographic data based on ISP records or databases. | Low accuracy; often only city-level. | `network`, `coarse`, `database` |
| **Browser / HTML5 Geolocation API** | Uses hybrid methods (GPS, Wi-Fi, cell, sensors) depending on device and permissions. | Depends on device hardware + permissions; accuracy varies widely. | `hybrid`, `client-side`, `standard-api` |
| **Inertial Navigation (IMU)** | Uses accelerometer, gyroscope, and magnetometer to track relative movement. | Drifts quickly without calibration; used for short-term tracking. | `sensors`, `dead-reckoning`, `relative` |
| **Visual Odometry (Camera-based)** | Computes movement/location from camera image changes. | Requires good lighting; heavy compute; drifts without anchors. | `cv`, `slam`, `robotics` |
| **SLAM (Simultaneous Localization and Mapping)** | Builds a map + localizes device within it using cameras, LiDAR, or sensors. | Needs strong compute; poor performance in featureless environments. | `slam`, `robotics`, `high-precision` |
| **LiDAR Positioning** | Uses laser scanning of environment to determine position relative to known maps. | Requires prior mapped environment; expensive hardware. | `lidar`, `indoor`, `high-precision` |
| **Geofencing (Logical)** | Uses device’s position to determine whether it's inside a predefined zone. | Depends on underlying geolocation source; not precise alone. | `logical`, `zones`, `context-aware` |
| **Time Difference of Arrival (TDoA)** | Computes position using timing differences between multiple signals (e.g., radio). | Requires synchronized transmitters; specialized infrastructure. | `triangulation`, `radio`, `infrastructure` |
| **RFID Positioning** | Location inferred by detecting RFID tag presence or signal characteristics. | Very short range; often coarse unless specialized readers exist. | `rfid`, `proximity`, `indoor` |
| **Ultrasound Positioning** | Uses sound pulses for short-range, high-precision indoor location. | Needs dedicated emitters/receivers; limited to small areas. | `ultrasound`, `indoor`, `high-precision` |

## References

- https://en.wikipedia.org/wiki/Geopositioning
- https://en.wikipedia.org/wiki/Internet_geolocation