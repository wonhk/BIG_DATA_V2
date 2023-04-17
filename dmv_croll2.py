from dmv_croll import get_dmv

mvlist = get_dmv()
print(mvlist)

for m in mvlist:
    print(f'{m[0]}위, 제목: {m[1]}, 평점: {m[2]} ')