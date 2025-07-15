import streamlit as st
import os
import anthropic
import random
import pandas as pd
import base64
import uuid
import datetime

# Set page configuration
st.set_page_config(
    page_title="Refine your Rhetoric • Just Rhett it",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS for Helvetica font
def load_css():
    with open(".streamlit/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the custom CSS
load_css()

# Load API key securely from Replit Secrets
API_KEY = os.getenv("CLAUDE_API_KEY")
if not API_KEY:
    st.error("API key not found. Add it to Replit Secrets.")
    st.stop()

# Initialize Claude API client
client = anthropic.Anthropic(api_key=API_KEY)

# Define presets with different balances of ethos, pathos, and logos
presets = {
    "MLK Dream": {
        "text": """Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity.

But 100 years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later the Negro is still languished in the corners of American society and finds himself in exile in his own land. And so we've come here today to dramatize a shameful condition. In a sense we've come to our nation's capital to cash a check.

When the architects of our republic wrote the magnificent words of the Constitution and the Declaration of Independence, they were signing a promissory note to which every American was to fall heir. This note was a promise that all men — yes, Black men as well as white men — would be guaranteed the unalienable rights of life, liberty and the pursuit of happiness.

It is obvious today that America has defaulted on this promissory note insofar as her citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad check, a check which has come back marked insufficient funds. But we refuse to believe that the bank of justice is bankrupt.

We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation. And so we've come to cash this check, a check that will give us upon demand the riches of freedom and the security of justice.

We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism.

Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God's children.

It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro's legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. 1963 is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual.

There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges.

But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place, we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred.

We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again, we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny.

And they have come to realize that their freedom is inextricably bound to our freedom. We cannot walk alone. And as we walk, we must make the pledge that we shall always march ahead. We cannot turn back.

There are those who are asking the devotees of civil rights, when will you be satisfied? We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities.

We cannot be satisfied as long as the Negro's basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating: for whites only.

We cannot be satisfied as long as a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote.

No, no, we are not satisfied, and we will not be satisfied until justice rolls down like waters, and righteousness like a mighty stream.

I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our Northern cities, knowing that somehow this situation can and will be changed.

Let us not wallow in the valley of despair, I say to you today, my friends.

So even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream. 

I have a dream that one day this nation will rise up and live out the true meaning of its creed: We hold these truths to be self-evident, that all men are created equal.

I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.

I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression will be transformed into an oasis of freedom and justice.

I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today.

I have a dream that one day down in Alabama with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification, one day right down in Alabama little Black boys and Black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today.

I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together.

This is our hope. This is the faith that I go back to the South with. With this faith, we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day.

This will be the day when all of God's children will be able to sing with new meaning: My country, 'tis of thee, sweet land of liberty, of thee I sing. Land where my fathers died, land of the pilgrims' pride, from every mountainside, let freedom ring.

And if America is to be a great nation, this must become true. And so let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania. Let freedom ring from the snowcapped Rockies of Colorado. Let freedom ring from the curvaceous slopes of California. But not only that, let freedom ring from Stone Mountain of Georgia. Let freedom ring from Lookout Mountain of Tennessee. Let freedom ring from every hill and molehill of Mississippi. From every mountainside, let freedom ring.

And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, Black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual: Free at last. Free at last. Thank God almighty, we are free at last.""",
        "balance": "Ethos: 30% Pathos: 45% Logos: 25%"
    },
    "Steve Jobs Stanford": {
        "text": """Today I want to tell you three stories from my life. That’s it. No big deal. Just three stories.

The first story is about connecting the dots.

I never graduated from college. Truth be told, this is the closest I’ve ever gotten to a college graduation. I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit. So why did I drop out?

It started before I was born. My biological mother was a young, unwed college graduate student, and she decided to put me up for adoption. She felt very strongly that I should be adopted by college graduates, so everything was all set for me to be adopted at birth by a lawyer and his wife. Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college.

And 17 years later I did go to college. But I naively chose a college that was almost as expensive as Stanford, and all of my working-class parents’ savings were being spent on my college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to do with my life and no idea how college was going to help me figure it out. And here I was spending all of the money my parents had saved their entire life. So I decided to drop out and trust that it would all work out OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.

It wasn’t all romantic. I didn’t have a dorm room, so I slept on the floor in friends’ rooms, I returned Coke bottles for the 5¢ deposits to buy food with, and I would walk the 7 miles across town every Sunday night to get one good meal a week at the Hare Krishna temple. I loved it. And much of what I stumbled into by following my curiosity and intuition turned out to be priceless later on. Let me give you one example:

Reed College at that time offered perhaps the best calligraphy instruction in the country. Throughout the campus every poster, every label on every drawer, was beautifully hand calligraphed. Because I had dropped out and didn’t have to take the normal classes, I decided to take a calligraphy class to learn how to do this. I learned about serif and sans serif typefaces, about varying the amount of space between different letter combinations, about what makes great typography great. It was beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.

None of this had even a hope of any practical application in my life. But 10 years later, when we were designing the first Macintosh computer, it all came back to me. And we designed it all into the Mac. It was the first computer with beautiful typography. If I had never dropped in on that single course in college, the Mac would have never had multiple typefaces or proportionally spaced fonts. And since Windows just copied the Mac, it’s likely that no personal computer would have them. If I had never dropped out, I would have never dropped in on this calligraphy class, and personal computers might not have the wonderful typography that they do. Of course it was impossible to connect the dots looking forward when I was in college. But it was very, very clear looking backward 10 years later.

Again, you can’t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect in your future. You have to trust in something – your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.

My second story is about love and loss.

I was lucky – I found what I loved to do early in life. Woz and I started Apple in my parents’ garage when I was 20. We worked hard, and in 10 years Apple had grown from just the two of us in a garage into a $2 billion company with over 4,000 employees. We had just released our finest creation – the Macintosh – a year earlier, and I had just turned 30. And then I got fired. How can you get fired from a company you started? Well, as Apple grew we hired someone who I thought was very talented to run the company with me, and for the first year or so things went well. But then our visions of the future began to diverge and eventually we had a falling out. When we did, our Board of Directors sided with him. So at 30 I was out. And very publicly out. What had been the focus of my entire adult life was gone, and it was devastating.

I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down – that I had dropped the baton as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and I even thought about running away from the valley. But something slowly began to dawn on me – I still loved what I did. The turn of events at Apple had not changed that one bit. I had been rejected, but I was still in love. And so I decided to start over.

I didn’t see it then, but it turned out that getting fired from Apple was the best thing that could have ever happened to me. The heaviness of being successful was replaced by the lightness of being a beginner again, less sure about everything. It freed me to enter one of the most creative periods of my life.

During the next five years, I started a company named NeXT, another company named Pixar, and fell in love with an amazing woman who would become my wife. Pixar went on to create the world’s first computer animated feature film, Toy Story, and is now the most successful animation studio in the world. In a remarkable turn of events, Apple bought NeXT, I returned to Apple, and the technology we developed at NeXT is at the heart of Apple’s current renaissance. And Laurene and I have a wonderful family together.

I’m pretty sure none of this would have happened if I hadn’t been fired from Apple. It was awful tasting medicine, but I guess the patient needed it. Sometimes life hits you in the head with a brick. Don’t lose faith. I’m convinced that the only thing that kept me going was that I loved what I did. You’ve got to find what you love. And that is as true for your work as it is for your lovers. Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it. And, like any great relationship, it just gets better and better as the years roll on. So keep looking until you find it. Don’t settle.

My third story is about death.

When I was 17, I read a quote that went something like: “If you live each day as if it was your last, someday you’ll most certainly be right.” It made an impression on me, and since then, for the past 33 years, I have looked in the mirror every morning and asked myself: “If today were the last day of my life, would I want to do what I am about to do today?” And whenever the answer has been “No” for too many days in a row, I know I need to change something.

Remembering that I’ll be dead soon is the most important tool I’ve ever encountered to help me make the big choices in life. Because almost everything – all external expectations, all pride, all fear of embarrassment or failure – these things just fall away in the face of death, leaving only what is truly important. Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are already naked. There is no reason not to follow your heart.

About a year ago I was diagnosed with cancer. I had a scan at 7:30 in the morning, and it clearly showed a tumor on my pancreas. I didn’t even know what a pancreas was. The doctors told me this was almost certainly a type of cancer that is incurable, and that I should expect to live no longer than three to six months. My doctor advised me to go home and get my affairs in order, which is doctor’s code for prepare to die. It means to try to tell your kids everything you thought you’d have the next 10 years to tell them in just a few months. It means to make sure everything is buttoned up so that it will be as easy as possible for your family. It means to say your goodbyes.

I lived with that diagnosis all day. Later that evening I had a biopsy, where they stuck an endoscope down my throat, through my stomach and into my intestines, put a needle into my pancreas and got a few cells from the tumor. I was sedated, but my wife, who was there, told me that when they viewed the cells under a microscope the doctors started crying because it turned out to be a very rare form of pancreatic cancer that is curable with surgery. I had the surgery and I’m fine now.

This was the closest I’ve been to facing death, and I hope it’s the closest I get for a few more decades. Having lived through it, I can now say this to you with a bit more certainty than when death was a useful but purely intellectual concept:

No one wants to die. Even people who want to go to heaven don’t want to die to get there. And yet death is the destination we all share. No one has ever escaped it. And that is as it should be, because Death is very likely the single best invention of Life. It is Life’s change agent. It clears out the old to make way for the new. Right now the new is you, but someday not too long from now, you will gradually become the old and be cleared away. Sorry to be so dramatic, but it is quite true.

Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking. Don’t let the noise of others’ opinions drown out your own inner voice. And most important, have the courage to follow your heart and intuition. They somehow already know what you truly want to become. Everything else is secondary.

When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop publishing, so it was all made with typewriters, scissors, and Polaroid cameras. It was sort of like Google in paperback form, 35 years before Google came along: It was idealistic, and overflowing with neat tools and great notions.

Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you.

Stay Hungry. Stay Foolish.""",
        "balance": "Ethos: 35% Pathos: 45% Logos: 20%"
    },
    "Greta's Wake-up Call": {
        "text": """This is all wrong. I shouldn't be up here. I should be back in school on the other side of the ocean. Yet you all come to us young people for hope. How dare you!

You have stolen my dreams and my childhood with your empty words. And yet I'm one of the lucky ones. People are suffering. People are dying. Entire ecosystems are collapsing. We are in the beginning of a mass extinction, and all you can talk about is money and fairy tales of eternal economic growth. How dare you!

For more than 30 years, the science has been crystal clear. How dare you continue to look away and come here saying that you're doing enough, when the politics and solutions needed are still nowhere in sight.

You say you hear us and that you understand the urgency. But no matter how sad and angry I am, I do not want to believe that. Because if you really understood the situation and still kept on failing to act, then you would be evil. And that I refuse to believe.

The popular idea of cutting our emissions in half in 10 years only gives us a 50% chance of staying below 1.5 degrees [Celsius], and the risk of setting off irreversible chain reactions beyond human control.

Fifty percent may be acceptable to you. But those numbers do not include tipping points, most feedback loops, additional warming hidden by toxic air pollution or the aspects of equity and climate justice. They also rely on my generation sucking hundreds of billions of tons of your CO2 out of the air with technologies that barely exist.

So a 50% risk is simply not acceptable to us — we who have to live with the consequences.

To have a 67% chance of staying below a 1.5 degrees global temperature rise – the best odds given by the [Intergovernmental Panel on Climate Change] – the world had 420 gigatons of CO2 left to emit back on Jan. 1st, 2018. Today that figure is already down to less than 350 gigatons.

How dare you pretend that this can be solved with just 'business as usual' and some technical solutions? With today's emissions levels, that remaining CO2 budget will be entirely gone within less than 8 1/2 years.

There will not be any solutions or plans presented in line with these figures here today, because these numbers are too uncomfortable. And you are still not mature enough to tell it like it is.

You are failing us. But the young people are starting to understand your betrayal. The eyes of all future generations are upon you. And if you choose to fail us, I say: We will never forgive you.

We will not let you get away with this. Right here, right now is where we draw the line. The world is waking up. And change is coming, whether you like it or not.""",
        "balance": "Ethos: 15% Pathos: 60% Logos: 25%"
    },
    "Warren Buffett's Letter to Shareholders": {
        "text": """To the Shareholders of Berkshire Hathaway Inc.: 

Berkshire earned $42.5 billion in 2020 according to generally accepted accounting principles (commonly called “GAAP”). The four components of that figure are $21.9 billion of operating earnings, $4.9 billion of realized capital gains, a $26.7 billion gain from an increase in the amount of net unrealized capital gains that exist in the stocks we hold and, finally, an $11 billion loss from a write-down in the value of a few subsidiary and affiliate businesses that we own. All items are stated on an after-tax basis. 

Operating earnings are what count most, even during periods when they are not the largest item in our GAAP total. Our focus at Berkshire is both to increase this segment of our income and to acquire large and favorably-situated businesses. Last year, however, we met neither goal: Berkshire made no sizable acquisitions and operating earnings fell 9%. We did, though, increase Berkshire’s per-share intrinsic value by both retaining earnings and repurchasing about 5% of our shares. 

The two GAAP components pertaining to capital gains or losses (whether realized or unrealized) fluctuate capriciously from year to year, reflecting swings in the stock market. Whatever today’s figures, Charlie Munger, my long-time partner, and I firmly believe that, over time, Berkshire’s capital gains from its investment holdings will be substantial. As I’ve emphasized many times, Charlie and I view Berkshire’s holdings of marketable stocks – at yearend worth $281 billion – as a collection of businesses. We don’t control the operations of those companies, but we do share proportionately in their long-term prosperity. From an accounting standpoint, however, our portion of their earnings is not included in Berkshire’s income. Instead, only what these investees pay us in dividends is recorded on our books. Under GAAP, the huge sums that investees retain on our behalf become invisible. What’s out of sight, however, should not be out of mind: Those unrecorded retained earnings are usually building value – lots of value – for Berkshire. Investees use the withheld funds to expand their business, make acquisitions, pay off debt and, often, to repurchase their stock (an act that increases our share of their future earnings). As we pointed out in these pages last year, retained earnings have propelled American business throughout our country’s history. What worked for Carnegie and Rockefeller has, over the years, worked its magic for millions of shareholders as well. Of course, some of our investees will disappoint, adding little, if anything, to the value of their company by retaining earnings. But others will over-deliver, a few spectacularly. In aggregate, we expect our share of the huge pile of earnings retained by Berkshire’s non-controlled businesses (what others would label our equity portfolio) to eventually deliver us an equal or greater amount of capital gains. Over our 56-year tenure, that expectation has been met.

The final component in our GAAP figure – that ugly $11 billion write-down – is almost entirely the quantification of a mistake I made in 2016. That year, Berkshire purchased Precision Castparts (“PCC”), and I paid too much for the company. No one misled me in any way – I was simply too optimistic about PCC’s normalized profit potential. Last year, my miscalculation was laid bare by adverse developments throughout the aerospace industry, PCC’s most important source of customers. In purchasing PCC, Berkshire bought a fine company – the best in its business. Mark Donegan, PCC’s CEO, is a passionate manager who consistently pours the same energy into the business that he did before we purchased it. We are lucky to have him running things. I believe I was right in concluding that PCC would, over time, earn good returns on the net tangible assets deployed in its operations. I was wrong, however, in judging the average amount of future earnings and, consequently, wrong in my calculation of the proper price to pay for the business. PCC is far from my first error of that sort. But it’s a big one. Two Strings to Our Bow Berkshire is often labeled a conglomerate, a negative term applied to holding companies that own a hodge-podge of unrelated businesses. And, yes, that describes Berkshire – but only in part. To understand how and why we differ from the prototype conglomerate, let’s review a little history. Over time, conglomerates have generally limited themselves to buying businesses in their entirety. That strategy, however, came with two major problems. One was unsolvable: Most of the truly great businesses had no interest in having anyone take them over. Consequently, deal-hungry conglomerateurs had to focus on so-so companies that lacked important and durable competitive strengths. That was not a great pond in which to fish. Beyond that, as conglomerateurs dipped into this universe of mediocre businesses, they often found themselves required to pay staggering “control” premiums to snare their quarry. Aspiring conglomerateurs knew the answer to this “overpayment” problem: They simply needed to manufacture a vastly overvalued stock of their own that could be used as a “currency” for pricey acquisitions. (“I’ll pay you $10,000 for your dog by giving you two of my $5,000 cats.”) Often, the tools for fostering the overvaluation of a conglomerate’s stock involved promotional techniques and “imaginative” accounting maneuvers that were, at best, deceptive and that sometimes crossed the line into fraud. When these tricks were “successful,” the conglomerate pushed its own stock to, say, 3x its business value in order to offer the target 2x its value. Investing illusions can continue for a surprisingly long time. Wall Street loves the fees that deal-making generates, and the press loves the stories that colorful promoters provide. At a point, also, the soaring price of a promoted stock can itself become the “proof” that an illusion is reality.

Eventually, of course, the party ends, and many business “emperors” are found to have no clothes. Financial history is replete with the names of famous conglomerateurs who were initially lionized as business geniuses by journalists, analysts and investment bankers, but whose creations ended up as business junkyards. Conglomerates earned their terrible reputation. ************ Charlie and I want our conglomerate to own all or part of a diverse group of businesses with good economic characteristics and good managers. Whether Berkshire controls these businesses, however, is unimportant to us. It took me a while to wise up. But Charlie – and also my 20-year struggle with the textile operation I inherited at Berkshire – finally convinced me that owning a non-controlling portion of a wonderful business is more profitable, more enjoyable and far less work than struggling with 100% of a marginal enterprise. For those reasons, our conglomerate will remain a collection of controlled and non-controlled businesses. Charlie and I will simply deploy your capital into whatever we believe makes the most sense, based on a company’s durable competitive strengths, the capabilities and character of its management, and price. If that strategy requires little or no effort on our part, so much the better. In contrast to the scoring system utilized in diving competitions, you are awarded no points in business endeavors for “degree of difficulty.” Furthermore, as Ronald Reagan cautioned: “It’s said that hard work never killed anyone, but I say why take the chance?” The Family Jewels and How We Increase Your Share of These Gems On page A-1 we list Berkshire’s subsidiaries, a smorgasbord of businesses employing 360,000 at yearend. You can read much more about these controlled operations in the 10-K that fills the back part of this report. Our major positions in companies that we partly own and don’t control are listed on page 7 of this letter. That portfolio of businesses, too, is large and diverse. Most of Berkshire’s value, however, resides in four businesses, three controlled and one in which we have only a 5.4% interest. All four are jewels. The largest in value is our property/casualty insurance operation, which for 53 years has been the core of Berkshire. Our family of insurers is unique in the insurance field. So, too, is its manager, Ajit Jain, who joined Berkshire in 1986. Overall, the insurance fleet operates with far more capital than is deployed by any of its competitors worldwide. That financial strength, coupled with the huge flow of cash Berkshire annually receives from its non-insurance businesses, allows our insurance companies to safely follow an equity-heavy investment strategy not feasible for the overwhelming majority of insurers. Those competitors, for both regulatory and credit-rating reasons, must focus on bonds. And bonds are not the place to be these days. Can you believe that the income recently available from a 10-year U.S. Treasury bond – the yield was 0.93% at yearend – had fallen 94% from the 15.8% yield available in September 1981? In certain large and important countries, such as Germany and Japan, investors earn a negative return on trillions of dollars of sovereign debt. Fixed-income investors worldwide – whether pension funds, insurance companies or retirees – face a bleak future.

Some insurers, as well as other bond investors, may try to juice the pathetic returns now available by shifting their purchases to obligations backed by shaky borrowers. Risky loans, however, are not the answer to inadequate interest rates. Three decades ago, the once-mighty savings and loan industry destroyed itself, partly by ignoring that maxim. Berkshire now enjoys $138 billion of insurance “float” – funds that do not belong to us, but are nevertheless ours to deploy, whether in bonds, stocks or cash equivalents such as U.S. Treasury bills. Float has some similarities to bank deposits: cash flows in and out daily to insurers, with the total they hold changing very little. The massive sum held by Berkshire is likely to remain near its present level for many years and, on a cumulative basis, has been costless to us. That happy result, of course, could change – but, over time, I like our odds. I have repetitiously – some might say endlessly – explained our insurance operation in my annual letters to you. Therefore, I will this year ask new shareholders who wish to learn more about our insurance business and “float” to read the pertinent section of the 2019 report, reprinted on page A-2. It’s important that you understand the risks, as well as the opportunities, existing in our insurance activities. Our second and third most valuable assets – it’s pretty much a toss-up at this point – are Berkshire’s 100% ownership of BNSF, America’s largest railroad measured by freight volume, and our 5.4% ownership of Apple. And in the fourth spot is our 91% ownership of Berkshire Hathaway Energy (“BHE”). What we have here is a very unusual utility business, whose annual earnings have grown from $122 million to $3.4 billion during our 21 years of ownership. I’ll have more to say about BNSF and BHE later in this letter. For now, however, I would like to focus on a practice Berkshire will periodically use to enhance your interest in both its “Big Four” as well as the many other assets Berkshire owns. ************ Last year we demonstrated our enthusiasm for Berkshire’s spread of properties by repurchasing the equivalent of 80,998 “A” shares, spending $24.7 billion in the process. That action increased your ownership in all of Berkshire’s businesses by 5.2% without requiring you to so much as touch your wallet. Following criteria Charlie and I have long recommended, we made those purchases because we believed they would both enhance the intrinsic value per share for continuing shareholders and would leave Berkshire with more than ample funds for any opportunities or problems it might encounter. In no way do we think that Berkshire shares should be repurchased at simply any price. I emphasize that point because American CEOs have an embarrassing record of devoting more company funds to repurchases when prices have risen than when they have tanked. Our approach is exactly the reverse. Berkshire’s investment in Apple vividly illustrates the powerof repurchases. We began buying Apple stock late in 2016 and by early July 2018, owned slightly more than one billion Apple shares (split-adjusted). Saying that, I’m referencing the investment held in Berkshire’s general account and am excluding a very small and separately-managed holding of Apple shares that was subsequently sold. When we finished our purchases in mid-2018, Berkshire’s general account owned 5.2% of Apple. Our cost for that stake was $36 billion. Since then, we have both enjoyed regular dividends, averaging about $775 million annually, and have also – in 2020 – pocketed an additional $11 billion by selling a small portion of our position. Despite that sale – voila! – Berkshire now owns 5.4% of Apple. That increase was costless to us, coming about because Apple has continuously repurchased its shares, thereby substantially shrinking the number it now has outstanding.

But that’s far from all of the good news. Because we also repurchased Berkshire shares during the 21⁄2 years, you now indirectly own a full 10% more of Apple’s assets and future earnings than you did in July 2018. This agreeable dynamic continues. Berkshire has repurchased more shares since yearend and is likely to further reduce its share count in the future. Apple has publicly stated an intention to repurchase its shares as well. As these reductions occur, Berkshire shareholders will not only own a greater interest in our insurance group and in BNSF and BHE, but will also find their indirect ownership of Apple increasing as well. The math of repurchases grinds away slowly, but can be powerful over time. The process offers a simple way for investors to own an ever-expanding portion of exceptional businesses. And as a sultry Mae West assured us: “Too much of a good thing can be . . . wonderful.” """,
        "balance": "Ethos: 35% Pathos: 15% Logos: 50%"
    },
    "Tech Investment": {
        "text": """Based on our comprehensive market analysis, investing in quantum computing technology represents an exceptional opportunity with significant potential for above-market returns over the next decade.

The quantum computing market is projected to grow from $412 million in 2020 to $8.6 billion by 2027, representing a compound annual growth rate (CAGR) of 50.9%. This growth is driven by several factors:

1. Increasing investments from major technology companies including IBM, Google, Microsoft, and Amazon, who collectively committed over $4 billion to quantum research in 2023 alone.

2. Expanding commercial applications across multiple high-value sectors:
   - Pharmaceutical companies can reduce drug discovery timelines from 10+ years to potentially 3-5 years
   - Financial institutions can optimize portfolios and risk models with unprecedented precision
   - Manufacturing firms can solve complex logistics and material science challenges

3. Government initiatives worldwide, with the U.S. National Quantum Initiative providing $1.2 billion in funding, China investing an estimated $10 billion, and the EU allocating €1 billion through the Quantum Flagship program.""",
        "balance": "Ethos: 15% Pathos: 10% Logos: 75%"
    }
}
# Add a blank preset
presets[" "] = {
    "text": "",
    "balance": "No analysis yet"
}

# Initialize session state for current preset and leaderboard
if 'current_preset' not in st.session_state:
    st.session_state.current_preset = " "

# Initialize leaderboard in session state if it doesn't exist
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = []

# Initialize user's submission ID
if 'submission_id' not in st.session_state:
    st.session_state.submission_id = None

# Initialize persuasion score
if 'persuasion_score' not in st.session_state:
    st.session_state.persuasion_score = None

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Just Rhett it.</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.9rem; font-weight: normal; text-transform: uppercase; letter-spacing: 0.2em;'>Refine Your Rhetoric</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: serif;'><i>\"The fool tells me his reasons; the wise man persuades me with my own.\"</i><br>— Aristotle</p>", unsafe_allow_html=True)

# Custom CSS for the persuasion score gauge
st.markdown("""
<style>
.persuasion-gauge {
    margin: 20px auto;
    max-width: 500px;
    text-align: center;
}
.gauge-background {
    width: 100%;
    height: 20px;
    background-color: #f0f0f0;
    border-radius: 10px;
    position: relative;
    overflow: hidden;
}
.gauge-fill {
    height: 100%;
    background: linear-gradient(90deg, #ffcc00, #00cc66);
    border-radius: 10px 0 0 10px;
    transition: width 0.5s ease-in-out;
}
.gauge-marker {
    margin-top: 5px;
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: #666;
}
.gauge-value {
    font-size: 24px;
    font-weight: bold;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Create two columns for the Inspire Me button and preset info
col1, col2 = st.columns([1, 3])

with col1:
    # Inspire Me button to rotate through presets
    if st.button("✨ Inspire Me"):
        # Get list of presets excluding current one
        available_presets = [p for p in presets.keys() if p != st.session_state.current_preset]
        # Randomly select a new preset
        st.session_state.current_preset = random.choice(available_presets)

# Get the current preset text
preset_text = ""
if st.session_state.current_preset in presets:
    preset_text = presets[st.session_state.current_preset]['text']

# User input box - will show preset text if "Inspire Me" was clicked
user_text = st.text_area("Now, make your case:", value=preset_text)

if st.button("Judge"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            prompt = f"""
            Analyze the following text and classify its persuasive strategy using Ethos (credibility), Pathos (emotion), and Logos (logic).
            Provide a percentage breakdown of each category, calculate an overall persuasion score, and suggest specific improvements.

            Text: "{user_text}"

            IMPORTANT: In your suggestions, extract ACTUAL PHRASES from the user's text and show specific word-by-word revisions to improve persuasiveness. Do not use placeholder text.

            For the persuasion score (0-100%), consider these factors:
            1. Balance of rhetorical appeals (ethos, pathos, logos) appropriate to the subject matter
            2. Clarity and coherence of argument
            3. Effective use of language (specificity, vividness, appropriateness)
            4. Audience awareness and adaptation
            5. Presence of concrete evidence or examples

            Use this exact format for your response:
            # Persuasive Strategy Analysis

            Ethos: X%
            Pathos: Y%
            Logos: Z%

            **Persuasion Score: [0-100]%**

            ## Summary
            Provide a 2-3 sentence overall summary of the text's persuasive approach. Include 1-2 direct quotes from the original text that best represent its persuasive elements. Briefly explain the reasoning behind the persuasion score, referencing the five factors listed above.

            ## Detailed Analysis
            Ethos: Brief explanation of ethos elements (1-2 sentences)

            Pathos: Brief explanation of pathos elements (1-2 sentences)

            Logos: Brief explanation of logos elements (1-2 sentences)

            ## Suggestions:
            Consider how you might enhance your persuasiveness. For instance, when you write "[extract a specific phrase from their input]", you could revise it to "[provide a specific word-by-word revision]" to strengthen your [ethos/pathos/logos] appeal.

            Another approach would be to [provide a second naturalistic suggestion based on their persuasive strategy].
            """

            response = client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )

            try:
                # Extract response text
                result = response.content[0].text

                # Display the result
                st.subheader("Analysis Result")

                # Try to extract persuasion score if available
                try:
                    import re
                    score_match = re.search(r'Persuasion Score: \[?(\d+)\]?%', result)
                    if score_match:
                        persuasion_score = int(score_match.group(1))
                        st.session_state.persuasion_score = persuasion_score

                        # Display persuasion score gauge
                        st.markdown(f"""
                        <div class="persuasion-gauge">
                            <div class="gauge-value">Persuasion Score: {persuasion_score}%</div>
                            <div class="gauge-background">
                                <div class="gauge-fill" style="width: {persuasion_score}%;"></div>
                            </div>
                            <div class="gauge-marker">
                                <span>0%</span>
                                <span>25%</span>
                                <span>50%</span>
                                <span>75%</span>
                                <span>100%</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                except:
                    # If score extraction fails, just continue
                    pass

                # Display the full analysis
                st.write(result)

               

                # Create simplified sharing section
                st.subheader("Share via:")
                
                # Define the app URL and sharing content
                app_url = "https://rhettit.app"
                share_text = f"I scored {st.session_state.persuasion_score}% on Rhett's rhetoric analysis! #rhetoric #persuasion"
                
                # Create a row of sharing buttons
                col1, col2, col3, col4 = st.columns(4)
                
                # Import urllib.parse once at the top
                import urllib.parse
                
                # Ensure the share text is properly formed with platform-specific tags
                twitter_share_text = f"AI says I'm {st.session_state.persuasion_score}% persuasive. Debate me. 🏛️ See your score: rhettit.app Made by @meanarchitects 🖤"
                bluesky_share_text = f"AI says I'm {st.session_state.persuasion_score}% persuasive. Debate me. 🏛️ See your score: rhettit.app Made by @kairosconcepts.substack.com 🖤"
                mastodon_share_text = f"AI says I'm {st.session_state.persuasion_score}% persuasive. Debate me. 🏛️ See your score: rhettit.app Made by @architectsofmeaning 🖤"
                
                
                # X/Twitter sharing
                with col1:
                    twitter_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(twitter_share_text)}"
                    st.markdown(f"""
                    <a href='{twitter_url}' target='_blank' rel="noopener noreferrer">
                        <button style="background-color:#1DA1F2; color:white; padding:10px; width:100%;
                                      border:none; border-radius:5px; font-weight:bold; cursor:pointer; 
                                      display:flex; align-items:center; justify-content:center;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" style="margin-right:5px;" viewBox="0 0 16 16">
                                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                            </svg>
                            X / Twitter
                        </button>
                    </a>
                    """, unsafe_allow_html=True)
                
                # Bluesky sharing
                with col2:
                    # Bluesky - opening a new page with pre-filled content
                    bluesky_url = f"https://bsky.app/intent/compose?text={urllib.parse.quote(bluesky_share_text)}"
                    st.markdown(f"""
                    <a href='{bluesky_url}' target='_blank' rel="noopener noreferrer">
                        <button style="background-color:#0085FF; color:white; padding:10px; width:100%;
                                      border:none; border-radius:5px; font-weight:bold; cursor:pointer; 
                                      display:flex; align-items:center; justify-content:center;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" style="margin-right:5px;" viewBox="0 0 100 100">
                                <path d="M50,16.2c-18.6,0-33.8,15.1-33.8,33.8c0,18.6,15.1,33.8,33.8,33.8c18.6,0,33.8-15.1,33.8-33.8 C83.8,31.3,68.6,16.2,50,16.2z M50,77.3c-15.1,0-27.3-12.2-27.3-27.3c0-15.1,12.2-27.3,27.3-27.3c15.1,0,27.3,12.2,27.3,27.3 C77.3,65.1,65.1,77.3,50,77.3z"/>
                                <circle cx="73" cy="27" r="5"/>
                            </svg>
                            Bluesky
                        </button>
                    </a>
                    """, unsafe_allow_html=True)
                
                # Mastodon sharing
                with col3:
                    # Mastodon - Web+Toot scheme URI
                    mastodon_url = f"https://mastodon.social/share?text={urllib.parse.quote(mastodon_share_text)}"
                    st.markdown(f"""
                    <a href='{mastodon_url}' target='_blank' rel="noopener noreferrer">
                        <button style="background-color:#6364FF; color:white; padding:10px; width:100%;
                                      border:none; border-radius:5px; font-weight:bold; cursor:pointer; 
                                      display:flex; align-items:center; justify-content:center;">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" style="margin-right:5px;" viewBox="0 0 16 16">
                                <path d="M11.19 12.195c2.016-.24 3.77-1.475 3.99-2.603.348-1.778.32-4.339.32-4.339 0-3.47-2.286-4.488-2.286-4.488C12.062.238 10.083.017 8.027 0h-.05C5.92.017 3.942.238 2.79.765c0 0-2.285 1.017-2.285 4.488l-.002.662c-.004.64-.007 1.35.011 2.091.083 3.394.626 6.74 3.78 7.57 1.454.383 2.703.463 3.709.408 1.823-.1 2.847-.647 2.847-.647l-.06-1.317s-1.303.41-2.767.36c-1.45-.05-2.98-.156-3.215-1.928a3.614 3.614 0 0 1-.033-.496s1.424.346 3.228.428c1.103.05 2.137-.064 3.188-.189zm1.613-2.47H11.13v-4.08c0-.859-.364-1.295-1.091-1.295-.804 0-1.207.517-1.207 1.541v2.233H7.168V5.89c0-1.024-.403-1.541-1.207-1.541-.727 0-1.091.436-1.091 1.296v4.079H3.197V5.522c0-.859.22-1.541.66-2.046.456-.505 1.052-.764 1.793-.764.856 0 1.504.328 1.933.983L8 4.39l.417-.695c.429-.655 1.077-.983 1.934-.983.74 0 1.336.259 1.791.764.442.505.661 1.187.661 2.046v4.203z"/>
                            </svg>
                            Mastodon
                        </button>
                    </a>
                    """, unsafe_allow_html=True)
                
              
                    
                # Add a Remix on Replit button
                with col4:
                    remix_url = "https://replit.com/github/KairosConcepts/rhett-app.git"
                    st.markdown(f"""
                    <a href='{remix_url}' target='_blank' rel="noopener noreferrer">
                        <button style="background-color:#F26207; color:white; padding:10px; width:100%;
                                      border:none; border-radius:5px; font-weight:bold; cursor:pointer; 
                                      display:flex; align-items:center; justify-content:center;">
                            <svg width="16" height="16" viewBox="0 0 32 32" fill="currentColor" style="margin-right:5px;">
                                <path d="M7.1 9.4c.2.2.5.2.7 0l2.8-2.8v23.9c0 .3.2.5.5.5h3.4c.3 0 .5-.2.5-.5V6.6l2.8 2.8c.2.2.5.2.7 0l2.4-2.4c.2-.2.2-.5 0-.7L12.1.1a.5.5 0 0 0-.7 0l-6.7, 6.2c-.2.2-.2.5 0 .7l2.4 2.4z"></path>
                            </svg>
                            Remix on Replit
                        </button>
                    </a>
                    """, unsafe_allow_html=True)

                # Add JavaScript to help ensure links open properly
                st.markdown("""
                <script>
                document.querySelectorAll('a[target="_blank"]').forEach(link => {
                    link.addEventListener('click', function(e) {
                        e.preventDefault();
                        window.open(this.getAttribute('href'), '_blank');
                    });
                });
                </script>
                """, unsafe_allow_html=True)


            except Exception as e:
                st.error(f"Error processing response: {str(e)}")
                st.info("Try checking your API key or using a different Claude model.")

# Add a dropdown to manually select presets
st.sidebar.header("The Art of Persuasion")
selected_preset = st.sidebar.selectbox(
    "Choose a persuasive style:",
    options=list(presets.keys()),
    index=list(presets.keys()).index(st.session_state.current_preset)
)

# Update the current preset if changed via dropdown
if selected_preset != st.session_state.current_preset:
    st.session_state.current_preset = selected_preset
    # Trigger a rerun to update the text area with the new preset
    st.rerun()

# Information about rhetorical appeals
st.sidebar.markdown("---")
st.sidebar.header("Understanding Rhetorical Appeals")
st.sidebar.markdown("""
**Ethos** - Appeal to credibility or character
- Establishes speaker's authority and trustworthiness
- Uses credentials, expertise, and shared values

**Pathos** - Appeal to emotion
- Connects with audience's feelings and values
- Uses vivid imagery, personal stories, and emotive language

**Logos** - Appeal to logic and reason
- Presents facts, statistics, and logical arguments
- Demonstrates cause-effect relationships and analytical thinking
""")