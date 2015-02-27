# dresscolor

*Note: This depends on the quality of the picture. If the original photo is proven to be tampered with or just plain bad photography, then take these results with a grain of salt.*

Trying to solve The Great Internet Debate of 2/26/15. This is a Python program that determines the top 8 colors prominent in the picture. Reads the image file and generates rectangles that represent each of the 8 colors. Uses the PIL library.

Link to the original page: http://swiked.tumblr.com/post/112073818575/guys-please-help-me-is-this-dress-white-and

Mirror just in case: http://i.imgur.com/EPEQ8Nl.jpg

<h2>Usage</h2>

* Save image as "a.jpg" and run in the same directory with Python2.7

<h2>Conclusion</h2>

You'll notice that the generated image has white as one of the colors. However, we can neglect that. Here's why:
  1. Suppose the dress is white and gold.
  2. Well, that means that blue will not exist.
  3. Since blue exists as one of the top colors, we can conclude by contradiction that the dress is truly blue.
