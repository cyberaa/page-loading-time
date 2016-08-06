% rebase('base.tpl', title='Ranking')

<div style="padding-top: 40px">
	<img style="display: block; margin: auto" src="/static/loading.gif">
</div>

<script type="text/javascript">
	$( document ).ready(function() {
		$.ajax({
			url: "/loadtest",
			context: $('.container')
		}).done(function( data, error ) {
			if ( error == 'success' ) {
				$( this ).html( data );
			} else {
				$( this ).html( 'An error occured: ' + error );
			}
		});
	});
</script>
