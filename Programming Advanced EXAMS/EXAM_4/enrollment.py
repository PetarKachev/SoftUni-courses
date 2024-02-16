def gather_credits(required_credits, *args):
    courses = []
    total_credits = 0

    for course_name, course_credits in args:
        if total_credits >= required_credits:
            break

        if course_name not in courses:
            courses.append(course_name)
            total_credits += course_credits

    if total_credits >= required_credits:
        return f"Enrollment finished! Maximum credits: {total_credits}.\n" \
               f"Courses: {', '.join(sorted(courses))}"
    else:
        diff = required_credits - total_credits
        return f"You need to enroll in more courses! You have to gather {diff} credits more."