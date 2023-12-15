---
title: Geographical coordinate
---

# SP-Lang geopoint

The geopoint type is a composite data type designed to efficiently store and represent geographical coordinates, specifically longitude and latitude, in a compact binary format.
It combines the longitude and latitude into a single 64-bit integer, utilizing a fixed-point encoding to ensure precision and efficient storage.
The geopoint type provides a balance between precision and storage efficiency, making it an ideal choice for modern 64-bit CPU architectures.


## Format

<img src="../geopoint.drawio.png" alt="Schema of the geopoint bit layout" />

The higher 32 bits represent the longitude, and the lower 32 bits represent the latitude.
Both longitude and latitude are encoded as signed 32-bit integers (si32), allowing for a high level of precision.

### Longitude

Scale factor for longitude is: (2^32 / 360) = ~11930464.711

Encoding: encoded = (longitude + 180) * (2^32 / 360)

Decoding: longitude = (encoded / (2^32 / 360)) - 180

### Latitude

Scale factor for latitude is: (2^32 / 180) = ~23860929.422

Encoding: encoded = (latitude + 90) * (2^32 / 180)

Decoding: latitude = (encoded / (2^32 / 180)) - 90


## Precision

The encoded longitude has a precision of approximately 4.76 meters at the equator.

The encoded latitude has a precision of approximately 1.19 meters.
