### BEGIN CONFIGURATION ###

# the top-level dictionary key is a name that doesn't necessarily define whether to set background or foreground
# whether to set background or foreground is determined by values within the group dict. if a value is an empty string, or if the group is a list, the palette name will be used, or in the case of settings keys, not needed
# group lists or dict keys can include both scopes and names of settings keys
# palette can be a list of hex strings (a static palette), or a list of parameters to pass to generatePalette

configuration = {
	'name' : 'Mimic Dark',
	'type' : 'Windows Terminal',
}

palettes = {
	'grayscale' : {
		'palette' : {'chroma':0, 'hue':0, 'xMin':0, 'xMax':1.0},
		'groups' : [
			['background', 'black'],
			[],
			['selectionBackground'],
			['brightBlack'],
			[],
			['foreground', 'white'],
			[],
			['brightWhite', 'cursorColor'],
		],
	},
	'colors' : {
		'palette' : {'lightness':0.45, 'hues': [29, 110, 142, 195, 264, 328]},
		'groups' : [
			['red'],
			['yellow'],
			['green'],
			['cyan'],
			['blue'],
			['purple'],
		]
	},
	'brightcolors' : {
		'palette' : {'lightness':0.75, 'hues':'colors'},
		'groups' : [
			['brightRed'],
			['brightYellow'],
			['brightGreen'],
			['brightCyan'],
			['brightBlue'],
			['brightPurple'],
		]
	},
}

fontStyles = {
}

### END CONFIGURATION ###