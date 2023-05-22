from collections import deque


def main(eggs, papers):
    boxes = 0
    box_size = 50
    egg = 0
    paper = 0

    while eggs and papers:
        egg = check_egg(eggs, papers)
        if egg == 2.5:
            break
        paper = papers.pop()

        boxes = check_box(egg, paper, boxes, box_size)

    print(format_the_result(boxes, eggs, papers))


def check_egg(eggs, papers):
    try:
        egg = eggs.popleft()

        while egg <= 0 or egg == 13:

            if egg == 13:
                papers[0], papers[-1] = papers[-1], papers[0]

            egg = eggs.popleft()
    except IndexError:
        return 2.5

    return egg


def check_box(egg, paper, boxes, box_size):

    if egg + paper <= box_size:
        boxes += 1

    return boxes


def format_the_result(boxes, eggs, papers):
    result = ""

    if boxes:
        result += f"Great! You filled {boxes} boxes.\n"
    else:
        result += "Sorry! You couldn't fill any boxes!\n"

    if eggs:
        result += f"Eggs left: {', '.join(str(egg) for egg in eggs)}\n"

    if papers:
        result += f"Pieces of paper left: {', '.join(str(paper) for paper in papers)}\n"

    return result


eggs = deque([int(el) for el in input().split(", ")])
papers = deque([int(el) for el in input().split(", ")])

main(eggs, papers)