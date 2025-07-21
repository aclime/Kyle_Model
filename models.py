import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sigma_V_0=0.4 # Variance of the Funadmental Value Observed by the insider at period n=0
sigma_u=0.5 # Volatility of the Noise Traders' Qunatity
tol = 1e-6
sigma_V_N_guess=0.9
sigma_V_N_guess=0.10732122295726415
#sigma_V_N_guess=1.450854632668097e-06
N=3

def solve_lambda(lambda_guess, sigma_u, sigma_V_n, alpha_n):
    tol = 1e-6
    def objective(_lambda_):
        return 2*(1-_lambda_**2 * sigma_u**2 / sigma_V_n)*(1-alpha_n*_lambda_)-1
    return fsolve(objective, lambda_guess,xtol=tol)[0]

alpha_N=0
delta_N=0
#lambda_terminal=(1/2)*np.sqrt(sigma_V_N)/sigma_u
#lambda_n=lambda_terminal
alpha_n,delta_n=alpha_N,delta_N
sigma_V_n=sigma_V_N_guess

for n in range(N,0,-1):
    print(f'n={n}')
    print(f'α_{n}:{alpha_n}')
    print(f'Σ_{n}:{sigma_V_n}')
    lambda_guess=100_000
    lambda_n=solve_lambda(lambda_guess, sigma_u, sigma_V_n, alpha_n)
    print(f'λ_{n}:{lambda_n}')
    beta_n=(1-2*alpha_n*lambda_n)/(2*lambda_n*(1-alpha_n*lambda_n))
    print(f'β_{n}:{beta_n}')
    #recursive step
    alpha_n=1/(4*lambda_n*(1-alpha_n*lambda_n))
    #lambda_guess=max(1e-3,lambda_guess)
    sigma_V_n/=(1-beta_n*lambda_n)
    print('----------')
    
abs(sigma_V_n-sigma_V_0)

