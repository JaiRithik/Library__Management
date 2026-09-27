from datetime import date, timedelta 
from db_config import connect_db 
import os 
 
def borrow_book(member_id): 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    cursor.execute("SELECT * FROM books WHERE quantity > 0") 
    available_books = cursor.fetchall( ) 
    if not available_books: 
        print("No books available for borrowing!") 
        print("\n=================================") 
        return 
    while True: 
        print("\n========= Borrow a Book =========\n") 
        print("1. Search by Title") 
        print("2. Search by Author") 
        print("3. Search by Genre") 
        print("4. Search by Rating") 
        print("5. Show all the books in Library") 
        print("6. Back to Borrow/Return System") 
        print("\n=================================") 
        print( ) 
        search_choice = input("Enter your choice (1-6): ").strip( ) 
        os.system('cls') 
 
        if search_choice == "1": 
            title = input("Enter the title of the book: ").strip( ) 
            book_update("title", title, member_id) 
            input("Press Enter to return...") 
            os.system('cls') 
        elif search_choice == "2": 
            author = input("Enter the author of the book: ").strip( ) 
            book_update("author", author, member_id) 
            input("Press Enter to return...") 
            os.system('cls')         
        elif search_choice == "3": 
            print('Available Genres:') 
            print( ) 
            cursor.execute("SELECT DISTINCT genre FROM books WHERE quantity > 0;") 
            genres_available = cursor.fetchall( ) 
            for genres in genres_available: 
                print(str(genres_available.index(genres)+1)+'.'+ genres[0])             
            genre_choice = input('\nWould you like to select from the above genres ( Y/N )?').strip( ).lower( ) 
            if genre_choice != 'y': 
                os.system('cls') 
                continue 
            while True: 
                try: 
                    genre_index = int(input("Enter the No. of the genre of the book: ").strip( 
)) 
                    if genre_index < 1 or genre_index > len(genres_available): 
                        print("Invalid genre index. Please try again.") 
                        input("Press Enter to continue...") 
                        os.system('cls') 
                        continue 
                    break 
                except ValueError: 
                    print("Invalid input. Please enter a number.") 
                    input("Press Enter to continue...") 
                    os.system('cls') 
                    continue 
            genre = genres_available[genre_index-1][0] 
            book_update("genre", genre, member_id) 
            input("Press Enter to return...") 
            os.system('cls') 
        elif search_choice == "4": 
            print('Rating of Books lies between 1 to 5') 
 
            try: 
                rating_input = input("Enter the rating of the book: ").strip( ) 
                if not rating_input.isdigit( ): 
                    print("Invalid input. Please enter a number.") 
                    input("Press Enter to continue...") 
                    os.system('cls') 
                    continue                 
                rating = int(rating_input) 
                if rating < 1 or rating > 5: 
                    print("Rating must be between 1 and 5.") 
                    input("Press Enter to continue...") 
                    os.system('cls') 
                    continue 
                book_update("rating", rating, member_id) 
                input("Press Enter to return...") 
                os.system('cls') 
            except ValueError: 
                print("Invalid input. Please enter a number for rating.").strip( ) 
                input("Press Enter to continue...") 
                os.system('cls') 
                continue 
        elif search_choice == "5": 
            print('Availible books:') 
            for book in available_books: 
                print(available_books.index(book)+1,'. ',book[1]) 
            print("\n=================================\n") 
            print("Do You want to borrow a book from the above list?") 
            sub_desire = input("Enter 'Y' or 'N': ").strip( ).lower( ) 
            if sub_desire != 'y': 
                os.system('cls') 
                continue 
            print( ) 
            try: 
                sno_choice = input("Enter the serial numbers of the books you want to borrow separated by commas: ").strip( ) 
                sno_choice = [int(i.strip( )) - 1 for i in sno_choice.split(",")] 
            except ValueError: 
                print("Invalid input. Please enter numbers separated by commas.") 
                input("Press Enter to continue...") 
                os.system('cls') 
                return             
            for sub_choice_index in sno_choice: 
                if sub_choice_index < 0 or sub_choice_index >= len(available_books): 
                    os.system('cls') 
 
                    print(f"Invalid choice. {sub_choice_index + 1} can't exist. Please enter a valid serial number.") 
                    input("Press Enter to continue...") 
                    os.system('cls') 
                    continue  
                title = available_books[sub_choice_index][1] 
                author = available_books[sub_choice_index][2]                 
                os.system('cls') 
                print(f"\nSelected Book:\nTitle: {title}\nAuthor: {author}") 
                sub_result = available_books[sub_choice_index] 
                book_fees(member_id, sub_result, title) 
                print("\n=================================") 
                input("Press Enter to return...") 
                os.system('cls') 
            input("Press Enter to return...") 
            os.system('cls') 
        elif search_choice == "6": 
            break        
        else: 
            print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
    conn.close( ) 
