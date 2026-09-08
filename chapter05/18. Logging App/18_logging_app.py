import logging

def main():
   log_file = "cf9.log"

   file_handler = logging.FileHandler(log_file, mode='a')

   handlers = [file_handler]

   logger = logging.getLogger("search-app")

   logging.basicConfig(
       handlers=handlers,
       level=logging.INFO,
       format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"

   )

   nums = [10, 20, 30, 40, 50]
   num_to_find = 120

   try:
       index = nums.index(num_to_find)
       print(f"Found at index: {index}")
   except ValueError as e:
       logger.error(f"Error occured: {e}", exc_info=True)   

if __name__ == "__main__":
    main()