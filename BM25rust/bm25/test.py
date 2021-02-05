import bm25_roost

corpus = [
    "Donald Trump has responded to news that Screen Actors Guild’s board had “overwhelmingly” voted that he violated their guidelines by inciting the Capitol insurrection and threatened to revoke his membership. In the letter to SAG-AFTRA president Gabrielle Carteris, dated on Thursday and shared by the guild, Mr Trump revoked his membership, and cited his on-screen career highlights in characteristically immodest language. ",
    "The vision of America's place in the world presented by Joe Biden was starkly, and predictably, different from that of Donald Trump, with a focus on undoing the damage done in the last four years as a leading role is reclaimed in the international scene. Biden reassured allies of support, but also warned that it would not be unconditional. He put adversaries on notice, lauded international cooperation, and insisted that core liberal democratic values would be the linchpin on which US global strategy will be based on his watch. The theme was 'America is back', rather than 'America First' and 'Make America Great Again' of the Trump era. But, as with all slogans, it remains to be seen how that translates into reality. 'America First' turned out to mean a doctrinaire turning away from multilateralism and retreat into isolationism. 'Make America Great Again' sucked the nation into a quicksand of division and discord. Biden chose the State Department, instead of the Pentagon or the CIA, to make his first major speech on foreign affairs. This was a message that the key role of diplomacy and diplomats will be restored after the chaos and confusion of the Trump years when advisers like son-in-law Jared Kushner seemed to run their own foreign policy operations. ",
    "Jon Stewart has mocked Donald Trump over his Screen Actors Guild resignation letter. On Thursday (4 February), the former president responded to news that SAG-AFTRA’s board had “overwhelmingly” voted that Trump violated their guidelines by inciting the Capitol insurrection. In the letter, which was shared with Fox News, Trump wrote that he was “revoking” his union membership, adding: “Who cares!” “While I’m not familiar with your work, I’m very proud of my work on movies such as Home Alone 2, Zoolander and Wall Street: Money Never Sleeps; and television shows including The Fresh Prince of Bel-Air, Saturday Night Lives, and of course, one of the most successful shows in television history, The Apprentice – to name just a few!” The letter was widely shared on social media, with comedian Stewart, who joined Twitter following Trump's departure from office, mocking him.",
    "Donald Trump is refusing to testify under oath at his second impeachment trial, which is set to get underway on Tuesday. In a letter to Jamie Raskin, the House Democrats' lead impeachment manager, Mr Trump's lawyers branded the request a 'publicity stunt' and claimed the trial was 'unconstitutional'. 'Your letter only confirms what is known to everyone: you cannot prove your allegations against the 45th President of the United States, who is now a private citizen,' the letter read, in reference to the charge that Mr Trump incited the riot at the Capitol last month. It comes as a letter from Mr Trump himself was made public in which he angrily quit the Screen Actors Guild after the union threatened to revoke his membership. Mr Trump's bizarre message asked, 'Who cares!', in reference to a disciplinary hearing before boasting about his appearances in Home Alone 2, Zoolander and The Fresh Prince of Bel-Air."
]

# Tuning parameters for BM25+ with a lower bound (eps) applied to the inverse frequency
k1 = 1.2  # k1 = [1.2, 2]
b  = 0.7
eps = 0.1
delt = 1.0

bm25 = bm25_roost.BM25(corpus, k1, b, eps, delt)

queries = [
    "Donald Trump",
    "Joe Biden",
    "Screen Actors Guild",
    "Tim Attwell",
    "Jon Stewart",
    "Jon"
]

#bm25.print()

res = bm25.query(queries)
for r in zip(queries, res):
    print(r)