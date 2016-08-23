import textwrap
from PIL import Image, ImageDraw, ImageFont

class memeGen():
	def generate(self, top, bot, image, **kwargs):
		#Opens up your SPICY MEME TEMPLATE
		im = Image.open(image)

		#Resizes the image for perfect MEME size
		im = im.resize((500, 500), Image.ANTIALIAS)

		#Stupid fucking useless arguments
		self.output = "output.png"
		self.font = ImageFont.truetype("impact.ttf", 60)
		self.stroke = "black"
		self.textcolor = "white"
		width, height = im.size
		draw = ImageDraw.Draw(im)
		topH, topP = 0, 10
		botH, botP = 420, 10
		pTop = textwrap.wrap(top, width=15)
		pBot = textwrap.wrap(bot, width=15)
		
		#Sets up the keyword arguments if you want proper CUSTOMIZATION
		for key, value in kwargs.items():
			setattr(self, key, value)

		#Writes the text with a spicy meme outline
		for line in pTop:
			w, h = draw.textsize(line, font=self.font)
			draw.text((((width - w)/2)-3, topH), top, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2)+3, topH), top, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2), topH-3), top, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2), topH+3), top, font=self.font, fill=self.stroke)
			draw.text(((width - w)/2, topH), top, font=self.font, fill=self.textcolor)
			topH += h + topP
		
		for line in pBot:
			w, h = draw.textsize(line, font=self.font)
			draw.text((((width - w)/2)-3, botH), bot, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2)+3, botH), bot, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2), botH-3), bot, font=self.font, fill=self.stroke)
			draw.text((((width - w)/2), botH+3), bot, font=self.font, fill=self.stroke)
			draw.text(((width - w)/2, botH), bot, font=self.font, fill=self.textcolor)
			botH += h + botP

		#saves the dank meme	
		im.save(self.output)
