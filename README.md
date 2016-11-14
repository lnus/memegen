# Memegen
Python module for easily generating dank memes.

# Documentation
This doesn't really need a documentation, just import it really.

###Example:

```python
from memegen import memeGen
m = memeGen()
m.generate("TOP", "BOTTOM", "IMAGEFILE")
```

#Kwargs

I've added kwarg support so now you can modify certain things, like:

thickness, font, text color, outline color, output file

###Example:

```python
m.generate("TOP", "BOTTOM", "IMAGEFILE", output="OUTPUTFILE", textcolor="white", stroke="black", thickness=3)
```

#Dependencies

PIL is the only dependency for this.
```pip
pip install Pillow
```
