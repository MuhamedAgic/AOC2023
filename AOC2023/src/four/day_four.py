


def day_4_part_1(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    card_scores = []
    for line in lines:
        card_nr = int(line.split(':')[0].split()[1])
        winning_nums = [int(x) for x in line.split('|')[0].split(':')[1].split()]
        my_nums =  [int(x) for x in line.split('|')[1].split()]

        print(f"Card {card_nr}\n    winning nums {winning_nums}\n    my nums {my_nums}")

        score_current_card = 0
        has_winning_num = False
        for my_num in my_nums:
            if my_num in winning_nums:
                if not has_winning_num: # als dit de eerste was +1
                    score_current_card += 1
                else:
                    score_current_card *= 2
                
                has_winning_num = True
            
            
        card_scores.append(score_current_card)
    
    ans = sum(card_scores)
    print("Answer part one: ", ans)
    return ans


filename = "D:/git/magic/aoc2023/aoc2023/src/four/input.txt"
day_4_part_1(filename)