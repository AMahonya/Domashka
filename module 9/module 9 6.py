def all_variants(text):

    for i in range(1, len(text) + 1):
        for j in range(len(text) - i + 1):
            yield text[j:j + i]


text = "abc"
for v in all_variants(text):
    print(v)

# text = "Fil Richeal"
# for vt in all_variants(text):
#     print(vt)
