###########
# Grapher #
###########

# Bokeh graphing library stuff
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, LabelSet

def plot_data(pred_df):
	# Turn datafarme into a form that Bokeh can plot
	src = ColumnDataSource(pred_df)

	# Create figure
	p = figure(plot_height=600, plot_width=2500, 
		title="Developer Salaries (Predicted)")

	# Create vertical bar
	p.vbar(x='x', top='y', width=0.9, source=src)

	# Add labels
	labels = LabelSet(x='x', y='y', level='glyph', 
		x_offset=0, y_offset=0, text='indices', text_font_size='8pt', 
		source=src, render_mode='canvas')
	p.add_layout(labels)

	return p