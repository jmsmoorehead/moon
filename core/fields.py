from .widgets import ISBNWidget

class ISBNField(models.CharField):

	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 13
		super(ISBNField, self).__init__(*args, **kwargs)

	def formfield(self, **kwargs):
		kwargs['widget'] = ISBNWidget()
		return super(ISBNField, self).formfield(**kwargs)