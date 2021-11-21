import openseespy.opensees as ops
import math

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
  Ti = 2*math.pi/omegai
  periodValues.append(Ti)
  fi = 1/Ti
  frequencyValues.append(fi)
print("结构初始自振圆频率：",omegaValues)
print("结构初始自振周期：",periodValues)
print("结构初始自振频率：",frequencyValues)

# 瑞雷阻尼
xDamp = 0.05
alphaM = xDamp*(2*omegaValues[0]*omegaValues[1])/(omegaValues[0]+omegaValues[1])
betaKcurr = 2.*xDamp/(omegaValues[0]+omegaValues[1])
ops.rayleigh(alphaM,betaKcurr,0,0)