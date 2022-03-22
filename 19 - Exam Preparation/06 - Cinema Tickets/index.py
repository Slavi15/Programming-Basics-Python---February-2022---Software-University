total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
tickets_per_movie = 0

finish_encounter = 0

while True:
    movie_name = str(input())

    if movie_name == "Finish":
        p1 = (student_tickets / total_tickets) * 100
        p2 = (standard_tickets / total_tickets) * 100
        p3 = (kid_tickets / total_tickets) * 100
        print(f"""Total tickets: {total_tickets}
        {p1:.2f}% student tickets.
        {p2:.2f}% standard tickets.
        {p3:.2f}% kids tickets.""")
        break

    free_places = int(input())

    while True:
        ticket_type = str(input())

        if ticket_type == "End":
            percent_fullness = (tickets_per_movie / free_places) * 100
            tickets_per_movie = 0
            print(f"{movie_name} - {percent_fullness:.2f}% full.")
            break
        elif ticket_type == "Finish":
            percent_fullness = (tickets_per_movie / free_places) * 100
            tickets_per_movie = 0
            p1 = (student_tickets / total_tickets) * 100
            p2 = (standard_tickets / total_tickets) * 100
            p3 = (kid_tickets / total_tickets) * 100
            print(f"{movie_name} - {percent_fullness:.2f}% full.")
            print(f"""Total tickets: {total_tickets}
            {p1:.2f}% student tickets.
            {p2:.2f}% standard tickets.
            {p3:.2f}% kids tickets.""")
            finish_encounter += 1
            break

        if tickets_per_movie <= free_places:
            if ticket_type == "standard":
                standard_tickets += 1
                total_tickets += 1
                tickets_per_movie += 1
            elif ticket_type == "student":
                student_tickets += 1
                total_tickets += 1
                tickets_per_movie += 1
            elif ticket_type == "kid":
                kid_tickets += 1
                total_tickets += 1
                tickets_per_movie += 1
        
        if tickets_per_movie == free_places:
            percent_fullness = (tickets_per_movie / free_places) * 100
            tickets_per_movie = 0
            print(f"{movie_name} - {percent_fullness:.2f}% full.")
            break

    if finish_encounter > 0:
        break