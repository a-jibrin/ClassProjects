from math import radians, cos, sin, asin, sqrt

def haversine(point1, point2, units="km"):
    """Calculate an approximate distance between two points on Earth.

    Args:
        point1 (tuple of float, float): first point (lat, lon) in decimal degrees.
        point2 (tuple of float, float): second point (lat, lon) in decimal degrees.
        units (str): units of return value. Should be "km" for kilometers or "mi" for miles. (Default: "km")

    Returns:
        float: the distance between the two points in the requested units.
    """
    if units not in ["km", "mi"]:
        raise ValueError("units should be 'km' or 'mi'")
    
    R = 6372.8 if units == "km" else 3959.87433
    
    if len(point1) != 2:
        raise ValueError("point1 should be a tuple of two floats")
    
    if len(point2) != 2:
        raise ValueError("point2 should be a tuple of two floats")
    
    lat1, lon1 = point1
    lat2, lon2 = point2
    
    for value in [lat1, lon1, lat2, lon2]:
        if not isinstance(value, (float, int)):
            raise ValueError("coordinates must be floats")
    
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    
    return R * c

