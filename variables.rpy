define flash = Fade(0.1, 0.0, 0.5, color="#fff")
default pushSanti = 0
default dropGabriel = 0
define subject = "they"
define contration = "they're"
define object1 = "them"
define possessive = "theirs"
define possessive_adjective = "their"
define eflexive = "themselves"

menu:

    "She/Her/Hers":
        $subject = "she"
        $contration = "she's"
        $object1 = "her"
        $possessive = "hers"
        $possessive_adjective = "her"
        $reflexive = "herself"
        jump next_part
    "He/Him/His":
        $subject = "he"
        $contration = "he's"
        $object1 = "him"
        $possessive = "his"
        $possessive_adjective = "his"
        $reflexive = "himself"
        jump next_part
    "They/Them/Theirs":
        $subject = "they"
        $contration = "they're"
        $object1 = "them"
        $possessive = "theirs"
        $possessive_adjective = "their"
        $reflexive = "themselves"
        jump next_part
        #add !c after the string
#m "So your pronouns are [subject!c]/[object!c]"

