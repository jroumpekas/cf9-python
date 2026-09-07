from typing import List, Tuple, Union
 
def calculate_grade(assignment_scores: List[Union[int, float]], mid_score: Union[int, float], final_score: Union[int, float]) -> Tuple[float, str]:
    def weighted_average():
        assignment_score = sum(assignment_scores) / len(assignment_scores)

        return(assignment_score * 0.4) + (mid_score * 0.3) + (final_score * 0.3)
    
    def determine_grade(average: float) -> str:
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'E'
   
    average = weighted_average()
    grage = determine_grade(average)
    return average, grage

def main():
    final_avrage, final_grade = calculate_grade([85, 90, 88, 92], 92, 84)
    print(f"The final grade is: {final_grade} with average: {final_averge}")