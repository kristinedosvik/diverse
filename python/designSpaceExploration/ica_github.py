import numpy as np

def fastIca(signals,  alpha = 1, thresh=1e-8, iterations=5000):
    m, n = signals.shape

    # Initialize random weights
    W = np.random.rand(m, m)

    for c in range(m):
            w = W[c, :].copy().reshape(m, 1)
            w = w / np.sqrt((w ** 2).sum())

            i = 0
            lim = 100
            while ((lim > thresh) & (i < iterations)):

                # Dot product of weight and signal
                if(i == 0 and c == 0):
                    print("\nw.T and signals = \n", w.T, "\n", signals)
                ws = np.dot(w.T, signals)
                if(i == 0 and c == 0):
                    print("\nws = \n", ws)

                # Pass w*s into contrast function g
                wg = np.tanh(ws * alpha).T
                if(i == 0 and c == 0):
                    print("\nwg = \n", wg)
                    

                # Pass w*s into g prime
                wg_ = (1 - np.square(np.tanh(ws))) * alpha
                if(i == 0 and c == 0):
                    print("\nwg_ = \n", wg_)
                    

                # Update weights
                wNew = (signals * wg.T).mean(axis=1) - wg_.mean() * w.squeeze()
                if(i == 0 and c == 0):
                    print("\nsignals*wg.T = \n", signals*wg.T)
                    print("\n(signals*wg.T).mean = \n", (signals*wg.T).mean(axis=1))
                    print("\nwg_.mean*w.squeeze = \nm): ", wg_.mean(), "\ns) ", w.squeeze(), "\nt) ", wg_.mean()*w.squeeze())
                    print("\nwNew = \n", wNew)
                    

                # Decorrelate weights
                if(i == 0 and c == 0):
                    print("np.dot ... ")
                    print(np.dot(wNew, W[:c].T))
                wNew = wNew - np.dot(np.dot(wNew, W[:c].T), W[:c])
                if(i == 0 and c == 0):
                    print("wNew: np.dot ... ")
                    print("\nwNew = \n", wNew)
                    

                wNew = wNew / np.sqrt((wNew ** 2).sum())

                # Calculate limit condition
                lim = np.abs(np.abs((wNew * w).sum()) - 1)

                # Update weights
                w = wNew
                if(i == 0 and c == 0):
                    print("\nw = \n", w)
                    

                # Update counter
                i += 1

            W[c, :] = w.T
    return W

signals = np.array([[1,2,3,4],
        [5,7,1,5],
        [6,3,8,6],
        [4,2,6,4],
        [1,0,0,8],
        [6,1,7,2]])


print("signals = \n", signals)
W = fastIca(signals)
print("\nW = ", W)

