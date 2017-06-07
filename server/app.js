+function($) {
	'use strict';

	var App = function () {

	}

	App.VERSION = "0.0.1";

	App.DEFAULTS = {
		appTitle: "PoE Currency Valuator",
		currencyOrder: [
			"Identification",
      ""
		]
	}

	App.prototype.createElement = function (element, options) {
		var $elem = $(element);

		if ('style' in options) {
			Object.keys(options.style).forEach(function(k, v){
				console.log(k, v);
			});
		}

		if ('innerHtml' in options) {
			$elem.html(options.innerHtml);
		}

		return $elem;
	}

	App.prototype.init = function (root) {
		this.root = root;
		this.$root = $(root);

		var k = this.createElement('<h1>', {
			style: {},
			innerHtml: App.DEFAULTS.appTitle
		})

		this.$root.append(k);
	}

	App.prototype.run = function () {

	}

	window.App = App;
	
}(jQuery);