# python openblas.py
import os
# use only 1 thread
os.environ['OPENBLAS_NUM_THREADS'] = '1'

# make sure the import is done after the environment variable is set
import numpy as np
import time

N = 8192
if __name__ == "__main__":
    FLOP = 2*N*N*N
    A = np.random.randn(N, N).astype(np.float32)
    B = np.random.randn(N, N).astype(np.float32)

    for _ in range(1):
        start = time.monotonic()
        C = A @ B
        end = time.monotonic()
        exec_time = end - start
        FLOPS = FLOP/exec_time
        GFLOPS = FLOPS*1e-9
        print(f"GFLOP/S: {GFLOPS}")

    # np.savetxt('matrix.csv', B, delimiter=',', fmt='%.2f')

    # # store A, B and result for verification
    try:
        with open("/tmp/gemm", "wb") as f:
            f.write(A.data)
            f.write(B.data)
            f.write(C.data)
    except:
        print("did not save properly")
