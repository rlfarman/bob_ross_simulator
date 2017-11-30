# Bob Ross Simulation Proposal

## Jesse Bulson-Lewis, Richard Farman, Zach Turner

Our goal is to make a program capable of simulating the generation of paintings
based on those of the esteemed Bob Ross. The idea is to generate new paintings 
that are representative of something that Bob Ross would create, with similar
elements and style. To do this, we will generate a random set of elements, then
create a mockup image with art assets

Our simulation would follow the steps below.

1. Reading the data and creating a Markov chain that accords with that data. A 
certain measure of preprocessing will be performed on the data, so that we
exclude features that aren't relevant or easy to reproduce.

2. Use that Markov chain to generate a set of elements which will appear in the
generated image.

3. Use that set of elements to create an image that contains stock assets
corresponding to those elements. At this stage, we're not trying to make a 
good looking image, just create a framework for random generation of simple images.

4. Use that image in conjuction with a deep convolutional generative adversarial
network (DCGAN) to generate a painting in the style of the ever-esteemed
Bob Ross' artwork. We'll do this by training a model on a painting created by
Bob Ross. See (4b) for more details.

4b. By clustering the paintings, we can figure out the painting closest to our
generated image.

We'll work together to figure out how to repurpose a Markov Chain for the context
of a dataset with true or false (0 or 1) values. Richard has experience with AI
and NLP, so he will determine the methods we'll be using in our program.
Jesse and Zach will help implement the algorithm.

Jesse and Zach will create a simple image generator that places elements on a canvas.
Richard will find art assets to use for the generator.

The final step (4) requires a powerful machine with lots of dependencies to set up, as
well as quite a long time to train a model. So this won't be easy to replicate on
other machines. Richard has an environment set up, so we'll plan to do testing on there.

The first purpose of this program, first and foremost, is to be able to generate
artwork with at least some semblance to work by Bob Ross, for artistic purposes.

Another use for this program is generating random data for a database. We can create random entries that will naturally reflect the data it is trained on, which might be nice for quickly creating large datasets from smaller ones for the sake of testing.
