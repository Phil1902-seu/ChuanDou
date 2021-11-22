##################################################################
##
##################################################################

import openseespy.postprocessing.Get_Rendering as opsplt
import openseespy.opensees as ops
import math as math
import os
import numpy as np
import pandas as pd

# Create ModelBuilder
ops.wipe()
ops.model('Basic', '-ndm', 3, '-ndf', 6)
DataDir = r'DataOut'
if not os.path.exists(DataDir):
    os.makedirs(DataDir)  # 创建结果输出目录

# ---------------------------------木框架建模-----------------------------------------
# Create nodes
# 模型质量集中至柱顶
# 1轴山墙
# 柱端节点
ops.node(1, 0, 0, 0)
ops.node(2, 0, 0, 1500)
ops.node(3, 0, 600, 1387.5)
ops.node(4, 0, 600, 1800)
ops.node(5, 0, 1200, 0)
ops.node(6, 0, 1200, 2100)
ops.node(7, 0, 1800, 1387.5)
ops.node(8, 0, 1800, 1800)
ops.node(9, 0, 2400, 0)
ops.node(10, 0, 2400, 1500)
# 斗枋节点
ops.node(11, 0, 0, 1275)
ops.node(12, 0, 2400, 1275)
# 穿枋节点
ops.node(13, 0, 0, 1387.5)
ops.node(14, 0, 1200, 1387.5)
ops.node(15, 0, 2400, 1387.5)
ops.node(16, 0, 600, 1687.5)
ops.node(17, 0, 1200, 1687.5)
ops.node(18, 0, 1800, 1687.5)
# 2轴隔墙
# 柱端节点
ops.node(19, 1650, 0, 0)
ops.node(20, 1650, 0, 1500)
ops.node(21, 1650, 600, 1387.5)
ops.node(22, 1650, 600, 1800)
ops.node(23, 1650, 1200, 0)
ops.node(24, 1650, 1200, 2100)
ops.node(25, 1650, 1800, 1387.5)
ops.node(26, 1650, 1800, 1800)
ops.node(27, 1650, 2400, 0)
ops.node(28, 1650, 2400, 1500)
# 斗枋节点
ops.node(29, 1650, 0, 1275)
ops.node(30, 1650, 2400, 1275)
# 穿枋节点
ops.node(31, 1650, 0, 1387.5)
ops.node(32, 1650, 1200, 1387.5)
ops.node(33, 1650, 2400, 1387.5)
ops.node(34, 1650, 600, 1687.5)
ops.node(35, 1650, 1200, 1687.5)
ops.node(36, 1650, 1800, 1687.5)
# 3轴隔墙
# 柱端节点
ops.node(37, 3450, 0, 0)
ops.node(38, 3450, 0, 1500)
ops.node(39, 3450, 600, 1387.5)
ops.node(40, 3450, 600, 1800)
ops.node(41, 3450, 1200, 0)
ops.node(42, 3450, 1200, 2100)
ops.node(43, 3450, 1800, 1387.5)
ops.node(44, 3450, 1800, 1800)
ops.node(45, 3450, 2400, 0)
ops.node(46, 3450, 2400, 1500)
# 斗枋节点
ops.node(47, 3450, 0, 1275)
ops.node(48, 3450, 2400, 1275)
# 穿枋节点
ops.node(49, 3450, 0, 1387.5)
ops.node(50, 3450, 1200, 1387.5)
ops.node(51, 3450, 2400, 1387.5)
ops.node(52, 3450, 600, 1687.5)
ops.node(53, 3450, 1200, 1687.5)
ops.node(54, 3450, 1800, 1687.5)
# 4轴山墙
# 柱端节点
ops.node(55, 5100, 0, 0)
ops.node(56, 5100, 0, 1500)
ops.node(57, 5100, 600, 1387.5)
ops.node(58, 5100, 600, 1800)
ops.node(59, 5100, 1200, 0)
ops.node(60, 5100, 1200, 2100)
ops.node(61, 5100, 1800, 1387.5)
ops.node(62, 5100, 1800, 1800)
ops.node(63, 5100, 2400, 0)
ops.node(64, 5100, 2400, 1500)
# 斗枋节点
ops.node(65, 5100, 0, 1275)
ops.node(66, 5100, 2400, 1275)
# 穿枋节点
ops.node(67, 5100, 0, 1387.5)
ops.node(68, 5100, 1200, 1387.5)
ops.node(69, 5100, 2400, 1387.5)
ops.node(70, 5100, 600, 1687.5)
ops.node(71, 5100, 1200, 1687.5)
ops.node(72, 5100, 1800, 1687.5)

print("OK！，木框架节点")

# 边界条件 浮搁柱脚
# 滑动平板支撑单元
# 固支点
ops.node(1000001, 0, 0, 0)
ops.node(1000005, 0, 1200, 0)
ops.node(1000009, 0, 2400, 0)
ops.node(10000019, 1650, 0, 0)
ops.node(10000023, 1650, 1200, 0)
ops.node(10000027, 1650, 2400, 0)
ops.node(10000037, 3450, 0, 0)
ops.node(10000041, 3450, 1200, 0)
ops.node(10000045, 3450, 2400, 0)
ops.node(10000055, 5100, 0, 0)
ops.node(10000059, 5100, 1200, 0)
ops.node(10000063, 5100, 2400, 0)
ops.fix(1000001, 1, 1, 1, 1, 1, 1)
ops.fix(1000005, 1, 1, 1, 1, 1, 1)
ops.fix(1000009, 1, 1, 1, 1, 1, 1)
ops.fix(10000019, 1, 1, 1, 1, 1, 1)
ops.fix(10000023, 1, 1, 1, 1, 1, 1)
ops.fix(10000027, 1, 1, 1, 1, 1, 1)
ops.fix(10000037, 1, 1, 1, 1, 1, 1)
ops.fix(10000041, 1, 1, 1, 1, 1, 1)
ops.fix(10000045, 1, 1, 1, 1, 1, 1)
ops.fix(10000055, 1, 1, 1, 1, 1, 1)
ops.fix(10000059, 1, 1, 1, 1, 1, 1)
ops.fix(10000063, 1, 1, 1, 1, 1, 1)

