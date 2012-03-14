# -*- coding: cp1252 -*-

"""
A naive summarization approach based on Luhn1958 work
"The Automatic Creation of Literature Abstracts"
It uses the frequencies of words in the document in order to 
calculate and extract the sentences that include the most frequent words.

"""

# Copyright (C) 2012 Alejandro Mosquera <amsqr2@gmail.com>
 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist 
from nltk.corpus import stopwords


class NaiveSummarizer:

	
	def summarize(self, input, num_sentences ):

		punt_list=['.',',','!','?']
		summ_sentences = []

	        sentences = sent_tokenize(input)
		lowercase_sentences =[sentence.lower() 
			for sentence in sentences]
		#print lowercase_sentences
		
		s=list(input)
		ts=''.join([ o for o in s if not o in  punt_list ]).split()
		lowercase_words=[word.lower() for word in ts]
		words = [word for word in lowercase_words if word not in stopwords.words()]
		word_frequencies = FreqDist(words)
		
		most_frequent_words = [pair[0] for pair in 
			word_frequencies.items()[:100]]

                # add sentences with the most frequent words
		for word in most_frequent_words:
			for i in range(0, len(lowercase_sentences)):
                                if len(summ_sentences) < num_sentences:
                                        if (lowercase_sentences[i] not in summ_sentences and word in lowercase_sentences[i]):
                                                summ_sentences.append(sentences[i])
                                                break
                                        
			
		# reorder the selected sentences
		summ_sentences.sort( lambda s1, s2: input.find(s1) - input.find(s2) )
		return " ".join(summ_sentences)


