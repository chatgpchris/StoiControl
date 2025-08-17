import datetime
import random

# Questions and answer options with internal scores
questions = {
    1: {
        "text": "Have you worried about things outside your control lately?",
        "answers": [
            {"text": "I have spent a lot of time and mental energy obsessing over things I couldn’t change, replaying scenarios in my mind.", "score": 0},
            {"text": "I have worried often, but occasionally reminded myself they were beyond my control.", "score": 1},
            {"text": "I have caught myself worrying a few times and redirected my focus toward what I could do.", "score": 2},
            {"text": "I rarely worried about uncontrollable events and quickly let such thoughts go.", "score": 3},
            {"text": "Not applicable in my situation", "score": None}
        ]
    },
    2: {
        "text": "When something unexpected happened recently, how calmly did you respond?",
        "answers": [
            {"text": "I reacted with visible frustration, anger, or panic, and it affected the rest of my day.", "score": 0},
            {"text": "I reacted poorly at first but made a small effort to calm down later.", "score": 1},
            {"text": "I felt some irritation or stress but maintained a mostly composed demeanor.", "score": 2},
            {"text": "I adapted smoothly and stayed composed without letting it disturb me internally.", "score": 3},
            {"text": "Not applicable in my situation.", "score": None}
        ]
    },
    3: {
        "text": "Did you accept outcomes without resentment?",
        "answers": [
            {"text": "I held grudges or repeatedly felt bitter about how things turned out.", "score": 0},
            {"text": "I accepted some outcomes but held onto frustration over others.", "score": 1},
            {"text": "I accepted most outcomes, though a little resentment lingered.", "score": 2},
            {"text": "I fully accepted all outcomes, focusing on what I could learn rather than what I lost.", "score": 3},
            {"text": "Not applicable in my situation on this occasion.", "score": None}
        ]
    },
    4: {
        "text": "How often did you remind yourself of what is and is not under your control?",
        "answers": [
            {"text": "I never considered the difference between what I can and cannot control.", "score": 0},
            {"text": "I thought about it once or twice but quickly forgot in the moment.", "score": 1},
            {"text": "I reminded myself fairly often and it influenced some of my choices.", "score": 2},
            {"text": "I consistently kept this distinction in mind and acted accordingly.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    5: {
        "text": "Did you mentally rehearse possible challenges in the morning or before sleep?",
        "answers": [
            {"text": "I made no effort to anticipate possible difficulties.", "score": 0},
            {"text": "I briefly thought about possible problems but without a plan.", "score": 1},
            {"text": "I considered a few scenarios and thought about how to respond.", "score": 2},
            {"text": "I deliberately visualized potential challenges and prepared my mindset for them.", "score": 3},
            {"text": "Not applicable in my situation.", "score": None}
        ]
    },
    6: {
        "text": "Did you get angry or frustrated at people?",
        "answers": [
            {"text": "Yes, and I expressed it strongly without trying to control it.", "score": 0},
            {"text": "Yes, but I tried to calm down after the fact.", "score": 1},
            {"text": "I felt irritation but didn’t let it take over my behavior.", "score": 2},
            {"text": "I mostly remained calm and patient, even when provoked.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    7: {
        "text": "How quickly did you regain emotional balance after negative events?",
        "answers": [
            {"text": "I stayed upset for hours or more.", "score": 0},
            {"text": "I calmed down within several hours but still felt mentally drained.", "score": 1},
            {"text": "I regained balance within an hour and carried on productively.", "score": 2},
            {"text": "I recovered almost immediately and refocused my attention.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    8: {
        "text": "When criticized, how rational and calm was your response?",
        "answers": [
            {"text": "I reacted defensively or aggressively without listening carefully.", "score": 0},
            {"text": "I listened briefly but mostly focused on defending myself.", "score": 1},
            {"text": "I stayed calm and considered the feedback, though I felt discomfort.", "score": 2},
            {"text": "I welcomed the feedback with an open mind.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    9: {
        "text": "Did you express gratitude despite difficulties?",
        "answers": [
            {"text": "I felt no gratitude and only saw the negatives.", "score": 0},
            {"text": "I expressed gratitude sometimes but mostly focused on what went wrong.", "score": 1},
            {"text": "I expressed gratitude multiple times despite challenges.", "score": 2},
            {"text": "I actively looked for reasons to be grateful and found many.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    10: {
        "text": "Did you make decisions based on reason rather than impulse?",
        "answers": [
            {"text": "I acted mostly on emotion or impulse without thinking.", "score": 0},
            {"text": "I sometimes paused to think but still acted impulsively in many cases.", "score": 1},
            {"text": "Most of my decisions were deliberate and reasoned.", "score": 2},
            {"text": "All significant decisions were made with careful reasoning and calmness.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    11: {
        "text": "Did you question your initial emotional reactions before acting?",
        "answers": [
            {"text": "I acted on my first emotional response without reflection.", "score": 0},
            {"text": "I paused a few times but usually followed my initial emotions.", "score": 1},
            {"text": "I regularly paused to assess whether my emotions were justified.", "score": 2},
            {"text": "I consistently evaluated my emotions before acting and adjusted my behavior accordingly.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    12: {
        "text": "How much time did you spend thinking about philosophical principles or virtues?",
        "answers": [
            {"text": "I gave no thought to such principles.", "score": 0},
            {"text": "I thought about them briefly but did not apply them.", "score": 1},
            {"text": "I reflected on them and tried to apply them in small ways.", "score": 2},
            {"text": "I deeply reflected on them and integrated them into my days’ actions.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    13: {
        "text": "Did you keep in mind the impermanence of life and possessions?",
        "answers": [
            {"text": "I never considered it.", "score": 0},
            {"text": "I thought of it rarely and briefly.", "score": 1},
            {"text": "I remembered it a few times, which shaped my perspective.", "score": 2},
            {"text": "It was a guiding thought in how I valued experiences and possessions.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    14: {
        "text": "Did you act honestly in all your dealings?",
        "answers": [
            {"text": "I lied or misled someone, even in small matters.", "score": 0},
            {"text": "I avoided major dishonesty but bent the truth in small ways.", "score": 1},
            {"text": "I was honest in most situations.", "score": 2},
            {"text": "I was completely truthful, even when inconvenient.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    15: {
        "text": "Were your actions aligned with your values and principles?",
        "answers": [
            {"text": "I almost always acted in ways that clearly violated my principles.", "score": 0},
            {"text": "I acted against my values for convenience, many times.", "score": 1},
            {"text": "I mostly acted in line with my values.", "score": 2},
            {"text": "I consistently lived according to my principles.", "score": 3},
            {"text": "Not applicable in my situation.", "score": None}
        ]
    },
    16: {
        "text": "Did you show fairness in interactions, even when inconvenient?",
        "answers": [
            {"text": "I acted unfairly when it benefitted me.", "score": 0},
            {"text": "I was fair most of the time but compromised in some cases.", "score": 1},
            {"text": "I was fair even in difficult situations.", "score": 2},
            {"text": "I actively went out of my way to ensure fairness for others.", "score": 3},
            {"text": "Not applicable on this occasion.", "score": None}
        ]
    },
    17: {
        "text": "Did you resist the temptation to take an easy but morally wrong path?",
        "answers": [
            {"text": "I gave in without much thought.", "score": 0},
            {"text": "I struggled but gave in occasionally.", "score": 1},
            {"text": "I resisted in most cases.", "score": 2},
            {"text": "I resisted every temptation and felt stronger for it.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    18: {
        "text": "Did you stick to your commitments despite difficulties?",
        "answers": [
            {"text": "I abandoned my commitments when it got tough.", "score": 0},
            {"text": "I completed some but dropped others.", "score": 1},
            {"text": "I fulfilled most of my commitments despite challenges.", "score": 2},
            {"text": "I honored all my commitments without compromise.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    19: {
        "text": "Did you remain focused and productive despite distractions?",
        "answers": [
            {"text": "I allowed distractions to consume most of my time.", "score": 0},
            {"text": "I gave in to distractions often but did some productive work.", "score": 1},
            {"text": "I stayed productive most of the time with minor lapses.", "score": 2},
            {"text": "I worked with focus and efficiency throughout.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    20: {
        "text": "Did you accept setbacks as opportunities to learn?",
        "answers": [
            {"text": "I saw setbacks only as failures and felt discouraged.", "score": 0},
            {"text": "I acknowledged learning potential but mostly felt defeated.", "score": 1},
            {"text": "I found lessons in most setbacks.", "score": 2},
            {"text": "I welcomed setbacks as valuable learning opportunities.", "score": 3},
            {"text": "Not applicable in my situation.", "score": None}
        ]
    },
     21: {
        "text": "Did you follow your planned schedules?",
        "answers": [
            {"text": "I ignored my schedules completely.", "score": 0},
            {"text": "I followed them loosely, skipping major tasks.", "score": 1},
            {"text": "I followed schedules for the most part.", "score": 2},
            {"text": "I followed my plans closely and achieved what I set out to do.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    22: {
        "text": "Did you practice moderation in food, drink, or entertainment?",
        "answers": [
            {"text": "I overindulged without restraint.", "score": 0},
            {"text": "I tried to moderate but often gave in.", "score": 1},
            {"text": "I was mostly moderate with a few excesses.", "score": 2},
            {"text": "I practiced moderation consistently and deliberately.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    23: {
        "text": "Did you avoid wasting time on trivial things?",
        "answers": [
            {"text": "I spent large parts of my time on pointless distractions.", "score": 0},
            {"text": "I wasted some time but did meaningful work as well.", "score": 1},
            {"text": "I minimized wasted time and stayed focused on important tasks.", "score": 2},
            {"text": "I used my time purposefully and avoided trivialities completely.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    },
    24: {
        "text": "Did you choose long-term benefit over short-term pleasure?",
        "answers": [
            {"text": "I almost always chose immediate gratification.", "score": 0},
            {"text": "I sometimes considered long-term consequences but still went for quick pleasure.", "score": 1},
            {"text": "I often prioritized long-term benefits over short-term gains.", "score": 2},
            {"text": "I consistently made choices with long-term value in mind.", "score": 3},
            {"text": "Not applicable.", "score": None}
        ]
    }
}

status_messages = {
    "0-39": [
        "The Unsettled Mind in the Anti-Stoic Zone: \nLike a ship without a rudder, you are at the mercy of the winds. Even small annoyances may have thrown you off course this time. Epictetus would remind you that storms are inevitable — but steering is always your task. Begin tomorrow by anchoring your mind before the first wave hits.",
        "The Unsettled Mind in the Anti-Stoic Zone: \nThe passions were your masters. Anger, desire, or fear may have decided your path for you. Marcus Aurelius faced such days too — yet each new morning he attempted to return to the discipline of reason. Let tonight’s reflection be your turning point.",
        "The Unsettled Mind in the Anti-Stoic Zone: \nYou’ve wandered far from the citadel of calmness. But remember: no one is born a Stoic Emperor — they are made, choice by choice, habit by habit. Start small: control your breath, control your tongue, control your thoughts.",
        "The Unsettled Mind in the Anti-Stoic Zone: \nIt seems externals had the upper hand this time. Seneca would counsel you not to despair: even a weak flame can be coaxed back to life. Tomorrow, light the fire again by deciding in advance how you’ll meet life’s provocations.",
        "The Unsettled Mind in the Anti-Stoic Zone: \nYou’ve tasted how it feels to let events drag you. This is not defeat — this is your map. Now you know the places where your fortress walls are thin. Begin reinforcing them before the next siege."
    ],
    "40-59": [
        "The Growing Practitioner: \nYou’ve begun to grasp that your mind is yours to govern, yet the gates are still often left open. Marcus might commend your effort but urge greater vigilance. Strengthen your watch over the first thoughts that enter.",
        "The Growing Practitioner: \nYou’ve landed solid strikes, yet openings remain. Seneca would remind you: train in peace for what you’ll face in chaos. Each calm exercise of reason strengthens your armor for life’s storms.",
        "The Growing Practitioner: \nYou’re moving away from the sway of impulse, though it still whispers in your ear. Epictetus would counsel: ‘Events do not disturb us; our judgments about them do.’ Keep working on changing those judgments before they harden into reactions.",
        "The Growing Practitioner: \nYour roots are beginning to grip the soil, but strong winds can still topple you. Think daily of what is truly yours to command, and let the rest blow past without stealing your peace.",
        "The Growing Practitioner: \nHalfway to mastery is knowing you are not yet master. Today shows you have some control, some calm — but also room to deepen them. Take pride in progress, but don’t linger there."
    ],
    "60-79": [
        "The Steady Walker: \nYou are becoming familiar with the Stoic path. You recover quickly from missteps, and your mind returns to calmness more often than not. Marcus Aurelius might smile at your persistence — and remind you: ‘The obstacle is the way.’",
        "The Steady Walker: \nLike an archer who hits the target more often than he misses, you’re finding your aim. Now refine your focus: be calm not only when you expect trouble, but also when it arrives unannounced.",
        "The Steady Walker: \nYou’ve built some walls of your inner citadel, but there are still gates that swing open too easily. Consider how you might reinforce them with small, daily disciplines: morning reflection, evening review, mindful speech.",
        "The Steady Walker: \nYour progress is visible: anger fades faster, joy lasts longer, and fear has less grip. Yet a Steady Walker knows there’s always further to go. Each day is another step toward mastery of yourself.",
        "The Steady Walker: \nThe path feels natural now — but beware of complacency. Even seasoned travelers can stumble if they stop watching the road. Keep your reason awake."
    ],
    "80-94": [
        "The Inner Citadel Builder: \nYou’ve raised high walls and your gates are guarded well. Most storms pass over without shaking you. Seneca would praise your composure but warn: never forget the foundations — virtue, reason, and the knowledge of what is truly good.",
        "The Inner Citadel Builder: \nYou are approaching the mastery of yourself. Like a city well-governed, your thoughts and actions serve the common good of your soul. Your next task: teach your calmness to hold not just in solitude but in the noise of the crowd.",
        "The Inner Citadel Builder: \nYou’ve tasted what it means to live as though fortune has no power over you. Marcus Aurelius would say: now see if you can meet both praise and blame with equal steadiness.",
        "The Inner Citadel Builder: \nYour inner citadel is nearly complete. But even Rome fell to carelessness within its walls. Keep training your sentries: attention, gratitude, and the habit of questioning your first impressions.",
        "The Inner Citadel Builder: \nYou are strong in the face of events, gentle toward others, and fair to yourself. This is rare. Guard it, and let it be the seed for an even greater constancy."
    ],
    "95-99": [
        "Philosopher of Life: \nYou live today as the philosophers taught. Anger does not linger, fear does not reign, and joy springs from virtue. If you keep this course, you will not just study the Stoics — you will join their ranks.",
        "Philosopher of Life: \nYour thoughts are ordered, your actions deliberate, your peace unbroken. This is the fruit of daily discipline. Still, remember: practical wisdom is an ideal, never fully reached. Tomorrow’s storms will test you anew.",
        "Philosopher of Life: \nIn the marketplace of life, you have traded impulse for wisdom. Seneca would say: this is wealth beyond coin. Continue to spend it generously in kindness and justice.",
        "Philosopher of Life: \nFew walk so steadily. You have shown what a human can do when guided by reason alone. Keep this flame bright — the world needs its light.",
        "Philosopher of Life: \nYou are living proof that philosophy is not idle talk but a craft. Continue to work it, and you may leave behind not just words, but an example worth imitating."
    ],
    "100": [
        "The Stoic Emperor: \nYou have touched the ideal. Like Marcus Aurelius with his imperial duties or Epictetus in his humble school, you have lived as though virtue were your only treasure. Remember: this is a glimpse, not a possession. Protect it, and seek it again tomorrow.",
        "The Stoic Emperor: \nYou have worn the purple of a Stoic Emperor, not by birth but by mastery of yourself. Fortune could take all else from you and you would remain whole. Carry this into the next dawn.",
        "The Stoic Emperor: \nYou stand shoulder to shoulder with the greats. You meet every trial with calmness, every person with justice, every moment with acceptance. This is the height of the human art.",
        "The Stoic Emperor: \nYou have lived without fear, anger, or grief at what you cannot control. This is what the Stoics called freedom. Now, the task is to keep it — or, if lost, to regain it.",
        "The Stoic Emperor: \nFew ever reach true wisdom, yet today you walked beside it. When you stumble, remember this ground — you have stood here before, and you can stand here again."
    ]
}


def get_user_answers():
    user_answers = {}
    for q_num, q_data in questions.items():
        print(f"\nQ{q_num}: {q_data['text']}")
        for i, option in enumerate(q_data['answers'], start=1):
            print(f"{i}. {option['text']}")
        print("Type 'QUIT' at any time to exit the test.")
        while True:
            ans = input("Select an option number: ").strip()
            if ans.upper() == "QUIT":
                print("You chose to quit the test.")
                return None
            if ans.isdigit() and 1 <= int(ans) <= len(q_data['answers']):
                user_answers[q_num] = int(ans) - 1
                break
            else:
                print("Invalid input. Try again.")
    return user_answers

def calculate_score(user_answers):
    total = 0
    count = 0
    for q_num, idx in user_answers.items():
        score = questions[q_num]['answers'][idx]['score']
        if score is not None:
            total += score
            count += 1
    if count == 0:
        return 0
    max_score = count * 3
    percentage = round((total / max_score) * 100)
    return percentage

def get_status_message(score):
    if score <= 39:
        key = "0-39"
    elif score <= 59:
        key = "40-59"
    elif score <= 79:
        key = "60-79"
    elif score <= 94:
        key = "80-94"
    elif score <= 99:
        key = "95-99"
    else:
        key = "100"
    return random.choice(status_messages[key])

def welcome_screen():
    print("They say life's a mess. We say, let's clean it up!")
    print("Welcome to StoiControl")
    print("the ultimate self-mastery challenge!\n")
    print("Your mind is the only kingdom you can truly rule, \nso start regaining your inner control \nand learn to handle whatever chaos"
          " the universe throws at you!\n")
    print("Let's test how much Stoic you have recently been.")
    print("1. Take the Stoic Self-Test")
    print("2. Quit")

    while True:
        choice = input("Select an option number: ").strip()
        if choice == "1":
            return True
        elif choice == "2":
            print("Exiting the app. See you next time!")
            return False
        else:
            print("Invalid input. Please type 1 or 2.")

def retake_menu():
    print("\nWhat would you like to do next?")
    print("1. Retake the Stoic Test")
    print("2. Quit")

    while True:
        choice = input("Select an option number: ").strip()
        if choice == "1":
            return True  # Retake
        elif choice == "2":
            print("Exiting the app. See you next time!")
            return False  # Quit
        else:
            print("Invalid input. Please type 1 or 2.")

def main():
    if not welcome_screen():
        return

    keep_playing = True

    while keep_playing:
        user_answers = get_user_answers()
        if user_answers is None:
            return  # User quit mid-test

        score = calculate_score(user_answers)
        message = get_status_message(score)
        test_date = datetime.datetime.now().strftime("%Y-%m-%d")

        print(f"\nTest Date: {test_date}")
        print(f"Your Stoic Score: {score}%")
        print(f"Assessment: \n{message}")


        # Ask user whether to retake or quit
        keep_playing = retake_menu()

if __name__ == "__main__":
    main()
