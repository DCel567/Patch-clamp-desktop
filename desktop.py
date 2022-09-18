import data_cutting as cutting
import predictor as predicting
import tkinter as t


def cut_intervals():
	first_points = 0
	last_points = 500000

	first = text_first_points.get()
	if first.isdigit():
		first_points = int(first)

	second = text_last_points.get()
	if second.isdigit():
		last_points = int(second)

	print(first_points, last_points)

	cutting.start_cutting(first_points, last_points)


def predict_interval():
	file_name = '0.0001_6.5.csv'
	first_points = 0
	last_points = 1000

	name = text_file_name.get()
	if name != '':
		if name[0:9] == 'intervals':
			file_name = name
		else:
			file_name = 'intervals/'+name

	first = text_first_window.get()
	if first.isdigit():
		first_points = int(first)

	second = text_last_window.get()
	if second.isdigit():
		last_points = int(second)

	print(file_name, first_points, last_points)

	predicting.start_predicting(file_name, first_points, last_points)


if __name__ == "__main__":
	window = t.Tk()
	window.title('Patch-clamp desktop')
	window.geometry('600x400')

	topFrame = t.Frame(window, padx=10, pady=10)
	bottomFrame = t.Frame(window, padx=10, pady=10)

	label_first_intervals = t.Label(topFrame, text='First interval point: ')
	label_last_intervals = t.Label(topFrame, text='Last interval point: ')

	text_first_points = t.StringVar()
	text_last_points = t.StringVar()
	entry_first_points = t.Entry(topFrame, textvariable=text_first_points, width=15)
	entry_last_points = t.Entry(topFrame, textvariable=text_last_points, width=15)
	button_cut = t.Button(topFrame, text='Cut', command=cut_intervals)

	text_first_window = t.StringVar()
	text_last_window = t.StringVar()
	text_file_name = t.StringVar()
	entry_file_name = t.Entry(bottomFrame, textvariable=text_file_name, width=30)
	entry_first_window = t.Entry(bottomFrame, textvariable=text_first_window, width=15)
	entry_last_window = t.Entry(bottomFrame, textvariable=text_last_window, width=15)
	button_predict = t.Button(bottomFrame, text='Predict', command=predict_interval)

	topFrame.pack()
	bottomFrame.pack()

	label_first_intervals.pack(side=t.LEFT)
	entry_first_points.pack(side=t.LEFT)
	label_last_intervals.pack(side=t.LEFT)
	entry_last_points.pack(side=t.LEFT)
	button_cut.pack(side=t.LEFT)

	entry_file_name.pack(side=t.LEFT)
	entry_first_window.pack(side=t.LEFT)
	entry_last_window.pack(side=t.LEFT)
	button_predict.pack(side=t.LEFT)

	window.mainloop()


