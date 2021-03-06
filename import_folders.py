
import sys
import os

base_path = os.path.abspath('')
print ("Base path: %s"%base_path)

sys.path.append(base_path + "/")
sys.path.append(base_path + "/InformationClasses/")
sys.path.append(base_path + "/TradingClasses/")

sys.path.append(base_path + "/InformationClasses/CTimeData/")
sys.path.append(base_path + "/InformationClasses/CPortfolio/")
sys.path.append(base_path + "/InformationClasses/CSymbol/")
sys.path.append(base_path + "/InformationClasses/CBond/")

sys.path.append(base_path + "/TradingClasses/StrategyPool/")
sys.path.append(base_path + "/TradingClasses/Coliseum/")
sys.path.append(base_path + "/TradingClasses/Brain/")
sys.path.append(base_path + "/TradingClasses/Brain/CMoneyManagement/")

#sys.path.append(base_path + "/TradingClasses/CFilter/")
sys.path.append(base_path + "/MarketModels/CAPM/")

sys.path.append(base_path + "/libs/")
sys.path.append(base_path + "/libs/graph/")       # Graphical libs
sys.path.append(base_path + "/libs/graph/GUI/")       # Graphical libs
sys.path.append(base_path + "/libs/graph/specific/")       # Graphical libs

sys.path.append(base_path + "/libs/DDBB/") # Graphical traders
sys.path.append(base_path + "/libs/math/") # Graphical traders
sys.path.append(base_path + "/libs/utilities/") # Graphical traders
sys.path.append(base_path + "/libs/tradersInfo/") # Graphical traders
sys.path.append(base_path + "/libs/ML/") # Graphical traders

### For the EM algorithm
sys.path.append(base_path + "/libs/EM")
sys.path.append(base_path + "/libs/EM/EM POO")
sys.path.append(base_path + "/libs/EM/utils")
sys.path.append(base_path + "/libs/Distributions")
sys.path.append(base_path + "/libs/Distributions/Watson")
sys.path.append(base_path + "/libs/Distributions/Gaussian")
sys.path.append(base_path + "/libs/Distributions/vonMisesFisher")

### For the Deep Learning
sys.path.append(base_path + "/libs/BBBLSTM")

sys.path.append(base_path + "/RainMaking/")
#imp_folders(os.path.abspath(''))
    
# Change code to only make it one ? main1, change folder name and database
