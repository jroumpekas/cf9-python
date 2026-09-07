def main():
 grades = [7, 5, 9, 10, 3]

  #upscale grades by 1 using list compr !

 upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
 print(f"Upscaled grades: {upscaled_grades}")

 # TODO: .....  


if __name__ == "__main__":
    main()