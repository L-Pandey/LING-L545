# Report

<table border="0">
 <tr>
    <td><b style="font-size:30px">TESTINGOUT.conllu</b></td>
    <td><b style="font-size:30px">test.conllu</b></td>
 </tr>
 <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/10.png"></td>
    <td><img src="./test.conlluScreenshots/10.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/11.png"></td>
    <td><img src="./test.conlluScreenshots/11.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/13.png"></td>
    <td><img src="./test.conlluScreenshots/13.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/14.png"></td>
    <td><img src="./test.conlluScreenshots/14.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/15.png"></td>
    <td><img src="./test.conlluScreenshots/15.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/17.png"></td>
    <td><img src="./test.conlluScreenshots/17.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/26.png"></td>
    <td><img src="./test.conlluScreenshots/26.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/27.png"></td>
    <td><img src="./test.conlluScreenshots/27.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/38.png"></td>
    <td><img src="./test.conlluScreenshots/38.png"></td>
 </tr>
  <tr>
    <td><img src="./TESTINGOUT.conlluScreenshots/44.png"></td>
    <td><img src="./test.conlluScreenshots/44.png"></td>
 </tr>
</table>

<h2>Performance </h2>
<img src="metrics.png">

<br>

<h2>Observations </h2>
<p>
<ul>
<li>English language tree bank (en_atis-ud-train) was used to train and test the model.
<li>UAS and LAS dependecy scores are not 100% accurate.
<li>Based on the comparison from the table above, it is found that the model successfully identifies the Lemma, tenses, verbForm, person etc. However, many times the model fails to identify the 'root'. In many tree banks, 'nsubj' (nominal subject) is mistaken for 'root'.
<li> The model also fails to identify the 'compound' words which can be seen in row 4 in the above table.
<li> 'nmod' (nominal modifier) are mistaken for 'compound' words.
<li> The above errors are constantly repeated in a majority of tree banks. This indicates the reason for decline in the UAS and LAS scores.
</ul>
</p>