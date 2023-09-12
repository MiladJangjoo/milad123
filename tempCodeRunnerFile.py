
input is a list
output is a number


"""
def count_glove_pairs(glove_colors):
    colors={}
    for i in glove_colors:
        if i not in colors:
            colors[i] = 1
        elif i in colors:
            colors[i] += 1
    return colors

print(count_glove_pairs(["red", "green", "red", "blue", "blue"]))