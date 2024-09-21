# Initialize coach seats array
coach = [
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0]               
]

def show_seats():
    # display the current status of seats
    print("Seat Layout (A = Available, B = Booked):")
    for row_num, row in enumerate(coach):
        row_display = ['A' if seat == 0 else 'B' for seat in row]
        print(f"Row {row_num + 1}: {' '.join(row_display)}")
    print() 

def book_seats_in_row(row_num, requested_seats):
    """Try to book seats in the user's preferred row."""
    booked = []
    row = coach[row_num - 1] 

    available_in_row = []
    for seat_num, seat in enumerate(row):
        if seat == 0:
            available_in_row.append(seat_num)
        else:
            available_in_row = []  
        
        if len(available_in_row) == requested_seats:
            # We found enough consecutive seats, so book them
            for idx in available_in_row:
                coach[row_num - 1][idx] = 1  
                booked.append(f"Row {row_num}, Seat {idx + 1}")
            return booked 

    # If there aren't enough consecutive seats
    for seat_num, seat in enumerate(row):
        if seat == 0:  
            coach[row_num - 1][seat_num] = 1
            booked.append(f"Row {row_num}, Seat {seat_num + 1}")
            if len(booked) == requested_seats:
                return booked 
    return booked  

def find_and_book_in_any_row(requested_seats):
    """Find and book seats in any row when the user's preferred row doesn't work."""
    booked = []
    
    for row_num, row in enumerate(coach):
        available_in_row = []
        for seat_num, seat in enumerate(row):
            if seat == 0:
                available_in_row.append(seat_num)
            else:
                available_in_row = [] 
            
            if len(available_in_row) == requested_seats:
                # We found enough consecutive seats, so book them
                for idx in available_in_row:
                    coach[row_num][idx] = 1  
                    booked.append(f"Row {row_num + 1}, Seat {idx + 1}")
                return booked  

    # Second pass: book nearby available seats across rows
    for row_num, row in enumerate(coach):
        for seat_num, seat in enumerate(row):
            if seat == 0:  
                coach[row_num][seat_num] = 1
                booked.append(f"Row {row_num + 1}, Seat {seat_num + 1}")
                if len(booked) == requested_seats:
                    return booked  
    
    return booked  

def start_booking():
    """Main function to handle the booking process."""
    while True:
        try:
            num_seats = int(input("Enter number of seats to book (or -1 to exit): "))
            if num_seats == -1:
                print("Exiting booking system.")
                break
            elif num_seats < 1 or num_seats > 7:
                print("You can only book between 1 and 7 seats.")
                continue

            # Ask the user for their preferred row
            preferred_row = int(input(f"Enter the preferred row number (1 to {len(coach)}): "))
            if preferred_row < 1 or preferred_row > len(coach):
                print("Invalid row number. Please enter a valid row.")
                continue

            # Try to book in the preferred row
            booked_seats = book_seats_in_row(preferred_row, num_seats)
            if len(booked_seats) < num_seats:
                # Ask user if they want to auto-book nearby seats
                choice = input("Not enough seats in the preferred row. Book nearby seats? (y/n): ").strip().lower()
                if choice == 'y':
                    remaining_seats = num_seats - len(booked_seats)
                    additional_seats = find_and_book_in_any_row(remaining_seats)
                    booked_seats += additional_seats

            if booked_seats:
                print(f"Seats booked: {', '.join(booked_seats)}")
            else:
                print("Not enough seats available for this request.")

            # Show updated seat layout
            show_seats()
        except ValueError:
            print("Please enter a valid number.")


show_seats()
start_booking()

