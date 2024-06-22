### BEGIN CONFIGURATION ###

# the top-level dictionary key is a name that doesn't necessarily define whether to set background or foreground
# whether to set background or foreground is determined by values within the group dict. if a value is an empty string, or if the group is a list, the palette name will be used, or in the case of settings keys, not needed
# group lists or dict keys can include both scopes and names of settings keys
# palette can be a list of hex strings (a static palette), or a list of parameters to pass to generatePalette
palettes = {
	'grayscale' : {
		'palette' : {'chroma':0, 'hue':0, 'xMin':0.216, 'xMax':0.722},
		'groups' : [
			['background', 'findHighlightForeGround', 'selectionBorder'],
			['selection', 'lineHighlight'],
			['stackGuide', 'invisibles'],
			['guide'],
			['activeGuide'],
			['foreground', 'caret'],
		],
	},
	'foreground' : {
		'palette' : {'lightness':0.722, 'chroma':0.1476},
		# 'palette' : {'lightness':0.722, 'chroma':0.14, 'hues':[96, 151, 233, 288, 343, 38]},
		'groups' : [
			['string', 'markup.italic', 'markup.bold', 'markup.strike'], #yellow
			['meta.function', 'variable.function', 'entity.other.attribute-name'], # green
			['storage.type', 'support.function', 'support.constant', 'support.class', 'support.type', 'meta.separator', 'keyword.declaration'], # sky blue
			{'constant':''}, # lilac
			{'keyword':'', 'storage':'', 'entity.name.tag':'', 'markup.heading':'', 'invalid.deprecated':'background'}, # pink
			{'variable.parameter':'', 'invalid':'background'}, # orange
		]
	},
	'background' : {
		'palette' : {'lightness':0.216, 'chroma':0.036, 'hues':'foreground'},
		'groups' : [
			[],
			['meta.arrayindex, meta.item-access.arguments'],
			[],
			[],
			{'invalid':'foreground'},
			{'invalid.deprecated':'foreground'},
		]
	},
	'comment' : {
		'palette' : {'lightness':0.722, 'chroma':0.07, 'hues':[64]},
		'groups' : [
			{'comment':'foreground', 'findHighlight':''},
		]
	}
}

fontStyles = {
	'variable.parameter' : 'italic',
	'support.type' : 'italic',
	'support.class' : 'italic',
	'storage.type' : 'italic',
	'entity.other.inherited-class' : 'italic underline',
	'entity.name.class' : 'underline',
	'invalid' : 'bold',
	'invalid.deprecated' : 'bold',
	'markup.heading' : 'underline',
	'markup.italic' : 'italic',
	'markup.bold' : 'bold',
}

### END CONFIGURATION ###