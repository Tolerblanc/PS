def chk_skill(skill_book,skill_tree):
    tree = [] #스킬 순서가 올바른지 체크하기 위한 리스트
    for skill in skill_tree: 
        if skill in skill_book:
            tree.append(skill) #스킬 트리를 돌면서 선행 스킬 순서에 있는 스킬을 모두 리스트에 넣음 
    tree = "".join(tree)
    if skill_book.startswith(tree) or tree.startswith(skill_book):
        return 1 #리스트를 문자열로 만들어서 검사
    return 0

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += chk_skill(skill,skill_tree)
    return answer