def book_update(feature_name, feature, member_id): 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    if feature_name in ['title', 'author']: 
        feature = feature.lower( ) 
        cursor.execute(f"SELECT * FROM books WHERE LOWER({feature_name}) = %s AND quantity > 0", (feature,)) 
    elif feature_name in ['rating', 'genre']: 
        cursor.execute(f"SELECT * FROM books WHERE {feature_name} = %s AND quantity > 0", (feature,)) 
    result = cursor.fetchall( ) 
    os.system('cls') 
    if result and len(result) == 1: 
        for book in result: 
            print('\n',f"Title: {book[1]}\n Author: {book[2]}\n Genre: {book[3]}\n Quantity: {book[4]}\n Rating: {book[5]}\n") 
        print("\n=================================\n") 
        print("Do You want to borrow a book from the above list?") 
        sub_desire = input("Enter 'Y' or 'N': ").strip( ).lower( ) 
        if sub_desire != 'y': 
 
            os.system('cls') 
            return         
        sub_choice_index = 0 
        title = result[sub_choice_index][1] 
        author = result[sub_choice_index][2] 
        os.system('cls') 
        print(f"\nSelected Book:\nTitle: {title}\nAuthor: {author}") 
        sub_result = result[sub_choice_index]         
        book_fees(member_id, sub_result, title) 
        print("\n=================================") 
    elif result: 
        print( ) 
        for book in result: 
            print(result.index(book)+1,". \n",f"Title: {book[1]}\n Author: {book[2]}\n Genre: {book[3]}\n Quantity: {book[4]}\n Rating: {book[5]}\n") 
        print("\n=================================\n") 
        print("Do You want to borrow a book from the above list?") 
        sub_desire = input("Enter 'Y' or 'N': ").strip( ).lower( ) 
        if sub_desire != 'y': 
            os.system('cls') 
            return 
        print( ) 
        try: 
            sno_choice = input("Enter the serial numbers of the books you want to borrow separated by commas: ").strip( ) 
            sno_choice = [int(i.strip( )) - 1 for i in sno_choice.split(",")] 
        except ValueError: 
            print("Invalid input. Please enter numbers separated by commas.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            return         
        for sub_choice_index in sno_choice: 
            if sub_choice_index < 0 or sub_choice_index >= len(result): 
                print(f"Invalid choice. {sub_choice_index + 1} can't exist. Please enter a valid serial number.") 
                input("Press Enter to continue...") 
                os.system('cls') 
                continue  
            title = result[sub_choice_index][1] 
            author = result[sub_choice_index][2] 
            os.system('cls') 
            print(f"\nSelected Book:\nTitle: {title}\nAuthor: {author}") 
            sub_result = result[sub_choice_index]             
            book_fees(member_id, sub_result, title) 
 
            print("\n=================================\n") 
            input("Press Enter to return...") 
            os.system('cls') 
    else: 
        print('Book is not Availible.') 
        input("Press Enter to return...") 
        os.system('cls') 
        return 
    conn.close( ) 
def book_fees(member_id, sub_result, title): 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    due_date = date.today( ) + timedelta(days=60) 
    fee = 0.00 
    print(f"\n{title} is expected to be returned on {due_date}") 
    print("A fee of ₹10 per day will be charged after 60 days.") 
    book_id = sub_result[0] 
    cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s AND quantity > 0", (book_id,))     
    if cursor.rowcount == 0: 
        print(f"\nError: '{title}' is currently out of stock.") 
        conn.rollback( ) 
        conn.close( ) 
        return 
    cursor.execute(""" 
    INSERT INTO transactions (book_id, member_id, borrow_date, expected_date, 
fees) 
    VALUES (%s, %s, %s, %s, %s) 
""", (book_id, member_id, date.today( ), due_date, fee)) 
    conn.commit( ) 
    conn.close( ) 
    print(f"{title} borrowed successfully!") 
def return_book(member_id): 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    print("\n========= Return a book =========\n") 
    print("Returnable Books:") 
    cursor.execute(""" 
        SELECT t.transaction_id, t.expected_date, t.fees, b.book_id, b.title 
        FROM transactions t 
        JOIN books b ON t.book_id = b.book_id 
        WHERE t.member_id = %s 
        AND t.return_date IS NULL; 
    """, (member_id,)) 
 
    rows = cursor.fetchall( ) 
    if not rows: 
        print("No books to return.") 
        print("\n=================================") 
        input("Press Enter to return..") 
        os.system('cls') 
        conn.close( ) 
        return 
    for i, row in enumerate(rows): 
        print(f"{i + 1}. {row[4]} (Due: {row[1]})") 
    print("\n=================================\n") 
    try: 
        selection = int(input("Enter the number of the book to return: ").strip( )) 
        if selection < 1 or selection > len(rows): 
            print("Invalid selection.") 
            conn.close( ) 
            input("Press Enter to return...") 
            return 
        transaction = rows[selection - 1] 
        transaction_id = transaction[0] 
        expected_date = transaction[1] 
        initial_fees = transaction[2] 
        book_id = transaction[3] 
        book_title = transaction[4] 
    except ValueError: 
        print("Invalid input. Please enter a number.") 
        conn.close( ) 
        input("Press Enter to return...") 
        os.system('cls') 
        return 
    days_late = (date.today( ) - expected_date).days 
    late_fee_per_day = 10 
    if days_late <= 0: 
        late_fee = 0.0 
    else: 
        late_fee = days_late * late_fee_per_day     
    total_fee = float(initial_fees) + late_fee 
    print(f"Return the book '{book_title}' and Pay ₹{total_fee}!") 
    input("Press Enter to Pay with Cash..") 
    os.system('cls') 
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id = %s", (book_id,))     
    rate_choice = input("Would you like to rate the book? ( Y/N ):").strip( ).lower( 
) 
 
    rating = None 
    if rate_choice == "y": 
        try: 
            rating = int(input("Rate the book (1 to 5): ").strip( )) 
            if rating < 1 or rating > 5: 
                print("Rating out of range. Skipping rating.") 
                rating = None 
        except ValueError : 
            print("Invalid rating. Skipping rating.") 
            rating = None         
    if rating is None: 
        print("We respect your valuable time! Feedback is optional.") 
        cursor.execute(""" 
            UPDATE transactions 
            SET return_date = %s 
            WHERE transaction_id = %s 
        """, (date.today( ), transaction_id)) 
        os.system('cls') 
    else: 
        cursor.execute(""" 
            UPDATE transactions 
            SET return_date = %s, rating = %s 
            WHERE transaction_id = %s 
        """, (date.today( ), rating, transaction_id)) 
    if rating is not None: 
        cursor.execute(""" 
            SELECT AVG(rating) 
            FROM transactions 
            WHERE book_id = %s AND rating IS NOT NULL 
        """, (book_id,)) 
        result = cursor.fetchone( ) 
        if result and result[0] is not None: 
            avg_rating = round(result[0], 2) 
            cursor.execute("UPDATE books SET rating = %s WHERE book_id = %s", 
(avg_rating, book_id)) 
            print(f"Thank you for rating! The new average rating for this book is {avg_rating}.") 
    print("Book returned successfully!") 
    print("\n=================================") 
    input("Press Enter to return..") 
    os.system('cls') 
    conn.commit( ) 
    conn.close( ) 
def add_book( ): 
 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    print("========= Add a Book ============\n") 
    print("Please enter the book details below:") 
    while True: 
        title = input("Enter Book Title: ").strip( ).capitalize( ) 
        if title : 
            break 
    while True: 
        author = input("Enter Book Author: ").strip( ).capitalize( ) 
        if author: 
            break     
    while True: 
        genre = input("Enter Book Genre: ").strip( ).capitalize( ) 
        if genre: 
            break 
    while True: 
        try: 
            quantity = int(input("Quantity: ").strip( )) 
            if quantity <= 0: 
                print('Quantity can’t be less than 1.') 
            break 
        except ValueError: 
            print("Invalid quantity. Enter a valid quantity.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue 
    while True: 
        invoice_no = input("Enter Invoice Number: ").strip( ) 
        if invoice_no: 
            break 
    while True: 
        publisher_name = input("Enter Publisher Name: ").strip( ) 
        if publisher_name: 
            break 
    while True: 
        store_name = input("Enter Store Name: ").strip( ) 
        if store_name: 
            break 
    while True: 
        try: 
            amt = float(input("Enter Price: ")) 
            if amt >= 0: 
                break 
 
        except ValueError: 
            print("Enter a valid Price.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue     
    while True: 
        purchase_date_str = input("Enter Purchase Date (YYYY-MM-DD): ").strip( ) 
        if not purchase_date_str: 
            print("Purchase date is required.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue             
        try: 
            year, month, day = map(int, purchase_date_str.replace('/', '-').split('-')) 
            purchase_date = date(year, month, day)             
            if purchase_date > date.today( ): 
                print("Purchase date cannot be in the future.") 
                input("Press Enter to continue...") 
                os.system('cls') 
                continue 
            break 
        except ValueError: 
            print("Invalid date format or value. Please use YYYY-MM-DD.") 
            input("Press Enter to continue...") 
            os.system('cls') 
            continue     
    cursor.execute(""" 
        SELECT book_id 
        FROM books  
        WHERE LOWER(title) = %s  
        AND LOWER(author) = %s  
        AND LOWER(genre) = %s 
    """, (title.lower( ), author.lower( ), genre.lower( ))) 
    existing = cursor.fetchone( ) 
    if existing: 
        cursor.execute(""" 
            UPDATE books 
            SET quantity = quantity + %s, 
                invoice_no = %s, 
                purchase_date = %s, 
                publisher_name = %s, 
                store_name = %s, 
                amt = %s 
            WHERE book_id = %s 
 
        """, (quantity, invoice_no, purchase_date, publisher_name, store_name, amt, 
existing[0])) 
        print("Book already exists. Updated quantity and details.") 
    else: 
        cursor.execute(""" 
            INSERT INTO books (title, author, genre, quantity, invoice_no, 
purchase_date, publisher_name, store_name, amt) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """, (title, author, genre, quantity, invoice_no, purchase_date, publisher_name, 
store_name, amt)) 
        print("New book added successfully.")            
    conn.commit( ) 
    conn.close( ) 
    print("Book added successfully!") 
    print("\n=================================") 
    input("Press Enter to return...") 
    os.system('cls') 
def remove_book( ): 
    conn = connect_db( ) 
    cursor = conn.cursor( ) 
    print("\n========= Remove Book ===========\n") 
    while True: 
        title = input("Enter the title of the book: ").strip( ) 
        if title: 
            break 
    while True: 
        author = input("Enter the author of the book: ").strip( ) 
        if author: 
            break 
    cursor.execute("SELECT * FROM books WHERE title = %s AND author = %s", 
(title, author)) 
    results = cursor.fetchall( ) 
    if not results: 
        print(" Book not found.") 
        conn.close( ) 
        input("Press Enter to Return...") 
        os.system('cls') 
        return 
    print(f"\nFound {len(results)} book(s):") 
    for i, book in enumerate(results): 
        print(f"{i + 1}. Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Publisher: {book[9]}") 
    print("\n=================================\n") 
    try: 
 
        selection = int(input("Enter the number of the book to delete: ").strip( )) 
        if selection < 1 or selection > len(results): 
            print("Invalid selection.") 
            conn.close( ) 
            input("Press Enter to return...") 
            return         
        selected_book = results[selection - 1] 
        book_id = selected_book[0]         
        confirm = input(f"Are you sure you want to delete '{selected_book[1]}' (ID: {book_id})? ( Y/N ): ").strip( ).lower( ) 
        if confirm == 'y': 
            cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,)) 
            conn.commit( ) 
            print("Book removed successfully.") 
        else: 
            print("Operation cancelled.") 
    except ValueError: 
        print("Invalid input. Please enter a number.") 
        input("Press Enter to continue...") 
        os.system('cls')     
    print("\n=================================") 
    input("Press Enter to return...") 
    os.system('cls') 
    conn.close( )
