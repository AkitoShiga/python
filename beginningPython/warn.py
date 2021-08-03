from warnings import warn
from warnings import filterwarnings
warn("w@@@ring")

# 抑制
filterwarnings("ignore")
warn("ignored warn")

# Exception
filterwarnings("error")
warn("error warn")
