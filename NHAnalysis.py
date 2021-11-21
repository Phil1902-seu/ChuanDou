import openseespy.opensees as ops

# 添加动力时程
record = 'Elcentro.txt'
dt = 0.02
factorList = [0.07,0.20,0.44]
PathID = 1
for factor in factorList:    
    PathID += 1
    ops.timeSeries('Path',PathID,'-filePath',record,'-dt',dt,'-factor',factor)
    ops.pattern('UniformExcitation',  PathID,   1,  '-accel', PathID)

    ops.constraints('Transformation')
    ops.system('UmfPack')
    ops.test('EnergyIncr', 1.0e-16,  20,2 )
    ops.algorithm('Newton')
    ops.numberer('RCM')
    ops.integrator('Newmark',  0.5,  0.25 )
    ops.analysis('Transient')
# 动力分析
    ops.analyze(1500,0.02)
    ops.loadConst('-time', 0.0)
    ops.wipeAnalysis()