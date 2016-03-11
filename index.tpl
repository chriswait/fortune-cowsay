<html>
    <head>
        <title>Fortune</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <style>
			body {
				margin: 0;
				color: black;
			}
			#parent {
				position: absolute;
				top: 0px;
				left: 0px;
				width: 100%;
				height: 100%;
				display: flex;
				justify-content: center;
				align-items: center;
				overflow: hidden;
			}
			#fortune {
				max-width: 100%;
				font-family: monospace;
				white-space: pre;
			}
			#footer {
				position: absolute;
				bottom: 0px;
				width: 100%;
				display: flex;
				justify-content: center;
				align-items: center;
			}
			#footer a {
				font-family: monospace;
				white-space: pre;
				font-variant: small-caps;
				font-size: 20px;
				padding-bottom: 20px;
				color: purple;
			}
			.blast {
				display: inline-block;
				opacity: 0;
			}
        </style>
        <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
        <script type="text/javascript" src="http://julian.com/research/velocity/build/jquery.velocity.min.js"></script>
        <script type="text/javascript" src="http://julian.com/research/velocity/build/velocity.ui.js"></script>
        <script type="text/javascript" src="http://julian.com/research/blast/build/jquery.blast.js"></script>
        <script>
		  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		  ga('create', 'UA-75004686-1', 'auto');
		  ga('send', 'pageview');
		</script>
    </head>
    <body>
		<div id="parent">
			<div id="fortune">{{output}}</div>
		</div>
		<div id="footer">
			<a href="http://chriswait.net">What is happening?</a>
		</div>
        <script type="text/javascript">
			$("#fortune")
			.blast({delimiter: "word"})
			.velocity("transition.fadeIn", { 
				display: null,
				duration: 250,
				stagger: 40
			});
        </script>
    </body>
</html>
