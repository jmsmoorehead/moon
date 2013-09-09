class ISBNWidget(forms.TextInput):
	def __init__(self, language=None, attrs={}):
		super(ISBNWidget, self).__init__(attrs=attrs)
	def render(self, name, value, attrs={}):
		if (not value) or len(str(value)) < 2:
			return super(ISBNWidget, self).render(name, value, attrs)
		return super(ISBNWidget, self).render(name, value, attrs) + mark_safe("""
			<br />
			<div class="alt">%s-digit: <span class="altisbn">%s <span class="doodad">
				<a href="http://www.librarything.com/isbn/%s">more &#9901;</a>
			</span></span></div>
		""" % (
			(len(str(value)) == 10) and "13" or "10",
			pyisbn.convert(value),
			value