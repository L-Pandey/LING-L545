<center><h1>Practical - 01_Tokenization </h1></center>

<h2>Question1: Why should we split punctuation from the token it goes with ?</h2>

<p> Tokenization is the process of splitting a sentence into a sequence of characters that make sense and have a meaning. There are different types of punctuation marks and each punctuation mark is a character in itself. Tokenization also helps to reduce the complexity by splitting a huge text into chucks. For instance - ('Text') can be further simplified as:
<ol>
<li>(</li>
<li>'</li>
<li>Text</li>
<li>'</li>
<li>)</li>

</ol> 
By considering the punctuation marks as separate tokens, we are also able to reduce the complexity of word.
Therefore, it becomes easier for the language models to form word embeddings. Many models don't have the support for special characters and therefore, splitting the text and punctuation can be helpful in that case.

Another example is - 'Hurray!!!'  Though it might be helpful to keep punctuation for sentiment analysis, but for a general text analysis, punctuations can cause problems. Therefore, splitting punctuation makes sure that each token is treated as a single entity with equality. 
</p>
<hr>

<h2>Question2: Should abbreviations with space in them be written as a single token or two tokens ?
How about numerals like 134 000 ?</h2>

<p> 
There are certain abbreviations in the English language such as 'U.S.A' or 'A. B. Smith' where different rules apply. There are certain words which should be considered as a single token or else the actual meaning of the token changes. Similary, in case of '134 000', this should be a single token or else the entire amount changes.
</p>

<hr>

<h2>Question3: If you have a case suffix following punctuation, how should it be tokenised ?</h2>

<p> In case of a case suffix following punctuation such as - "L'aragonés" or "l'idioma", then they should be tokenized separately. So the above example will become - L, ', aragonés</p>

<hr>

<h2>Question4: Should contractions and clitics be a single token or two (or more) tokens ?</h2>

</p> Contraction words are the words like "I'm" or "can't". These words can be tokenized into two or more tokens. Some examples include -
<ul>
<li> token1 - I <br>token2 -  m
<li> token1 - I' <br> token2 - m
<li> token1 - I'm
</ul>

It strongly depends upon the type of NLP application.
</p>
