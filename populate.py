import re

with open('SUMMARY.md') as summary:
    for line in summary:
        try:
            file = re.findall('\((.*\.md)\)', line)[0]
            with open(file, 'w') as output:
                string = "{% include 'git+https://github.com/catedu/google-classroom-2018.git/" + file + "' %}"
                output.write(string)
        except:
            print('índice fuera de rango')
