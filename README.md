# Rhyme-Check

This is a very simple micromaterial created for the Oxford [Summer of Hacks](https://summerofhacks.io) [Language Hack Day](https://summerofhacks.io/#2019:3-language-hackday).

The aim is to give learners practice in converting from regular text to [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet), and then to finding
single syllable rhymes using IPA.

## learning objectives

- what IPA is, and how to convert regular text to IPA
- match vowel phonemes and final consonant phonemes in IPA to find rhymes

## The activity

We want to use rhymes to create some fun text of our own, but first we need to find
some rhymes. We'll limit this activity to only finding rhymes in single-syllable
words, since that's much easier, and largely predictable.

We'd like to take an input text (maybe all the lyrics of the Beatles songs?) and
get a list of all the rhymes in it:

for example, a list like "snow, go, slow, know, though, low"...

Then, we can create our own madlibs template to be filled in with rhymes
(a sample template exists in `./data/template`, so you can use that one, or create
your own.

One big skeleton function has already been written, along with the test for it.
So to complete the activit , just fill in the functions and run the tests.
If the test passes, you did it! If not, try to fix the function so the test passes.

to run the test:
`python -m unittest`

## Possible steps:

### 1) find out about IPA.
Some resources are [here](https://penandthepad.com/convert-english-ipa-7396725.html) and [here](http://dialectblog.com/the-international-phonetic-alphabet/the-ipa-vowels/) and [the more verbose wikipedia article](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet).

There are various python libraries to help you easily convert between regular text and IPA:

- [https://github.com/mphilli/English-to-IPA](https://github.com/mphilli/English-to-IPA)
- [https://github.com/pettarin/ipapy](https://github.com/pettarin/ipapy)
- [https://github.com/dmort27/epitran](https://github.com/dmort27/epitran)

The one that I recommend is `epitran`, mostly because it has a very simple API once it's installed and configured.

There are some additional things to install to get this working, namely the `flite` speech to text utility, though the steps are a bit more involved then just `pip install flite`.

clone the repo at https://github.com/festvox/flite

Also make sure you have a C compiler installed; `gcc` should be sufficient.

then
```
$ git clone git@github.com:festvox/flite.git
$ cd flite/
$ ./configure && make
$ sudo make install
$ cd testsuite
$ make lex_lookup
$ sudo cp lex_lookup /usr/local/bin
```

after that, the hard part is done, and you should be able to use:
```
import epitran
epi = epitran.Epitran('eng-Latn')
epi.transliterate('string')
```

to turn a single word into its IPA representation.

### 2) Find rhymes from IPA

This is most of the meat of this activity, though some things to think about:

- you can technically convert an entire sentence (or longer) into IPA with
something like epitran, though you may want to start with just a single word to
IPA at a time. This will be more predictable and easier to think about and
work with.

- when you're reading in text (either from a file or just in memory), you need
to get rid of all the "extra stuff" like punctuation and numbers (basically
anything that isn't a letter).

- once you have the list of all the words in IPA, you need to compare the IPA
vowels to see if they are the same. To find things that are true rhymes, you
will also want to match all the sounds after these vowels.

Words like "boat" and "grown" will have the same IPA vowel, but we usually
wouldn't say that they "rhyme". That's because the consonant sound at the end
isn't the same, whereas a word like "float" would more clearly rhyme with "boat".

One easy way to compare these final vowels and the sounds after them might be to sort the IPA representations (these funny symbols should still be sortable via python).

- keep track of the "regular" forms of the words that rhyme, so you can use these
later as the thing your `find_all_rhymes` function gives back.
