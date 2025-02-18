Write a product spec (PRD) for the following. It should be detailed enough that it can be given to a senior software engineer to create a detailed engineering design document, which can then by implemented unambiguously by a junior software engineer. But for now only write the PRD.

The PRD should be in markdown format, and put into the file docs/product_spec.md.

I use a prompt with an LLM to come up with chapters (timestamps and titles) for my YouTube videos.

The input is the transcript for the video in SRT format (i.e. it has timestamps).

And then I use the following prompt:

```
I will give you a video transcript in SRT format. Come up with logical chapter markers with timestamp and title, in youtube format. 
```

After that I will ask the LLM to suggest 10 short but catchy titles using the following prompt:

```
suggest 10 short catchy titles for a youtube video with this content. but i don't want them to be cheesy or sound like clickbait.
```

Now I want to write a script/tool that automatically does that.