ops.frictionModel('Coulomb', 1, 0.33)  # 库伦摩擦模型  薛建阳
kInit = 164  # 薛建阳
PMatTag = 1000001  # 释放抬升自由度
ops.uniaxialMaterial('ENT', PMatTag, 1.0E10)
TMatTag = 1000002  # 刚接
ops.uniaxialMaterial('Elastic', TMatTag, 1.0E14)
MyMatTag = 1000003  # 铰接
ops.uniaxialMaterial('Elastic', MyMatTag, 1.0)
MzMatTag = 1000004  # 铰接
ops.uniaxialMaterial('Elastic', MzMatTag, 1.0)


ops.element('flatSliderBearing', 1000001, 1000001, 1, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 1000005, 1000005, 5, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 1000009, 1000009, 9, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000019, 10000019, 19, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000023, 10000023, 23, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000027, 10000027, 27, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000037, 10000037, 37, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000041, 10000041, 41, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000045, 10000045, 45, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000055, 10000055, 55, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000059, 10000059, 59, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('flatSliderBearing', 10000063, 10000063, 63, 1, kInit,
            '-P', PMatTag, '-T', TMatTag, '-My', MyMatTag, '-Mz', MzMatTag, '-orient', 0, 0, 1, 0, 1, 0)
print("OK！，柱脚模拟")

# 本构及构架截面
# 材料编号
WoodMaterialTag = 1
# 截面编号
ColSecTag = 1
BeamSecTag = 2
GirdSecTag = 3
# 杉木 理想弹塑性材料
ops.uniaxialMaterial('ElasticPP', WoodMaterialTag, 11612, 0.006, -0.006)
# Define cross-section for nonlinear elements
# 柱
ops.section('Fiber', ColSecTag, '-GJ', 1E14)
ops.patch('circ', 1, 20, 5, 0., 0., 0., 65., 0., 360.)
# 檩
ops.section('Fiber', BeamSecTag, '-GJ', 1E14)
ops.patch('circ', 1, 20, 5, 0., 0., 0., 50., 0., 360.)
# 枋
ops.section('Fiber', GirdSecTag, '-GJ', 1E14)
ops.patch('rect', 1, 5, 5, -30, -37.5, 30, 37.5)

# Define column elements
ops.geomTransf('Linear', 1, 1, 0, 0)  # 柱
ops.geomTransf('Linear', 2, 0, 0, 1)  # 枋
ops.geomTransf('Linear', 3, 0, 0, 1)  # 檩

ops.beamIntegration('Lobatto', 1, 1, 5)
ops.beamIntegration('Lobatto', 2, 2, 5)
ops.beamIntegration('Lobatto', 3, 3, 5)

frameType = 'dispBeamColumn'
# 柱
massCol = 0.486E-9 * math.pi * 65 ** 2
ops.element(frameType, 1, 1, 11, 1, 1, '-mass', massCol)
ops.element(frameType, 2, 11, 13, 1, 1, '-mass', massCol)
ops.element(frameType, 3, 13, 2, 1, 1, '-mass', massCol)
ops.element(frameType, 4, 3, 16, 1, 1, '-mass', massCol)
ops.element(frameType, 5, 16, 4, 1, 1, '-mass', massCol)
ops.element(frameType, 6, 5, 14, 1, 1, '-mass', massCol)
ops.element(frameType, 7, 14, 17, 1, 1, '-mass', massCol)
ops.element(frameType, 8, 17, 6, 1, 1, '-mass', massCol)
ops.element(frameType, 9, 7, 18, 1, 1, '-mass', massCol)
ops.element(frameType, 10, 18, 8, 1, 1, '-mass', massCol)
ops.element(frameType, 11, 9, 12, 1, 1, '-mass', massCol)
ops.element(frameType, 12, 12, 15, 1, 1, '-mass', massCol)
ops.element(frameType, 13, 15, 10, 1, 1, '-mass', massCol)
ops.element(frameType, 14, 19, 29, 1, 1, '-mass', massCol)
ops.element(frameType, 15, 29, 31, 1, 1, '-mass', massCol)
ops.element(frameType, 16, 31, 20, 1, 1, '-mass', massCol)
ops.element(frameType, 17, 21, 34, 1, 1, '-mass', massCol)
ops.element(frameType, 18, 34, 22, 1, 1, '-mass', massCol)
ops.element(frameType, 19, 23, 32, 1, 1, '-mass', massCol)
ops.element(frameType, 20, 32, 35, 1, 1, '-mass', massCol)
ops.element(frameType, 21, 35, 24, 1, 1, '-mass', massCol)
ops.element(frameType, 22, 25, 36, 1, 1, '-mass', massCol)
ops.element(frameType, 23, 36, 26, 1, 1, '-mass', massCol)
ops.element(frameType, 24, 27, 30, 1, 1, '-mass', massCol)
ops.element(frameType, 25, 30, 33, 1, 1, '-mass', massCol)
ops.element(frameType, 26, 33, 28, 1, 1, '-mass', massCol)
ops.element(frameType, 27, 27, 30, 1, 1, '-mass', massCol)
ops.element(frameType, 28, 37, 47, 1, 1, '-mass', massCol)
ops.element(frameType, 29, 47, 49, 1, 1, '-mass', massCol)
ops.element(frameType, 30, 49, 38, 1, 1, '-mass', massCol)
ops.element(frameType, 31, 39, 52, 1, 1, '-mass', massCol)
ops.element(frameType, 32, 52, 40, 1, 1, '-mass', massCol)
ops.element(frameType, 33, 41, 50, 1, 1, '-mass', massCol)
ops.element(frameType, 34, 50, 53, 1, 1, '-mass', massCol)
ops.element(frameType, 35, 53, 42, 1, 1, '-mass', massCol)
ops.element(frameType, 36, 43, 54, 1, 1, '-mass', massCol)
ops.element(frameType, 37, 54, 44, 1, 1, '-mass', massCol)
ops.element(frameType, 38, 45, 48, 1, 1, '-mass', massCol)
ops.element(frameType, 39, 48, 51, 1, 1, '-mass', massCol)
ops.element(frameType, 40, 51, 46, 1, 1, '-mass', massCol)
ops.element(frameType, 41, 55, 65, 1, 1, '-mass', massCol)
ops.element(frameType, 42, 65, 67, 1, 1, '-mass', massCol)
ops.element(frameType, 43, 67, 56, 1, 1, '-mass', massCol)
ops.element(frameType, 44, 57, 70, 1, 1, '-mass', massCol)
ops.element(frameType, 45, 70, 58, 1, 1, '-mass', massCol)
ops.element(frameType, 46, 59, 68, 1, 1, '-mass', massCol)
ops.element(frameType, 47, 68, 71, 1, 1, '-mass', massCol)
ops.element(frameType, 48, 71, 60, 1, 1, '-mass', massCol)
ops.element(frameType, 49, 61, 72, 1, 1, '-mass', massCol)
ops.element(frameType, 50, 72, 62, 1, 1, '-mass', massCol)
ops.element(frameType, 51, 63, 66, 1, 1, '-mass', massCol)
ops.element(frameType, 52, 66, 69, 1, 1, '-mass', massCol)
ops.element(frameType, 53, 69, 64, 1, 1, '-mass', massCol)
# 斗枋
massFang = 0.486E-9 * 60 * 70
ops.element(frameType, 54, 11, 29, 3, 3, '-mass', massFang)
ops.element(frameType, 55, 12, 30, 3, 3, '-mass', massFang)
ops.element(frameType, 56, 29, 47, 3, 3, '-mass', massFang)
ops.element(frameType, 57, 30, 48, 3, 3, '-mass', massFang)
ops.element(frameType, 58, 47, 65, 3, 3, '-mass', massFang)
ops.element(frameType, 59, 48, 66, 3, 3, '-mass', massFang)
# 穿枋
ops.element(frameType, 60, 13, 14, 2, 3, '-mass', massFang)
ops.element(frameType, 61, 14, 15, 2, 3, '-mass', massFang)
ops.element(frameType, 62, 16, 17, 2, 3, '-mass', massFang)
ops.element(frameType, 63, 17, 18, 2, 3, '-mass', massFang)
ops.element(frameType, 64, 31, 32, 2, 3, '-mass', massFang)
ops.element(frameType, 65, 32, 33, 2, 3, '-mass', massFang)
ops.element(frameType, 66, 34, 35, 2, 3, '-mass', massFang)
ops.element(frameType, 67, 35, 36, 2, 3, '-mass', massFang)
ops.element(frameType, 68, 49, 50, 2, 3, '-mass', massFang)
ops.element(frameType, 69, 50, 51, 2, 3, '-mass', massFang)
ops.element(frameType, 70, 52, 53, 2, 3, '-mass', massFang)
ops.element(frameType, 71, 53, 54, 2, 3, '-mass', massFang)
ops.element(frameType, 72, 67, 68, 2, 3, '-mass', massFang)
ops.element(frameType, 73, 68, 69, 2, 3, '-mass', massFang)
ops.element(frameType, 74, 70, 71, 2, 3, '-mass', massFang)
ops.element(frameType, 75, 71, 72, 2, 3, '-mass', massFang)
# 檩条
massLing = 0.486E-9 * math.pi * 50 ** 2
ops.element(frameType, 76, 2, 20, 3, 2, '-mass', massLing)
ops.element(frameType, 77, 4, 22, 3, 2, '-mass', massLing)
ops.element(frameType, 78, 6, 24, 3, 2, '-mass', massLing)
ops.element(frameType, 79, 8, 26, 3, 2, '-mass', massLing)
ops.element(frameType, 80, 10, 28, 3, 2, '-mass', massLing)
ops.element(frameType, 81, 20, 38, 3, 2, '-mass', massLing)
ops.element(frameType, 82, 22, 40, 3, 2, '-mass', massLing)
ops.element(frameType, 83, 24, 42, 3, 2, '-mass', massLing)
ops.element(frameType, 84, 26, 44, 3, 2, '-mass', massLing)
ops.element(frameType, 85, 28, 46, 3, 2, '-mass', massLing)
ops.element(frameType, 86, 38, 56, 3, 2, '-mass', massLing)
ops.element(frameType, 87, 40, 58, 3, 2, '-mass', massLing)
ops.element(frameType, 88, 42, 60, 3, 2, '-mass', massLing)
ops.element(frameType, 89, 44, 62, 3, 2, '-mass', massLing)
ops.element(frameType, 90, 46, 64, 3, 2, '-mass', massLing)

print("OK！，木框架梁柱单元")

# ------------------------------------砌体墙建模--------------------------------------
# 填充墙面外质点
density = 1.8e-9  # 砌体面密度： 密度 1.8e-9 t/mm3
# 1轴山墙
m1 = 1350 * 1170 * density * 110
m2 = 225 * 470 * density * 110
ops.node(1001, 0, 600, 1387.5 / 2, '-mass', 0, 0.81 * m1, 0, 0, 0, 0)
ops.node(1002, 0, 1800, 1387.5 / 2, '-mass', 0, 0.81 * m1, 0, 0, 0, 0)
ops.node(1003, 0, 900, 1387.5 + 150, '-mass', 0, 0.81 * m2, 0, 0, 0, 0)
ops.node(1004, 0, 1500, 1387.5 + 150, '-mass', 0, 0.81 * m2, 0, 0, 0, 0)
# 2轴隔墙
m3 = 1350 * 1170 * density * 60
m4 = 0.7 * 1350 * 1170 * density * 60
m5 = 225 * 470 * density * 60
ops.node(2001, 1650, 600, 1387.5 / 2, '-mass', 0, 0.81 * m3, 0, 0, 0, 0)
ops.node(2002, 1650, 1800, 1387.5 / 2, '-mass', 0, 0.81 * m4, 0, 0, 0, 0)
ops.node(2003, 1650, 900, 1387.5 + 150, '-mass', 0, 0.81 * m5, 0, 0, 0, 0)
ops.node(2004, 1650, 1500, 1387.5 + 150, '-mass', 0, 0.81 * m5, 0, 0, 0, 0)
# 3轴隔墙
ops.node(3001, 3450, 600, 1387.5 / 2, '-mass', 0, 0.81 * m3, 0, 0, 0, 0)
ops.node(3002, 3450, 1800, 1387.5 / 2, '-mass', 0, 0.81 * m4, 0, 0, 0, 0)
ops.node(3003, 3450, 900, 1387.5 + 150, '-mass', 0, 0.81 * m5, 0, 0, 0, 0)
ops.node(3004, 3450, 1500, 1387.5 + 150, '-mass', 0, 0.81 * m5, 0, 0, 0, 0)
# 4轴山墙
ops.node(4001, 5100, 600, 1387.5 / 2, '-mass', 0, 0.81 * m1, 0, 0, 0, 0)
ops.node(4002, 5100, 1800, 1387.5 / 2, '-mass', 0, 0.81 * m1, 0, 0, 0, 0)
ops.node(4003, 5100, 900, 1387.5 + 150, '-mass', 0, 0.81 * m2, 0, 0, 0, 0)
ops.node(4004, 5100, 1500, 1387.5 + 150, '-mass', 0, 0.81 * m2, 0, 0, 0, 0)
# A轴纵墙
m6 = 0.75 * 1200 * 1550 * density * 110
m7 = 1200 * 1700 * density * 110
m8 = 175 * 1550 * density * 110
m9 = 175 * 1700 * density * 110
ops.node(5001, 1650 / 2, 0, 1275 / 2, '-mass', 0.81 * m6, 0, 0, 0, 0, 0)
ops.node(5002, 1650 / 2, 0, 1365, '-mass', 0.81 * 0.53 * m8, 0, 0, 0, 0, 0)
# ops.node(5003, 1650+900, 0, 1275/2, m7 * 0.53)
ops.node(5004, 1650 + 900, 0, 1365, '-mass', 0.81 * m9, 0, 0, 0, 0, 0)
ops.node(5005, 1650 + 1800 + 1650 / 2, 0, 1275 / 2, '-mass', 0.81 * m6, 0, 0, 0, 0, 0)
ops.node(5006, 1650 + 1800 + 1650 / 2, 0, 1365, '-mass', 0.81 * m8, 0, 0, 0, 0, 0)
# C轴纵墙
ops.node(6001, 1650 / 2, 2400, 1275 / 2, '-mass', 0.81 * m6, 0, 0, 0, 0, 0)
ops.node(6002, 1650 / 2, 2400, 1365, '-mass', 0.81 * m8, 0, 0, 0, 0, 0)
ops.node(6003, 1650 + 900, 2400, 1275 / 2, '-mass', 0.81 * m7, 0, 0, 0, 0, 0)
ops.node(6004, 1650 + 900, 2400, 1365, '-mass', 0.81 * m9, 0, 0, 0, 0, 0)
ops.node(6005, 1650 + 1800 + 1650 / 2, 2400, 1275 / 2, '-mass', 0.81 * m6, 0, 0, 0, 0, 0)
ops.node(6006, 1650 + 1800 + 1650 / 2, 2400, 1365, '-mass', 0.81 * m8, 0, 0, 0, 0, 0)

print("OK！，填充墙面外质点")

# 填充墙等效杆截面

Eminfm = 3674.216  # 砌体弹性模量
IDYMaterial = 10000  # 虚拟Y向纤维本构编号
ops.uniaxialMaterial('Steel01', IDYMaterial, 1.e40, Eminfm, 0.02)
# 1轴山墙
# 1轴山墙墙片1 编号1001
rinfM_1001 = 1786.45

sectioninf_1001 = 10011  # 塑性铰
infmattag_1001 = list(range(11, 21))  # [11,12,...,20]
fyfibinf_1001 = [83.303131, 0.490160, 0.032194, 0.002515, 0.000015,
                 0.000015, 0.002515, 0.032194, 0.490160, 83.303131]
areafibinf_1001 = [0.000228, 0.074349, 1.598936, 28.275665, 8790.407495,
                   8790.407495, 28.275665, 1.598936, 0.074349, 0.000228]
zfibinf_1001 = [1237.770003, 645.292096, 456.841060, 330.627391, 173.290680,
                -173.290680, -330.627391, -456.841060, -645.292096, -1237.770003]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_1001[i], fyfibinf_1001[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_1001, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_1001[i], areafibinf_1001[i], infmattag_1001[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_1001 = 10012  # 弹性铰
AreainfM_1001 = sum(areafibinf_1001)
ops.section('Elastic', sectionpin_1001, Eminfm, AreainfM_1001, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_1001 = 10013  # 内部弹性截面
InertiainfM_1001 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_1001, Eminfm, AreainfM_1001, 1e-5, InertiainfM_1001, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 1001, 0, 1, 0)
ops.beamIntegration('HingeRadau', 1001, sectioninf_1001, rinfM_1001 * 0.1, sectionpin_1001, rinfM_1001 * 0.05,
                    sectioninterior_1001)
eleType = 'forceBeamColumn'
ops.element(eleType, 10011, 1001, 1, 1001, 1001)
ops.element(eleType, 10012, 1001, 14, 1001, 1001)

# 4轴山墙墙片1 编号 4001
ops.element(eleType, 40011, 4001, 55, 1001, 1001)
ops.element(eleType, 40012, 4001, 68, 1001, 1001)

# 1轴山墙墙片2 编号1002
rinfM_1002 = 1786.45
sectioninf_1002 = 10021  # 塑性铰
infmattag_1002 = list(range(21, 31))  # [21,12,...,30]
fyfibinf_1002 = [83.303131, 0.490160, 0.032194, 0.002515, 0.000015,
                 0.000015, 0.002515, 0.032194, 0.490160, 83.303131]
areafibinf_1002 = [0.000228, 0.074349, 1.598936, 28.275665, 8790.407495,
                   8790.407495, 28.275665, 1.598936, 0.074349, 0.000228]
zfibinf_1002 = [1237.770003, 645.292096, 456.841060, 330.627391, 173.290680,
                -173.290680, -330.627391, -456.841060, -645.292096, -1237.770003]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_1002[i], fyfibinf_1002[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_1002, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_1002[i], areafibinf_1002[i], infmattag_1002[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_1002 = 10022  # 弹性铰
AreainfM_1002 = sum(areafibinf_1002)
ops.section('Elastic', sectionpin_1002, Eminfm, AreainfM_1002, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_1002 = 10023  # 内部弹性截面
InertiainfM_1002 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_1002, Eminfm, AreainfM_1002, 1e-5, InertiainfM_1002, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 1002, 0, 1, 0)
ops.beamIntegration('HingeRadau', 1002, sectioninf_1002, rinfM_1002 * 0.1, sectionpin_1002, rinfM_1002 * 0.05,
                    sectioninterior_1002)
eleType = 'forceBeamColumn'
ops.element(eleType, 10021, 1002, 5, 1002, 1002)
ops.element(eleType, 10022, 1002, 15, 1002, 1002)

# 4轴山墙墙片2 编号 4002
ops.element(eleType, 40021, 4002, 59, 1002, 1002)
ops.element(eleType, 40022, 4002, 69, 1002, 1002)

# 1轴山墙墙片3 编号1003
rinfM_1003 = 521.08
sectioninf_1003 = 10031  # 塑性铰
infmattag_1003 = list(range(31, 41))  # [31,12,...,40]
fyfibinf_1003 = [0.000066, 0.000041, 0.000032, 0.000025, 0.000016,
                 0.000016, 0.000025, 0.000032, 0.000041, 0.000066]
areafibinf_1003 = [84.499520, 260.954281, 474.481972, 830.456393, 2541.035941,
                   2541.035941, 830.456393, 474.481972, 260.954281, 84.499520]
zfibinf_1003 = [1656.981142, 863.841289, 611.565170, 442.605129, 231.981214,
                -231.981214, -442.605129, -611.565170, -863.841289, 1656.981142]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_1003[i], fyfibinf_1003[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_1003, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_1003[i], areafibinf_1003[i], infmattag_1003[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_1003 = 10032  # 弹性铰
AreainfM_1003 = sum(areafibinf_1003)
ops.section('Elastic', sectionpin_1003, Eminfm, AreainfM_1003, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_1003 = 10033  # 内部弹性截面
InertiainfM_1003 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_1003, Eminfm, AreainfM_1003, 1e-5, InertiainfM_1003, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 1003, 0, 1, 0)
ops.beamIntegration('HingeRadau', 1003, sectioninf_1003, rinfM_1003 * 0.1, sectionpin_1003, rinfM_1003 * 0.05,
                    sectioninterior_1003)
eleType = 'forceBeamColumn'
ops.element(eleType, 10031, 1003, 3, 1003, 1003)
ops.element(eleType, 10032, 1003, 17, 1003, 1003)

# 4轴墙片3 编号 4003
ops.element(eleType, 40031, 4003, 57, 1003, 1003)
ops.element(eleType, 40032, 4003, 71, 1003, 1003)

# 1轴山墙墙片4 编号1004
rinfM_1004 = 521.08
sectioninf_1004 = 10041  # 塑性铰
infmattag_1004 = list(range(41, 51))  # [41,12,...,50]
fyfibinf_1004 = [0.000066, 0.000041, 0.000032, 0.000025, 0.000016,
                 0.000016, 0.000025, 0.000032, 0.000041, 0.000066]
areafibinf_1004 = [84.499520, 260.954281, 474.481972, 830.456393, 2541.035941,
                   2541.035941, 830.456393, 474.481972, 260.954281, 84.499520]
zfibinf_1004 = [1656.981142, 863.841289, 611.565170, 442.605129, 231.981214,
                -231.981214, -442.605129, -611.565170, -863.841289, 1656.981142]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_1004[i], fyfibinf_1004[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_1004, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_1004[i], areafibinf_1004[i], infmattag_1004[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_1004 = 10042  # 弹性铰
AreainfM_1004 = sum(areafibinf_1004)
ops.section('Elastic', sectionpin_1004, Eminfm, AreainfM_1004, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_1004 = 10043  # 内部弹性截面
InertiainfM_1004 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_1004, Eminfm, AreainfM_1004, 1e-5, InertiainfM_1004, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 1004, 0, 1, 0)
ops.beamIntegration('HingeRadau', 1004, sectioninf_1004, rinfM_1004 * 0.1, sectionpin_1004, rinfM_1004 * 0.05,
                    sectioninterior_1004)
eleType = 'forceBeamColumn'
ops.element(eleType, 10041, 1004, 14, 1004, 1004)
ops.element(eleType, 10042, 1004, 18, 1004, 1004)

# 4轴墙片4 编号 4004
ops.element(eleType, 40041, 4004, 68, 1004, 1004)
ops.element(eleType, 40042, 4004, 72, 1004, 1004)

# 2轴隔墙
# 2轴墙片1 编号2001
rinfM_2001 = 1786.45

sectioninf_2001 = 20011  # 塑性铰
infmattag_2001 = list(range(51, 61))
fyfibinf_2001 = [0.001245, 0.000292, 0.000136, 0.000066, 0.000016,
                 0.000016, 0.000066, 0.000136, 0.000292, 0.001245]
areafibinf_2001 = [8.335728, 68.092482, 207.369305, 588.230856, 4723.051242,
                   4723.051242, 588.230856, 207.369305, 68.092482, 8.335728]
zfibinf_2001 = [468.398119, 244.192058, 172.878235, 125.116336, 65.576826,
                -65.576826, -125.116336, -172.878235, -244.192058, -468.398119]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_2001[i], fyfibinf_2001[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_2001, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_2001[i], areafibinf_2001[i], infmattag_2001[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_2001 = 20012  # 弹性铰
AreainfM_2001 = sum(areafibinf_2001)
ops.section('Elastic', sectionpin_2001, Eminfm, AreainfM_2001, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_2001 = 20013  # 内部弹性截面
InertiainfM_2001 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_2001, Eminfm, AreainfM_2001, 1e-5, InertiainfM_2001, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 2001, 0, 1, 0)
ops.beamIntegration('HingeRadau', 2001, sectioninf_2001, rinfM_2001 * 0.1, sectionpin_2001, rinfM_2001 * 0.05,
                    sectioninterior_2001)
eleType = 'forceBeamColumn'
ops.element(eleType, 20011, 2001, 19, 2001, 2001)
ops.element(eleType, 20012, 2001, 32, 2001, 2001)

# 3轴墙片1 编号3001
ops.element(eleType, 30011, 3001, 37, 2001, 2001)
ops.element(eleType, 30012, 3001, 50, 2001, 2001)

# 2轴山墙墙片2 编号2002
rinfM_2002 = 1786.45
sectioninf_2002 = 20021  # 塑性铰
infmattag_2002 = list(range(61, 71))
fyfibinf_2002 = [0.000896, 0.000247, 0.000124, 0.000066, 0.000018,
                 0.000018, 0.000066, 0.000124, 0.000247, 0.000896]
areafibinf_2002 = [11.585358, 80.765535, 226.136887, 592.928546, 4068.204530,
                   4068.204530, 592.928546, 226.1366887, 80.765535, 11.585358]
zfibinf_2002 = [468.398119, 244.192058, 172.878235, 125.116336, 65.576826,
                -65.576826, -125.116336, -172.878235, -244.192058, -468.398119]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_2002[i], fyfibinf_2002[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_2002, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_2002[i], areafibinf_2002[i], infmattag_2002[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_2002 = 20022  # 弹性铰
AreainfM_2002 = sum(areafibinf_2002)
ops.section('Elastic', sectionpin_2002, Eminfm, AreainfM_2002, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_2002 = 20023  # 内部弹性截面
InertiainfM_2002 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_2002, Eminfm, AreainfM_2002, 1e-5, InertiainfM_2002, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 2002, 0, 1, 0)
ops.beamIntegration('HingeRadau', 2002, sectioninf_2002, rinfM_2002 * 0.1, sectionpin_2002, rinfM_2002 * 0.05,
                    sectioninterior_2002)
eleType = 'forceBeamColumn'
ops.element(eleType, 20021, 2002, 23, 2002, 2002)
ops.element(eleType, 20022, 2002, 33, 2002, 2002)

# 3轴墙片2 编号3002
ops.element(eleType, 30021, 3002, 41, 2002, 2002)
ops.element(eleType, 30022, 3002, 51, 2002, 2002)

# 2轴山墙墙片3 编号2003
rinfM_2003 = 521.08
sectioninf_2003 = 20031  # 塑性铰
infmattag_2003 = list(range(71, 81))
fyfibinf_2003 = [0.003216, 0.000474, 0.000172, 0.000066, 0.000010,
                 0.000010, 0.000066, 0.000172, 0.000474, 0.003216]
areafibinf_2003 = [0.947622, 12.342998, 48.139855, 172.145462, 2195.524977,
                   2195.524977, 172.145462, 48.139855, 12.342998, 0.947622]
zfibinf_2003 = [1656.981142, 863.841289, 611.565170, 442.605129, 231.981214,
                -231.981214, -442.605129, -611.565170, -863.841289, -1656.981142]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_2003[i], fyfibinf_2003[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_2003, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_2003[i], areafibinf_2003[i], infmattag_2003[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_2003 = 20032  # 弹性铰
AreainfM_2003 = sum(areafibinf_2003)
ops.section('Elastic', sectionpin_2003, Eminfm, AreainfM_2003, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_2003 = 20033  # 内部弹性截面
InertiainfM_2003 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_2003, Eminfm, AreainfM_2003, 1e-5, InertiainfM_2003, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 2003, 0, 1, 0)
ops.beamIntegration('HingeRadau', 2003, sectioninf_2003, rinfM_2003 * 0.1, sectionpin_2003, rinfM_2003 * 0.05,
                    sectioninterior_2003)
eleType = 'forceBeamColumn'
ops.element(eleType, 20031, 2003, 21, 2003, 2003)
ops.element(eleType, 20032, 2003, 35, 2003, 2003)

# 3轴墙片3 编号3003
ops.element(eleType, 30031, 3003, 39, 2003, 2003)
ops.element(eleType, 30032, 3003, 53, 2003, 2003)

# 2轴山墙墙片4 编号2004
rinfM_2004 = 521.08
sectioninf_2004 = 20041  # 塑性铰
infmattag_2004 = list(range(81, 91))  # [41,12,...,50]
fyfibinf_2004 = [0.003216, 0.000474, 0.000172, 0.000066, 0.000010,
                 0.000010, 0.000066, 0.000172, 0.000474, 0.003216]
areafibinf_2004 = [0.947622, 12.342998, 48.139855, 172.145462, 2195.524977,
                   2195.524977, 172.145462, 48.139855, 12.342998, 0.947622]
zfibinf_2004 = [1656.981142, 863.841289, 611.565170, 442.605129, 231.981214,
                -231.981214, -442.605129, -611.565170, -863.841289, -1656.981142]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_2004[i], fyfibinf_2004[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_2004, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_2004[i], areafibinf_2004[i], infmattag_2004[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_2004 = 20042  # 弹性铰
AreainfM_2004 = sum(areafibinf_2004)
ops.section('Elastic', sectionpin_2004, Eminfm, AreainfM_2004, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_2004 = 20043  # 内部弹性截面
InertiainfM_2004 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_2004, Eminfm, AreainfM_2004, 1e-5, InertiainfM_2004, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 2004, 0, 1, 0)
ops.beamIntegration('HingeRadau', 2004, sectioninf_2004, rinfM_2004 * 0.1, sectionpin_2004, rinfM_2004 * 0.05,
                    sectioninterior_2004)
eleType = 'forceBeamColumn'
ops.element(eleType, 20041, 2004, 32, 2004, 2004)
ops.element(eleType, 20042, 2004, 36, 2004, 2004)

# 3轴墙片4 编号3004
ops.element(eleType, 30041, 3004, 50, 2004, 2004)
ops.element(eleType, 30042, 3004, 54, 2004, 2004)

# A轴纵墙
# A轴墙片 1 编号5001
rinfM_5001 = 1960.23
sectioninf_5001 = 50011  # 塑性铰
infmattag_5001 = list(range(91, 101))
fyfibinf_5001 = [0.276024, 0.011088, 0.002016, 0.0000409, 0.000017,
                 0.000017, 0.000409, 0.002016, 0.011088, 0.276024]
areafibinf_5001 = [0.074217, 3.544047, 27.525862, 187.590936, 8678.377122,
                   8678.377122, 187.590936, 27.525862, 3.544047, 0.074217]
zfibinf_5001 = [1986.087850, 1035.415941, 733.033178, 530.514589, 278.056919,
                -278.056919, -530.514589, -733.033178, -1035.415941, -1986.087850]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_5001[i], fyfibinf_5001[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_5001, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_5001[i], areafibinf_5001[i], infmattag_5001[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_5001 = 50012  # 弹性铰
AreainfM_5001 = sum(areafibinf_5001)
ops.section('Elastic', sectionpin_5001, Eminfm, AreainfM_5001, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_5001 = 50053  # 内部弹性截面
InertiainfM_5001 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_5001, Eminfm, AreainfM_5001, 1e-5, InertiainfM_5001, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 5001, 1, 0, 0)
ops.beamIntegration('HingeRadau', 5001, sectioninf_5001, rinfM_5001 * 0.1, sectionpin_5001, rinfM_5001 * 0.05,
                    sectioninterior_5001)
eleType = 'forceBeamColumn'
ops.element(eleType, 50011, 5001, 19, 5001, 5001)
ops.element(eleType, 50012, 5001, 13, 5001, 5001)

# 5005
ops.element(eleType, 50051, 5005, 55, 5001, 5001)
ops.element(eleType, 50052, 5005, 49, 5001, 5001)

# C轴墙片1 编号6001
ops.element(eleType, 60011, 6001, 27, 5001, 5001)
ops.element(eleType, 60012, 6001, 15, 5001, 5001)

# 6005
ops.element(eleType, 60051, 6005, 63, 5001, 5001)
ops.element(eleType, 60052, 6005, 51, 5001, 5001)

# A轴墙片 2 编号5002
rinfM_5002 = 1559.85
sectioninf_5002 = 50021  # 塑性铰
infmattag_5002 = list(range(101, 111))
fyfibinf_5002 = [0.000007, 0.000012, 0.000016, 0.000020, 0.000033,
                 0.000033, 0.000020, 0.000016, 0.000012, 0.000007]
areafibinf_5002 = [2303.109700, 2676.617717, 2898.643970, 3123.175748, 3625.207262,
                   3625.207262, 3123.175748, 2898.643970, 2676.617717, 2303.109700]
zfibinf_5002 = [4639.546497, 2418.755244, 1712.382216, 1239.294174, 649.547302,
                -649.547302, -1239.294174, -1712.382216, -2418.755244, -4639.546497]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_5002[i], fyfibinf_5002[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_5002, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_5002[i], areafibinf_5002[i], infmattag_5002[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_5002 = 50022  # 弹性铰
AreainfM_5002 = sum(areafibinf_5002)
ops.section('Elastic', sectionpin_5002, Eminfm, AreainfM_5002, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_5002 = 50023  # 内部弹性截面
InertiainfM_5002 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_5002, Eminfm, AreainfM_5002, 1e-5, InertiainfM_5002, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 5002, 1, 0, 0)
ops.beamIntegration('HingeRadau', 5002, sectioninf_5002, rinfM_5002 * 0.1, sectionpin_5002, rinfM_5002 * 0.05,
                    sectioninterior_5002)
eleType = 'forceBeamColumn'
ops.element(eleType, 50021, 5002, 31, 5002, 5002)
ops.element(eleType, 50022, 5002, 2, 5002, 5002)

# 5006
ops.element(eleType, 50061, 5006, 67, 5002, 5002)
ops.element(eleType, 50062, 5006, 38, 5002, 5002)

# C轴墙片2 编号6002
ops.element(eleType, 60021, 6002, 33, 5002, 5002)
ops.element(eleType, 60022, 6002, 10, 5002, 5002)

# 6006
ops.element(eleType, 60061, 6006, 69, 5002, 5002)
ops.element(eleType, 60062, 6006, 46, 5002, 5002)

# # A轴墙片3 编号5003
# rinfM_5003 = 2080.865
# sectioninf_5003 = 50031  # 塑性铰
# infmattag_5003 = list(range(111,121))
# fyfibinf_5003 = []
# areafibinf_5003 = []
# zfibinf_5003 = []
# for i in range(0,10):
#     ops.uniaxialMaterial('Steel01', infmattag_5003[i], fyfibinf_5003[i], Eminfm, 0.02)
# ops.section('Fiber', sectioninf_5003, '-GJ', 1.0e14)
# for i in range(0,10):
#     ops.fiber(0, zfibinf_5003[i], areafibinf_5003[i], infmattag_5003[i])
# ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)
#
# sectionpin_5003 = 50032 # 弹性铰
# AreainfM_5003 = sum(areafibinf_5003)
# ops.section('Elastic', sectionpin_5003, Eminfm, AreainfM_5003, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)
#
# sectioninterior_5003 = 50033 # 内部弹性截面
# InertiainfM_5003 = 642.461 * 25.4**4
# ops.section('Elastic', sectioninterior_5003, Eminfm, AreainfM_5003, 1e-5, InertiainfM_5003, Eminfm / 2.5, 1.0e14)
#
# ops.geomTransf('Linear', 5003, 0, 0 ,-1)
# ops.beamIntegration('HingeRadau', 5003, sectioninf_5003, rinfM_5003 * 0.1, sectionpin_5003, rinfM_5003 * 0.05, sectioninterior_5003)
# eleType = 'forceBeamColumn'
# ops.element(eleType, 50031, 5003, 37, 5003, 5003)
# ops.element(eleType, 50032, 5003, 31, 5003, 5003)

# A轴墙片4 编号5004
rinfM_5004 = 1708.98
sectioninf_5004 = 50041  # 塑性铰
infmattag_5004 = list(range(121, 131))
fyfibinf_5004 = [0.000015, 0.000016, 0.000017, 0.000019, 0.000021,
                 0.000021, 0.000016, 0.000017, 0.000019, 0.000015]
areafibinf_5004 = [1245.735315, 2128.750765, 2828.180038, 3689.956310, 6277.863308,
                   6277.863308, 3689.956310, 2828.180038, 2128.750765, 1245.735315]
zfibinf_5004 = [6896.873913, 3595.577705, 2545.525569, 1842.261019, 965.578391,
                -965.578391, -1842.261019, -2545.525569, -3595.577705, -6896.873913]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_5004[i], fyfibinf_5004[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_5004, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_5004[i], areafibinf_5004[i], infmattag_5004[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_5004 = 50042  # 弹性铰
AreainfM_5004 = sum(areafibinf_5004)
ops.section('Elastic', sectionpin_5004, Eminfm, AreainfM_5004, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_5004 = 50043  # 内部弹性截面
InertiainfM_5004 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_5004, Eminfm, AreainfM_5004, 1e-5, InertiainfM_5004, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 5004, 1, 0, 0)
ops.beamIntegration('HingeRadau', 5004, sectioninf_5004, rinfM_5004 * 0.1, sectionpin_5004, rinfM_5004 * 0.05,
                    sectioninterior_5004)
eleType = 'forceBeamColumn'
ops.element(eleType, 50041, 5004, 49, 5004, 5004)
ops.element(eleType, 50042, 5004, 20, 5004, 5004)

# 6004
ops.element(eleType, 60041, 6004, 51, 5004, 5004)
ops.element(eleType, 60042, 6004, 28, 5004, 5004)

# C轴墙片3 编号6003
rinfM_6003 = 2080.865
sectioninf_6003 = 60031  # 塑性铰
infmattag_6003 = list(range(141, 151))
fyfibinf_6003 = [0.696695, 0.020192, 0.003089, 0.000533, 0.000016,
                 0.000016, 0.000533, 0.003089, 0.020192, 0.696695]
areafibinf_6003 = [0.031345, 2.074567, 19.157198, 153.522809, 9817.360901,
                   9817.360901, 153.522809, 19.157198, 2.074567, 0.031345]
zfibinf_6003 = [2163.421689, 1127.866173, 798.484254, 577.883182, 302.884069,
                -302.884069, -577.883182, -798.484254, -1127.866173, -2163.421689]
for i in range(0, 10):
    ops.uniaxialMaterial('Steel01', infmattag_6003[i], fyfibinf_6003[i], Eminfm, 0.02)
ops.section('Fiber', sectioninf_6003, '-GJ', 1.0e14)
for i in range(0, 10):
    ops.fiber(0, zfibinf_6003[i], areafibinf_6003[i], infmattag_6003[i])
ops.layer('straight', IDYMaterial, 1, 0.0001, 1.0, 0.0, 1.0, 0.0)

sectionpin_6003 = 60032  # 弹性铰
AreainfM_6003 = sum(areafibinf_6003)
ops.section('Elastic', sectionpin_6003, Eminfm, AreainfM_6003, 1e-3, 1e-3, Eminfm / 2.5, 1e-3)

sectioninterior_6003 = 60033  # 内部弹性截面
InertiainfM_6003 = 642.461 * 25.4 ** 4
ops.section('Elastic', sectioninterior_6003, Eminfm, AreainfM_6003, 1e-5, InertiainfM_6003, Eminfm / 2.5, 1.0e14)

ops.geomTransf('Linear', 6003, 1, 0, 0)
ops.beamIntegration('HingeRadau', 6003, sectioninf_6003, rinfM_6003 * 0.1, sectionpin_6003, rinfM_6003 * 0.05,
                    sectioninterior_6003)
eleType = 'forceBeamColumn'
ops.element(eleType, 60031, 6003, 45, 6003, 6003)
ops.element(eleType, 60032, 6003, 33, 6003, 6003)

print("OK！，填充墙等效杆")
# ---------------------------------------分析-----------------------------------------
# opsplt.plot_model()

# 初始模态分析
numEigen = 2
eigenValues = ops.eigen(numEigen)
omegaValues = []
periodValues = []
frequencyValues = []
for i in range(numEigen):
    lambdai = eigenValues[i]
    omegai = math.sqrt(lambdai)
    omegaValues.append(omegai)
    Ti = 2 * math.pi / omegai
    periodValues.append(Ti)
    fi = 1 / Ti
    frequencyValues.append(fi)
print("结构初始自振圆频率：", omegaValues)
print("结构初始自振周期：", periodValues)
print("结构初始自振频率：", frequencyValues)

# 瑞雷阻尼
xDamp = 0.05
alphaM = xDamp * (2 * omegaValues[0] * omegaValues[1]) / (omegaValues[0] + omegaValues[1])
betaKcurr = 2. * xDamp / (omegaValues[0] + omegaValues[1])
ops.rayleigh(alphaM, betaKcurr, 0, 0)

# # 输出
# ops.recorder('Node', '-file', "DataOut/node_2_accel.txt", '-time',  '-node', 2, '-dof', 1, 2, 'accel')
# ops.recorder('Node', '-file', "DataOut/node_2_disp.txt", '-time',   '-node', 2, '-dof', 1, 2, 'disp')
#
#
# print("Go Gravity Analysis")
# Tol = 1.0e-8
# ops.constraints('Transformation')
# ops.numberer('RCM')
# ops.system('UmfPack')
# ops.test('EnergyIncr', Tol, 6)
# ops.algorithm('Newton')
# NstepGravity = 10  # apply gravity in 10 steps
# DGravity = 1.0 / NstepGravity  # first load increment
# ops.integrator('LoadControl', DGravity)
# ops.analysis('Static')
# ops.analyze(NstepGravity)
#
# ops.loadConst('-time', 0.0)
#
# print("Model Built")
