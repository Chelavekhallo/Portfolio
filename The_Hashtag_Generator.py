def generate_hashtag(s):
    s = s.split()
    e = []
    output = ''
    for x in range(len(s)):
        d = s[x].capitalize()
        e.append(d)

    for i in range(len(e)):
        output+=e[i]
    if output == "":
        return False
    elif len(output)>139:
        return False
    else:
        return f"#{output}"
# The original problem: https://www.codewars.com/users/Vagadza/completed_solutions
