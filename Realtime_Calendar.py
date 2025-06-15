import time
from datetime import datetime
from threading import Timer


class CalendarClass:
    @staticmethod
    def main():
        # Create a datetime instance for June 1, 2025
        calendar_date = datetime(2025, 6, 1)

        # Get the day of the week (Monday is 0 and Sunday is 6)
        day_of_week = calendar_date.weekday()

        # Print the day of the week
        print(f"Day of the week for JUNE 2025: {day_of_week + 1}")  # +1 to match Java's Calendar where Sunday=1

        # Function to print current time and date information
        def print_current_time():
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_day = now.strftime("%A")
            current_month = now.strftime("%B")
            current_year = now.strftime("%Y")
            day_number = now.strftime("%d")

            print(
                f"Current Time: {current_time} | Day: {current_day} | Month: {current_month} | Year: {current_year} | Day Number: {day_number}")

            # Schedule the next execution after 1 second
            Timer(1, print_current_time).start()

        # Start the periodic printing
        print_current_time()

        # Let it run for 5 seconds
        time.sleep(5)


# Run the main method
if __name__ == "__main__":
    CalendarClass.main()