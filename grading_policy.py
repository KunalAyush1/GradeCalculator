from typing import Dict, List, Dict

def get_relative_grading_policy() -> List[Dict]:
    """
    Returns the grading policy as a list of (grade, sd_multiplier).

    Order matters: higher grades must come first.
    """
    return [
        {
            "grade": "A+",
            "points": 10,
            "sd_multiplier": 1.5,
            "percentage_cap": 91
        },
        {
            "grade": "A",
            "points": 9,
            "sd_multiplier": 1.0,
            "percentage_cap": 82
        },
        {
            "grade": "B+",
            "points": 8,
            "sd_multiplier": 0.5,
            "percentage_cap": 73
        },
        {
            "grade": "B",
            "points": 7,
            "sd_multiplier": 0.0,
            "percentage_cap": 64
        },
        {
            "grade": "C+",
            "points": 6,
            "sd_multiplier": -0.5,
            "percentage_cap": 55
        },
        {
            "grade": "C",
            "points": 5,
            "sd_multiplier": -1.0,
            "percentage_cap": 91
        },
        {
            "grade": "D",
            "points": 4,
            "sd_multiplier": None,
            "percentage_cap": 35
        },
        {
            "grade": "F",
            "points": 0,
            "sd_multiplier": None,
            "percentage_cap": 0
        }
    ]
   