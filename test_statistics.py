from statistics import compute_mean_and_std

def run_tests():
    print("Running statistics module tests.....\n")
    
    marks = [65, 70, 75, 80, 85]
    mean, sd = compute_mean_and_std(marks)
    print("Test-1 - Normal case")
    print(f"Mean: {mean}, SD: {sd} \n")
    
    marks = [90]
    mean, sd = compute_mean_and_std(marks)
    print("Test-2 - Single value")
    print(f"Mean: {mean}, SD: {sd} \n")
    
    print("Test-3 - Empty list")
    try:
        compute_mean_and_std([])
    except Exception as e:
        print(type(e).__name__, ":",e,"\n")
    
    print("Test-4 - Non-numeric value")
    try:
        compute_mean_and_std([70,89,"@a", 91])
    except Exception as e:
        print(type(e).__name__, ":", e, "\n")
    
if __name__ =="__main__":
    run_tests()