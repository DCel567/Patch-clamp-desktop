import data_cutting as cutting
import predictor as predicting
import tkinter as t

source_file = 'test_data.csv'


def draw_top_frame():

	def apply_source_file():
		source = text_source_file.get()
		global source_file

		if source != '':
			source_file = source

	topFrame = t.Frame(window, padx=10, pady=10)
	label_source_file = t.Label(topFrame, text='Введите полный путь к файлу: ')
	text_source_file = t.StringVar()
	entry_source_file = t.Entry(topFrame, textvariable=text_source_file, width=40)
	button_save_source_file_name = t.Button(topFrame, text='Использовать этот файл', command=apply_source_file)

	topFrame.pack()
	label_source_file.pack(side=t.LEFT)
	entry_source_file.pack(side=t.LEFT)
	button_save_source_file_name.pack(side=t.LEFT)


def draw_mid_frame():
	def cut_intervals():
		print(source_file)
		first_points = 0
		last_points = 100000

		first = text_first_points.get()
		if first.isdigit():
			first_points = int(first)

		second = text_last_points.get()
		if second.isdigit():
			last_points = int(second)

		print(first_points, last_points)

		cutting.start_cutting(source_file, first_points, last_points)

	midFrame = t.Frame(window, padx=10, pady=10)

	text_first_points = t.StringVar()
	text_last_points = t.StringVar()

	label_first_intervals = t.Label(midFrame, text='Начальная точка парсинга: ')
	label_last_intervals = t.Label(midFrame, text='Последняя точка парсинга: ')

	entry_first_points = t.Entry(midFrame, textvariable=text_first_points, width=15)
	entry_last_points = t.Entry(midFrame, textvariable=text_last_points, width=15)
	button_cut = t.Button(midFrame, text='Разделить', command=cut_intervals)

	midFrame.pack()

	label_first_intervals.pack(side=t.LEFT)
	entry_first_points.pack(side=t.LEFT)
	label_last_intervals.pack(side=t.LEFT)
	entry_last_points.pack(side=t.LEFT)
	button_cut.pack(side=t.LEFT)


def draw_bottom_frame():
	def predict_interval():
		file_name = 'intervals/0.0001_6.5.csv'
		first_points = 0
		last_points = 100000

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

	bottomFrame = t.Frame(window, padx=10, pady=30)
	underBottomFrame = t.Frame(window, padx=10, pady=0)

	label_file_name = t.Label(bottomFrame, text='Имя файла для предсказания: ')
	label_first_window = t.Label(underBottomFrame, text='Начальная точка: ')
	label_last_window = t.Label(underBottomFrame, text='Конечная точка: ')

	text_file_name = t.StringVar()
	text_first_window = t.StringVar()
	text_last_window = t.StringVar()

	entry_file_name = t.Entry(bottomFrame, textvariable=text_file_name, width=30)

	entry_first_window = t.Entry(underBottomFrame, textvariable=text_first_window, width=15)
	entry_last_window = t.Entry(underBottomFrame, textvariable=text_last_window, width=15)
	button_predict = t.Button(underBottomFrame, text='Рассчитать', command=predict_interval)

	bottomFrame.pack()
	underBottomFrame.pack()

	label_file_name.pack(side=t.LEFT)
	entry_file_name.pack(side=t.LEFT)

	label_first_window.pack(side=t.LEFT)
	entry_first_window.pack(side=t.LEFT)
	label_last_window.pack(side=t.LEFT)
	entry_last_window.pack(side=t.LEFT)
	button_predict.pack(side=t.LEFT)


if __name__ == "__main__":
	window = t.Tk()
	window.title('Patch-clamp desktop')
	window.geometry('700x300')

	draw_top_frame()
	draw_mid_frame()
	draw_bottom_frame()

	window.mainloop()
