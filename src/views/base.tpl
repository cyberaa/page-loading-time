<!DOCTYPE html>
<html lang="en">
<head>
	<title>{{title or 'Load time'}}</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha.3/css/bootstrap.min.css" rel="stylesheet" type="text/css">
	%# <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-alpha.3/js/bootstrap.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<style type="text/css">
		.loading {
			-webkit-animation: rotation 2s infinite linear;
			animation: rotation 2s infinite linear;
		}

		@-webkit-keyframes rotation {
			from {-webkit-transform: rotate(0deg);}
			to   {-webkit-transform: rotate(359deg);}
		}
		
		/*firefox*/
		@keyframes{
			from {transform: rotate(0deg);}
			to   {transform: rotate(359deg);}
		}
	</style>
</head>
<body>
	<div class="container">
		{{!base}}
	</div>
</body>
</html>
