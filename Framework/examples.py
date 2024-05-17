from generators import *
import time

# print(RandomVariateGenerator([0.1306, 0.0422, 0.6579, 0.7965]).Exponential(1))
# print(RandomVariateGenerator([0.23, 0.75, 0.44]).Uniform(3, 8))

# print(LCM(27, 17, 43, 100).generate())

# for i in range(26, 32):
start_time = time.time()
print(LCM.generate(27, 17, 43, 100))
end_time = time.time()
print(f"{end_time - start_time:.2f} seconds")

# maximum density -> very large m (2**31 - 1)
# maximum period -> proper choice of a, c, m, X0

# print(CLCG(2).generate(40014, 2_147_483_563, 20692, 2_147_483_399))
