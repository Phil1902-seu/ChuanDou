import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt
from model import *

# 添加动力时程
record = 'GMfiles/Elcentro_NS.txt'
data = np.loadtxt(record)
dt = 0.02
nPts = len(data)
iGMFactor = 0.07
ops.timeSeries('Path', 2, '-filePath', record, '-dt', dt, '-factor', iGMFactor)
ops.pattern('UniformExcitation', 2, 1, '-accel', 2)
ops.constraints('Transformation')
ops.system('UmfPack')
# ops.test('NormDispIncr', 1.0e-6, 10)
# ops.algorithm('Newton')
ops.numberer('RCM')
# ops.integrator('Newmark', 0.5, 0.25)
# ops.analysis('Transient')


tCurrent = ops.getTime()


# Perform the transient analysis
test = {1: 'NormDispIncr', 2: 'RelativeEnergyIncr', 3: 'EnergyIncr', 4: 'RelativeNormUnbalance',
        5: 'RelativeNormDispIncr', 6: 'NormUnbalance'}
algorithm = {1: 'KrylovNewton', 2: 'SecantNewton', 3: 'ModifiedNewton', 4: 'RaphsonNewton',
             5: 'PeriodicNewton', 6: 'BFGS', 7: 'Broyden', 8: 'NewtonLineSearch'}
tFinal = nPts * dt
time = [tCurrent]
u2 = [0.0]
a2 = [0.0]
ok = 0
Tol = 1.0e-6
maxNumIter = 100

while tCurrent < tFinal:
    for i in test:
        for j in algorithm:
            if j < 4:
                ops.algorithm(algorithm[j], '-initial')

            else:
                ops.algorithm(algorithm[j])
            while ok == 0 and tCurrent < tFinal:

                ops.test(test[i], Tol, maxNumIter)
                NewmarkGamma = 0.5
                NewmarkBeta = 0.25
                ops.integrator('Newmark', NewmarkGamma, NewmarkBeta)
                ops.analysis('Transient')
                ok = ops.analyze(1, dt)

                if ok == 0:
                    tCurrent = ops.getTime()
                    time.append(tCurrent)
                    u2.append(ops.nodeDisp(2, 1))
                    a2.append(ops.nodeAccel(2, 1))
                    print(test[i], algorithm[j], 'tCurrent=', tCurrent)


plt.figure(figsize=(8,8))
plt.plot(time, u2)
plt.ylabel('Horizontal Displacement of node 2 (mm)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Disp at Node 2 vs time-uniform excitation-acctime.jpeg', dpi = 500)
plt.show()

plt.figure(figsize=(8,8))
plt.plot(time, a2)
plt.ylabel('Horizontal Acceleration of node 2 (mm/s2)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Accel at Node 2 vs time-uniform excitation-acctime.jpeg', dpi = 500)
plt.show()
# factorList = [0.07, 0.20, 0.44]
# PathID = 1
# for factor in factorList:
#     PathID += 1
#     ops.timeSeries('Path', PathID, '-filePath', record, '-dt', dt, '-factor', factor)
#     ops.pattern('UniformExcitation', PathID, 1, '-accel', PathID)
#
#     ops.constraints('Transformation')
#     ops.system('UmfPack')
#     ops.test('EnergyIncr', 1.0e-16, 20, 2)
#     ops.algorithm('Newton')
#     ops.numberer('RCM')
#     ops.integrator('Newmark', 0.5, 0.25)
#     ops.analysis('Transient')
#     # 动力分析
#     ops.analyze(nPts, dt)
#     ops.loadConst('-time', 0.0)
#     ops.wipeAnalysis()
