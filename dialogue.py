from benderClass import bender
import random as rand

pairs = [
    [
        r"my name is (.*)",
        [rand.choice(bender().intro),]
    ],
     [
        r"what is your name ?",
        [rand.choice(bender().intro),]
    ],
    [
        r"how are you ?",
        [rand.choice(bender().a_quote),rand.choice(bender().s_quote), rand.choice(bender().ap_quote), ]
    ],
    [
        r"sorry (.*)",
        [rand.choice(bender().p_quote),]
    ],
    [
        r"i'm (.*) doing good",
        [rand.choice(bender().rand_quote),]
    ],
    [
        r"hi|hey|hello",
        [rand.choice(bender().greetings), ]
    ]
]