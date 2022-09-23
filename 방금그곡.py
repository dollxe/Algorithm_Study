def parsing_time(t):
    temp = t.split(':')
    return (int(temp[0])*60 + int(temp[1]))

def replace_music(m):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return m

def solution_bak(m, musicinfos):
    answers = No
    for mi in musicinfos:
        start, end, name, music = mi.split(',')
        start = parsing_time(start)
        end = parsing_time(end)

        listen_music = ''
        i = 0
        while start != end:
            if i >= len(music): i -= len(music)
            listen_music += music[i]
            if i == len(music)-1:
                listen_music += '.'
            elif music[i+1] != '#':
                listen_music += '.'
            else:
                pass
            
            start += 1
            i += 1
        
        parsed_m = ''
        for i, s in enumerate(m):
            parsed_m += s
            if i == len(m)-1:
                parsed_m += '.'
            elif m[i+1] != '#':
                parsed_m += '.'
            else:
                pass

        print(listen_music, '\t', parsed_m)

        if parsed_m in listen_music:
            answers.append((end-start, start, name))

    if answers:
        return sorted(answers, key=lambda x: (-x[0], x[1]))[0][2]
    else:
        return "(None)"

def solution(m, musicinfos):
    answer = None
    for mi in musicinfos:
        start, end, name, music = mi.split(',')
        start = parsing_time(start)
        end = parsing_time(end)

        music = replace_music(music)

        listen_music = ''
        i = 0
        while start != end:
            if i >= len(music): i -= len(music)
            listen_music += music[i]
            start += 1
            i += 1

        m = replace_music(m)

        if m in listen_music:
            if (not answer) or (answer[0] < (nd-start)) or (answer[0] == (end-start) and answer[1] > start):
                answer = (end-start, start, name)

    if answer: return answer[-1]
    return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print()
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))