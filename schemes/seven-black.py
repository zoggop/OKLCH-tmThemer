### BEGIN CONFIGURATION ###

# the top-level dictionary key is a name that doesn't necessarily define whether to set background or foreground
# whether to set background or foreground is determined by values within the group dict. if a value is an empty string, or if the group is a list, the palette name will be used, or in the case of settings keys, not needed
# group lists or dict keys can include both scopes and names of settings keys
# palette can be a list of hex strings (a static palette), or a list of parameters to pass to generatePalette
palettes = {
	'grayscale' : {
		'palette' : {'chroma':0, 'hue':0, 'xMin':0, 'xMax':60},
		'groups' : [
			['background', 'findHighlightForeGround', 'selectionBorder'],
			['selection', 'lineHighlight'],
			['stackGuide', 'invisibles'],
			['guide'],
			['activeGuide'],
			['foreground', 'caret'],
		],
	},
	'background' : {
		'palette' : {'lightness':15, 'chroma':42},
		'groups' : [
			{'invalid':'foreground', 'invalid.deprecated':'foreground'},
			['meta.arrayindex, meta.item-access.arguments'],
			[],# ['entity.name.class', 'entity.name.function', 'entity.other.inherited-class'],
		]
	},
	'foreground' : {
		'palette' : {'lightness':60, 'chroma':63},
		'groups' : [
			['storage.type', 'support.function', 'support.constant', 'support.class', 'support.type', 'meta.separator', 'keyword.declaration'],
			{'constant':''},
			{'keyword':'', 'storage':'', 'entity.name.tag':'', 'invalid':'background', 'markup.heading':''},
			{'variable.parameter':'', 'invalid.deprecated':'background'},
			['string', 'markup.italic', 'markup.bold', 'markup.strike'],
			['meta.function', 'variable.function', 'entity.other.attribute-name'], # 'meta.functioncall, meta.function-call'
			# [],
			# ['variable, support.variable, meta.qualified-name, support.other.variable'],
		]
	},
	'comment' : {
		'palette' : {'lightness':60, 'chroma':31},
		'groups' : [
			[],
			{'comment':'foreground', 'findHighlight':''},
			[],
			[],
			[],
			[],
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