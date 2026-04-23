import matplotlib.pyplot as plt
x = [1,2,3,4,5]
 
plt.plot(x, [2,4,6,8,10], color="blue",   label="2023")
plt.plot(x, [1,3,5,7,9],  color="orange", label="2024")
 
# Basic legend
plt.legend()
 
# Positioned legend
plt.legend(loc="upper left")      # fixed position
plt.legend(loc="best")            # auto best position
 
# Styled legend
plt.legend(loc        = "upper left",
           fontsize   = 11,
           frameon    = True,      # border box
           framealpha = 0.9,       # box transparency
           shadow     = True,
           title      = "Year",
           title_fontsize = 12)
 
plt.show()
