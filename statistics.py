import math
from typing import List, Tuple

def validate_marks(marks: List[float]) -> None:
    """
    Validates the marks list.
    Parameters
    ---------
    marks: List[float]
        List of marks obtained by students.
    Raises
    ------
    ValueError
        If the list is empty
    TypeError
        If any mark is not numeric
    """
    if not marks:
        raise ValueError("Marks list is empty, cannot compute!!!!")
    
    for m in marks:
        if not isinstance(m, (int, float)):
            raise TypeError(f"Invalid mark detected: {m}. Marks must be numeric.")



def compute_mean(marks: List[float]) -> float:
    """
    Computes the average of marks.
    Parameters
    -----------
    marks : List[float]
    
    
    Returns
    --------
    float
        Mean of marks.
    """
    validate_marks(marks)
    return sum(marks) / len(marks)

def compute_std_dev(marks: List[float], mean: float) -> float:
    """
    Computes the population standard deviation of marks.
    
    Formula:
        sqrt( (1 / N) * sigma(x - mean)**2)
        
    Parameters
    -----------
    marks : List[float]
    mean : float
    
    Returns
    ---------
    float
        Population standard deviation    
    """
    variance = sum((x - mean) ** 2 for x in marks) / len(marks)
    return math.sqrt(variance)

def compute_mean_and_std(marks: List[float]) -> Tuple[float, float]:
    """
    Computes mean and standard deviation together

    Parameter
    ----------
        marks- List[float]

    Returns:
        Tuple[float, float]
            Mean and standard deviation
    """
    mean = compute_mean(marks)
    std_dev = compute_std_dev(marks, mean)
    
    return mean, std_dev

