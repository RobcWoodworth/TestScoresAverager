#!/usr/bin/env python3
# Rob Woodworth CS223 2/2/22 Chapter 6 Exercise 1
def get_english():
    total1 = 0
    counter1 = 0
    list1 = []
    while True:
        if counter1 < 5:
            score1 = input("Enter a test score: ")
            if score1 == "x":
                return total1, counter1, list1
            else:
                if 0 <= int(score1) <= 100:
                    total1 += int(score1)
                    counter1 += 1
                    list1.append(int(score1))
                else:
                    print("Test score must be 0 to 100. Score discarded.")
                list1.sort()
        else:
            return total1, counter1, list1


def process_scores(list1):
    average1 = sum(list1) / len(list1)
    print(f"-------------------------")
    print(f"Scores entered    :{list1}")
    print(f"Score total:       {sum(list1)}")
    print(f"Number of Scores:  {(len(list1))}")
    print(f"Average Score:     {average1:.1f}")
    print(f"High score:        {(max(list1))}")
    print(f"Low score:         {(min(list1))}")
    print(f"Median score:      {(list1[len(list1) // 2])}")


def main():
    print("\n~~Robert's Test Scores program~~\n\nMaximum of 5 scores "
          " \nEnter 'x' to exit\n")
    total1, count1, list1 = get_english()
    process_scores(list1)


if __name__ == "__main__":
    main()
