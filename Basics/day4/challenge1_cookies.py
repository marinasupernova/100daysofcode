cookies = ['R6', 'C5', 'C3', 'C8', 'R7', 'R7','C6', 'C9', 'C10', 'R8', 'C2', 'C7', 'R4']


c_cookies = [];

for i in range(len(cookies)):
    if cookies[i][0] == 'C': 
        c_cookies.append(cookies[i][1]);

print(c_cookies);

print(max(c_cookies));