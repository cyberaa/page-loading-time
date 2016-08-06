<div class="row">
	<div class="col-lg-6">
		<table class="table table-striped">
			<tr>
				<th>URL</th>
				<th>Loading time</th>
			</tr>
			% for result in rank_load:
			<tr>
				<td><a href="{{ result['url'] }}">{{ result['url'] }}</a></td>
				<td>{{ round(result['loading_time'] * 1000, 2) }} ms</td>
			</tr>
			% end
		</table>
	</div>
	<div class="col-lg-6">
		<table class="table table-striped">
			<tr>
				<th>URL</th>
				<th>Page size</th>
			</tr>
			% for result in rank_size:
			<tr>
				<td><a href="{{ result['url'] }}">{{ result['url'] }}</a></td>
				<td>{{ round(result['page_size'] / 1024, 2) }} kB</td>
			</tr>
			% end
		</table>
	</div>
</div>
