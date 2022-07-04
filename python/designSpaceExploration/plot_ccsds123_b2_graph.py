import matplotlib.pyplot as plt

def plot_ccsds_graph():
	ccsds123_graph = [[0,1], [128,0.9], [256, 0.1], [1024, 0]]
	x = [0,128,256, 1024]
	y = [1,0.9,0.1,0]

	plt.figure(4, figsize=(7,4), tight_layout=True)
	plt.plot(x, y, color="grey")
	#plt.savefig("ccsds123_b2_graph.png")
	plt.show()

plot_ccsds_graph()