if __name__ == "__main__":

	naivesum = NaiveSummarizer()
	text='''
	To see a world in a grain of sand,
	And a heaven in a wild flower,
	Hold infinity in the palm of your hand,
	And eternity in an hour.

	A robin redbreast in a cage
	Puts all heaven in a rage.

	A dove-house fill'd with doves and pigeons
	Shudders hell thro' all its regions.
	A dog starv'd at his master's gate
	Predicts the ruin of the state.

	A horse misused upon the road
	Calls to heaven for human blood.
	Each outcry of the hunted hare
	A fibre from the brain does tear.

	A skylark wounded in the wing,
	A cherubim does cease to sing.
	The game-cock clipt and arm'd for fight
	Does the rising sun affright.

	Every wolf's and lion's howl
	Raises from hell a human soul.

	The wild deer, wand'ring here and there,
	Keeps the human soul from care.
	The lamb misus'd breeds public strife,
	And yet forgives the butcher's knife.

	The bat that flits at close of eve
	Has left the brain that won't believe.
	The owl that calls upon the night
	Speaks the unbeliever's fright.

	He who shall hurt the little wren
	Shall never be belov'd by men.
	He who the ox to wrath has mov'd
	Shall never be by woman lov'd.

	The wanton boy that kills the fly
	Shall feel the spider's enmity.
	He who torments the chafer's sprite
	Weaves a bower in endless night.

	The caterpillar on the leaf
	Repeats to thee thy mother's grief.
	Kill not the moth nor butterfly,
	For the last judgement draweth nigh.

	He who shall train the horse to war
	Shall never pass the polar bar.
	The beggar's dog and widow's cat,
	Feed them and thou wilt grow fat.

	The gnat that sings his summer's song
	Poison gets from slander's tongue.
	The poison of the snake and newt
	Is the sweat of envy's foot.

	The poison of the honey bee
	Is the artist's jealousy.

	The prince's robes and beggar's rags
	Are toadstools on the miser's bags.
	A truth that's told with bad intent
	Beats all the lies you can invent.

	It is right it should be so;
	Man was made for joy and woe;
	And when this we rightly know,
	Thro' the world we safely go.

	Joy and woe are woven fine,
	A clothing for the soul divine.
	Under every grief and pine
	Runs a joy with silken twine.

	The babe is more than swaddling bands;
	Every farmer understands.
	Every tear from every eye
	Becomes a babe in eternity;

	This is caught by females bright,
	And return'd to its own delight.
	The bleat, the bark, bellow, and roar,
	Are waves that beat on heaven's shore.

	The babe that weeps the rod beneath
	Writes revenge in realms of death.
	The beggar's rags, fluttering in air,
	Does to rags the heavens tear.

	The soldier, arm'd with sword and gun,
	Palsied strikes the summer's sun.
	The poor man's farthing is worth more
	Than all the gold on Afric's shore.

	One mite wrung from the lab'rer's hands
	Shall buy and sell the miser's lands;
	Or, if protected from on high,
	Does that whole nation sell and buy.

	He who mocks the infant's faith
	Shall be mock'd in age and death.
	He who shall teach the child to doubt
	The rotting grave shall ne'er get out.

	He who respects the infant's faith
	Triumphs over hell and death.
	The child's toys and the old man's reasons
	Are the fruits of the two seasons.

	The questioner, who sits so sly,
	Shall never know how to reply.
	He who replies to words of doubt
	Doth put the light of knowledge out.

	The strongest poison ever known
	Came from Caesar's laurel crown.
	Nought can deform the human race
	Like to the armour's iron brace.

	When gold and gems adorn the plow,
	To peaceful arts shall envy bow.
	A riddle, or the cricket's cry,
	Is to doubt a fit reply.

	The emmet's inch and eagle's mile
	Make lame philosophy to smile.
	He who doubts from what he sees
	Will ne'er believe, do what you please.

	If the sun and moon should doubt,
	They'd immediately go out.
	To be in a passion you good may do,
	But no good if a passion is in you.

	The whore and gambler, by the state
	Licensed, build that nation's fate.
	The harlot's cry from street to street
	Shall weave old England's winding-sheet.

	The winner's shout, the loser's curse,
	Dance before dead England's hearse.

	Every night and every morn
	Some to misery are born,
	Every morn and every night
	Some are born to sweet delight.

	Some are born to sweet delight,
	Some are born to endless night.

	We are led to believe a lie
	When we see not thro' the eye,
	Which was born in a night to perish in a night,
	When the soul slept in beams of light.

	God appears, and God is light,
	To those poor souls who dwell in night;
	But does a human form display
	To those who dwell in realms of day.
	'''
        text2 = '''
        IT IS kind of you, my esteemed friend, to condone my two years of silence and to write to me thus. It is
        more than kind of you to give to your solicitude about me, to your perplexity at what appears to you as mental stagnation, the expression of lightness and jest which only great men, convinced of the perilousness of life yet not dis­couraged by it, can master.
         You conclude with the aphorism of Hippocrates, "Qui gravi morbo correpti dolores non sentiunt, us mens aegro­tat" (Those who do not perceive that they are wasted by seri­ous illness are sick in mind), and suggest that I am in need of medicine not only to conquer my malady, but even more, to sharpen my senses for the condition of my inner self. I would fain give you an answer such as you deserve, fain reveal myself to you entirely, but I do not know how to set about it. Hardly do I know whether I am still the same person to whom your precious letter is addressed. Was it I who, now six-and-twenty, at nineteen wrote The New Paris, The Dream of Daphne, Epithalamium, those pastorals reeling under the splendour of their words-plays which a divine Queen and several over­indulgent lords and gentlemen are gracious enough still to remember? And again, was it I who, at three-and-twenty, be­neath the stone arcades of the great Venetian piazza, found in myself that structure of Latin prose whose plan and order delighted me more than did the monuments of Palladio and Sansovino rising out of the sea? And could I, if otherwise I am still the same person, have lost from my inner inscrutable self all traces and scars of this creation of my most intensive thinking-lost them so completely that in your letter now lying before me the title of my short treatise stares at me strange and cold? I could not even comprehend, at first, what the familiar picture meant, but had to study it word by word, as though these Latin terms thus strung together were meet­ing my eye for the first time. But I am, after all, that person, and there is rhetoric in these questions-rhetoric which is good for women or for the House of Commons, whose power, however, so overrated by our time, is not sufficient to pene­trate into the core of things. But it is my inner self that I feel bound to reveal to you-a peculiarity, a vice, a disease of my mind, if you like-if you are to understand that an abyss equally unbridgeable separates me from the literary works lying seemingly ahead of me as from those behind me: the latter having become so strange to me that I hesitate to call them my property.
        I know not whether to admire more the urgency of your benevolence or the unbelievable sharpness of your memory, when you recall to me the various little projects I entertained during those days of rare enthusiasm which we shared together. True, I did plan to describe the first years of the reign of our glorious sovereign, the late Henry VIII. The papers bequeathed to me by my grandfather, the Duke of Exeter, concerning his negotiations with France and Portugal, offered me some foundation. And out of Sallust, in those happy, stimulating days, there flowed into me as though through never~ongested conduits the realization of form-that deep, true, inner form which can be sensed only beyond the domain of rhetorical tricks: that form of which one can no longer say that it organizes subject-matter, for it pene­trates it, dissolves it, creating at once both dream and reality, an interplay of eternal forces, something as marvellous as music or algebra. This was my most treasured plan.
        But what is man that he should make plans!
        I also toyed with other schemes. These, too, your kind letter conjures up. Each one, bloated with a drop of my blood, dances before me like a weary gnat against a sombre wall whereon the bright sun of halcyon days no longer lies.
        I wanted to decipher the fables, the mythical tales be­queathed to us by the Ancients, in which painters and sculp­tors found an endless and thoughtless pleasure decipher them as the hieroglyphs of a secret, inexhaustible wisdom whose breath I sometimes seemed to feel as though from be­hind a veil. 
        I well remember this plan. It was founded on I know not what sensual and spiritual desire: as the hunted hart craves water, so I craved to enter these naked, glistening bodies, these sirens and dryads, this Narcissus and Proteus, Perseus and Actaeon. I longed to disappear in them and talk out of them with tongues. And I longed for more. I planned to start an Apophthegmata, like that composed by Julius Caesar:
        you will remember that Cicero mentions it in a letter. In it I thought of setting side by side the most memorable say­ings which-while associating with the learned men and witty women of our time, with unusual people from among the sim­ple folk or with erudite and distinguished personages I had managed to collect during my travels. With these I meant to combine the brilliant maxims and reflections from classical and Italian works, and anything else of intellectual adornment that appealed to me in books, in manuscripts or conversations; the arrangement, moreover, of particularly beautiful festivals and pageants, strange crimes and cases of madness, descriptions of the greatest and most characteristic architectural monuments in the Netherlands, in France and Italy; and many other things. The whole work was to have been entitled Nosce te ipsum. 
        To sum up: In those days I, in a state of continuous in­toxication, conceived the whole of existence as one great unit: the spiritual and physical worlds seemed to form no contrast, as little as did courtly and bestial conduct, art and barbarism, solitude and society; in everything I felt the pres­ence of Nature, in the aberrations of insanity as much as in the utmost refinement of the Spanish ceremonial; in the boorishness of young peasants no less than in the most deli­cate of allegories; and in all expressions of Nature I felt my-self. When in my hunting lodge I drank the warm foaming milk which an unkempt wench had drained into a wooden pail from the udder of a beautiful gentle~yed cow, the sen­sation was no different from that which I experienced when, seated on a bench built into the window of my study, my mind absorbed the sweet and foaming nourishment from a book. The one was like the other: neither was superior to the other, whether in dreamlike celestial quality or in physical in­tensity-and thus it prevailed through the whole expanse of life in all directions; everywhere I was in the centre of it, never suspecting mere appearance: at other times I divined that all was allegory and that each creature was a key to all the others; and I felt myself the one capable of seizing each by the handle and unlocking as many of the others as were ready to yield. This explains the title which I had intended to give to this encyclopedic book. 
        To a person susceptible to such ideas, it might appear a well-designed plan of divine Providence that my mind should fall from such a state of inflated arrogance into this extreme of despondency and feebleness which is now the permanent condition of my inner self. Such religious ideas, however, have no power over me: they belong to the cobwebs through which my thoughts dart out into the void, while the thoughts of so many others are caught there and come to rest. To me the mysteries of faith have been condensed into a lofty alle­gory which arches itself over the fields of my life like a radiant rainbow, ever remote, ever prepared to recede should it occur to me to rush toward it and wrap myself into the folds of its mantle. 
        But, my dear friend, worldly ideas also evade me in a like manner. How shall I try to describe to you these strange spiritual torments, this rebounding of the fruit-branches above my outstretched hands, this recession of the murmuring stream from my thirsting lips? 
        My case, in short, is this: I have lost completely the abil­ity to think or to speak of anything coherently. 
        At first I grew by degrees incapable of discussing a loftier or more general subject in terms of which everyone, fluently and without hesitation, is wont to avail himself. I experienced an inexplicable distaste for so much as uttering the words spirit, soul, or body. I found it impossible to express an opinion on the affairs at Court, the events in Parliament, or whatever you wish. This was not motivated by any form of personal deference (for you know that my candour borders on imprudence), but because the abstract terms of which the tongue must avail itself as a matter of course in order to voice a judgment-these terms crumbled in my mouth like mouldy fungi. Thus, one day, while reprimanding my four-year-old daughter, Katherina Pompilia, for a childish lie of which she had been guilty and demonstrating to her the necessity of always being truthful, the ideas streaming into my mind sud­denly took on such iridescent colouring, so flowed over into one another, that I reeled off the sentence as best I could, as if suddenly overcome by illness. Actually, I did feel myself growing pale, and with a violent pressure on my forehead I left the child to herself, slammed the door behind me, and began to recover to some extent only after a brief gallop over the lonely pasture. 
        Gradually, however, these attacks of anguish spread like a corroding rust. Even in familiar and humdrum conversation all the opinions which are generally expressed with ease and sleep-walking assurance became so doubtful that I had to cease altogether taking part in such talk. It filled me with an in­explicable anger, which I could conceal only with effort, to hear such things as: This affair has turned out well or ill for this or that person; Sheriff N. is a bad, Parson T. a good man; Farmer M. is to be pitied, his sons are wasters; another is to be envied because his daughters are thrifty; one family is rising in the world, another is on the downward path. All this seemed as indemonstrable, as mendacious and hollow as could be. My mind compelled me to view all things occurring in such conversations from an uncanny closeness. As once, through a magnifying glass, I had seen a piece of skin on my little finger look like a field full of holes and furrows, so I now perceived human beings and their actions. I no longer suc­ceeded in comprehending them with the simplifying eye of habit. For me everything disintegrated into parts, those parts again into parts; no longer would anything let itself be en­compassed by one idea. Single words floated round me; they congealed into eyes which stared at me and into which I was forced to stare back-whirlpools which gave me vertigo and, reeling incessantly, led into the void. 
        I tried to rescue myself from this plight by seeking refuge in the spiritual world of the Ancients. Plato I avoided, for I dreaded the perilousness of his imagination. Of them all, I in­tended to concentrate on Seneca and Cicero. Through the harmony of their clearly defined and orderly ideas I hoped to regain my health. But I was unable to find my way to them. These ideas, I understood them well: I saw their wonderful interplay rise before me like magnificent fountains upon which played golden balls. I could hover around them and watch how they played, one with the other; but they were concerned only with each other, and the most prof6und, most personal quality of my thinking remained excluded from this magic circle. In their company I was overcome by a terrible sense of loneliness; I felt like someone locked in a garden sur­rounded by eyeless statues. So once more I escaped into the open. 
        Since that time I have been leading an existence which I fear you can hardly imagine, so lacking in spirit and thought is its flow: an existence which, it is true, differs little from that of my neighbours, my relations, and most of the land­owning nobility of this kingdom, and which is not utterly bereft of gay and stimulating moments. It is not easy for me to indicate wherein these good moments subsist; once again words desert me. For it is, indeed, something entirely un­named, even barely nameable which, at such moments, re­veals itself to me, filling like a vessel any casual object of my daily surroundings with an overflowing flood of higher life. I cannot expect you to understand me without examples, and I must plead your indulgence for their absurdity. A pitcher, a harrow abandoned in a field, a dog in the sun, a neglected cemetery, a cripple, a peasant's hut-all these can become the vessel of my revelation. Each of these objects and a thousand others similar, over which the eye usually glides with a natural indifference, can suddenly, at any moment (which I am ut­terly powerless to evoke), assume for me a character so exalted and moving that words seem too poor to describe it. Even the distinct image of an absent object, in fact, can acquire the mysterious function of being filled to the brim with this silent but suddenly rising flood of divine sensation. Recently, for instance, I had given the order for a copious supply of rat-poison to be scattered in the milk cellars of one of my dairy-farms. Towards evening I had gone off for a ride and, as you can imagine, thought no more about it. As I was trotting along over the freshly-ploughed land, nothing more alarming in sight than a scared covey of quail and, in the distance, the great sun sinking over the undulating fields, there suddenly loomed up before me the vision of that cellar, resounding with the death-struggle of a mob of rats. I felt everything within me: the cool, musty air of the cellar filled with the sweet and pungent reek of poison, and the yelling of the death cries breaking against the mouldering walls; the vain convulsions of those convoluted bodies as they tear about in confusion and despair; their frenzied search for escape, and the grimace of icy rage when a couple collide with one an­other at a blocked-up crevice. But why seek again for words which I have foresworn! You remember, my friend, the won­derful description in Livy of the hours preceding the destruc­tion of Alba Longa: when the crowds stray aimlessly through the streets which they are to see no more . . . when they bid farewell to the stones beneath their feet. I assure you, my friend, I carried this vision within me, and the vision of burning Carthage, too; but there was more, something more divine, more bestial; and it was the Present, the fullest, most exalted Present. There was a mother, surrounded by her young in their agony of death; but her gaze was cast neither toward the dying nor upon the merciless walls of stone, but into the void, or through the void into Infinity, accompanying this gaze with a gnashing of teeth!-A slave struck with help­less terror standing near the petrifying Niobe must have ex­perienced what I experienced when, within me, the soul of this animal bared its teeth to its monstrous fate. 
        Forgive this description, but do not think that it was pity I felt. For if you did, my example would have been poorly chosen. It was far more and far less than pity: an immense sympathy, a flowing over into these creatures, or a feeling that an aura of life and death, of dream and wakefulness, had flowed for a moment into them-but whence? For what had it to do with pity, or with any comprehensible concatenation of human thought when, on another evening, on finding beneath a nut-tree a half-filled pitcher which a gardener boy had left there, and the pitcher and the water in it, darkened by the shadow of the tree, and a beetle swimming on the surface from shore to shor~when this combination of trifles sent through me such a shudder at the presence of the Infinite, a shudder running from the roots of my hair to the marrow of mv heels? What was it that made me want to break into words which, I know, were I to find them, would force to their knees those cherubim in whom I do not believe? What made me turn silently away from this place? Even now, after weeks, catching sight of that nut-tree, I pass it by with a shy sidelong glance, for I am loath to dispel the memory of the miracle hovering there round the trunk, loath to scare away the celestial shudders that still linger about the shrubbery in this neighbourhood! In these moments an insignificant creature-a dog, a rat, a beetle, a crippled apple tree, a lane winding over the hill, a moss-covered stone, mean more to me than the most beautiful, abandoned mistress of the happiest night. These mute and, on occasion, inanimate creatures rise toward me with such an abundance, such a presence of love, that my enchanted eye can find nothing in sight void of life. Every­thing that exists, everything I can remember, everything touched upon by my confused thoughts, has a meaning. Even my own heaviness, the general torpor of my brain, seems to acquire a meaning; I experience in and around me a blissful, never-ending interplay, and among the objects playing against one another there is not one into which I cannot flow. To me, then, it is as though my body consists of nought but ciphers which give me the key to everything; or as if we could enter into a new and hopeful relationship with the whole of exist­ence if only we begin to think with the heart. As soon, how­ever, as this strange enchantment falls from me, I find myself confused; wherein this harmony transcending me and the en­tire world consisted, and how it made itself known to me, I could present in sensible words as little as I could say any­thing precise about the inner movements of my intestines or a congestion of my blood. 
        Apart from these strange occurrences, which, incidentally, I hardly know whether to ascribe to the mind or the body, I live a life of barely believable vacuity, and have difficulties in concealing from my wife this inner stagnation, and from my servants the indifference wherewith I contemplate the affairs of my estates. The good and strict education which I owe to my late father and the early habit of leaving no hour of the day unused are the only things, it seems to me, which help me maintain towards the outer world the stability and the dig­nified appearance appropriate to my class and my person. 
        I am rebuilding a wing of my house and am capable of conversing occasionally with the architect concerning the progress of his work; I administer my estates, and my tenants and employees may find me, perhaps, somewhat more taciturn but no less benevolent than of yore. None of them, standing with doffed cap before the door of his house while I ride by of an evening, will have any idea that my glance, which he is wont respectfully to catch, glides with longing over the rickety boards under which he searches for earthworms for fishing-bait; that it plunges through the latticed window into the stuffy chamber where, in a corner, the low bed with its chequered linen seems forever to be waiting for someone to die or another to be born; that my eye lingers long upon the ugly puppies or upon a cat stealing stealthily among the flower-pots; and that it seeks among all the poor and clumsy objects of a peasant's life for the one whose insignificant form, whose unnoticed being, whose mute existence, can become the source of that mysterious, wordless, and boundless ecstasy. For my unnamed blissful feeling is sooner brought about by a distant lonely shepherd's fire than by the vision of a starry sky, sooner by the chirping of the last dying cricket when the autumn wind chases wintry clouds across the deserted fields than by the majestic booming of an organ. And in my mind I compare myself from time to time with the orator Crassus, of whom it is reported that he grew so excessively enamoured of a tame lamprey-a dumb, apathetic, red-eyed fish in his ornamental pond-that it became the talk of the town; and when one day in the Senate Domitius reproached him for having shed tears over the death of this fish, attempting thereby to make him appear a fool, Crassus answered, "Thus have I done over the death of my fish as you have over the death of neither your first nor your second wife." 
        I know not how oft this Crassus with his lamprey enters mv mind as a mirrored image of my Self, reflected across the abyss of centuries. But not on account of the answer he gave Domitius. The answer brought the laughs on his side, and the whole affair turned into a jest. I, however, am deeply affected by the affair, which would have remained the same even had Domitius shed bitter tears of sorrow over his wives. For there would still have been Crassus, shedding tears over his lam­prey. And about this figure, utterly ridiculous and contempti­ble in the midst of a world-governing senate discussing the most serious subjects, I feel compelled by a mysterious power to reflect in a manner which, the moment I attempt to express it in words, strikes me as supremely foolish. 
        Now and then at night the image of this Crassus is in my brain, like a splinter round which everything festers, throbs, and boils. It is then that I feel as though I myself were about to ferment, to effervesce, to foam and to sparkle. And the whole thing is a kind of feverish thinking, but thinking in a medium more immediate, more liquid, more glowing than words. It, too, forms whirlpools, but of a sort that do not seem to lead, as the whirlpools of language, into the abyss, but into myself and into the deepest womb of peace. 
        I have troubled you excessively, my dear friend, with this extended description of an inexplicable condition which is wont, as a rule, to remain locked up in me. 
        You were kind enough to express your dissatisfaction that no book written by me reaches you any more, "to compensate for the loss of our relationship." Reading that, I felt, with a certainty not entirely bereft of a feeling of sorrow, that neither in the coming year nor in the following nor in all the years of this my life shall I write a book, whether in English or in Latin: and this for an odd and embarrassing reason which I must leave to the boundless superiority of your mind to place in the realm of physical and spiritual values spread out har­moniously before your unprejudiced eye: to wit, because the language in which I might be able not only to write but to think is neither Latin nor English, neither Italian nor Spanish, but a language none of whose words is known to me, a lan­guage in which inanimate things speak to me and wherein I may one day have to justify myself before an unknown judge. 
        Fain had I the power to compress in this, presumably my last, letter to Francis Bacon all the love and gratitude, all the unmeasured admiration, which I harbour in my heart for the greatest benefactor of my mind, for the foremost Englishman of my day, and which I shall harbour therein until death break it asunder.
         '''
	print(naivesum.summarize(text2,4))
	print(naivesum.summarize(text,2))
	
