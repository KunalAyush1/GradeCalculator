from typing import Tuple, Dict, List

def compute_cutoff(
    mean: float,
    std_dev: float,
    sd_multiplier: float,
    percentage_cap: float,
) -> float:
    return min(mean + std_dev * sd_multiplier, percentage_cap)

def assign_grade(
    marks:float,
    mean:float,
    std_dev: float,
    grading_policy: List[Dict]
) -> Tuple[ str, int]:
    for rule in grading_policy:
        grade = rule["grade"]
        points = rule["points"]
        sd_multiplier = rule["sd_multiplier"]
        percentage_cap = rule["percentage_cap"]
        
        #ruling
        if sd_multiplier is not None:
            cutoff = compute_cutoff(
                mean,
                std_dev,
                sd_multiplier,
                percentage_cap
            )
            if marks >= cutoff:
                return grade, points
        else:
            if grade == "F" and marks < 35:
                return grade, points
            if grade == "D" and marks >= 35:
                return grade, points
            
    raise RuntimeError("Grade assignment failed, Check grading policy.")