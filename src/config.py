# src/config.py


import numpy as np


def get_birth_values(df_pivot):
    human_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Human"].values[0]
    mouse_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Mouse"].values[0]
    rat_birth = df_pivot.loc[df_pivot["Parameter"] == "Birth", "Rat"].values[0]
    return human_birth, mouse_birth, rat_birth

#modelo logaritmico
def mod_log(x, b, c):
    return b * np.log(x) + c
#modelo logaritmico con dummy (grupos)
def model_M_log(X, b0, b1, c0, c1):
    x, D = X
    return (b0 + b1 * D) * np.log(x) + (c0 + c1 * D)
#modelo potencia + constante
def mod_pot_const(x, a, b, c):
    return b * x**a + c
#modelo potencia
def mod_pot(x, a, b):
    return b * x**a 
# Power-1/4 models (fixed exponent)
def mod_quarter_const(x, b, c):
    return b * x**0.25 + c
#modelo exponente 1/4
def mod_quarter(x, b):
    return b * x**0.25

def mod_third_const(x, b, c):
    return b * x**(1/3) + c

def mod_third(x, b):
    return b * x**(1/3)

def model_M1(X, b0, b1, c0, c1):
    x, D = X
    return (b0 + b1 * D) * (x ** 0.25) + (c0 + c1 * D)
#modelo exponente compartido libre
def model_M2(X, a, b0, b1, c0, c1):
    x, D = X
    return (b0 + b1 * D) * (x ** a) + (c0 + c1 * D)
#modelo exponente libre 
def model_M3(X, a0, a1, b0, b1, c0, c1):
    x, D = X
    return (b0 + b1 * D) * (x ** (a0 + a1 * D)) + (c0 + c1 * D)
def model_tercio_dummy(X, b0, b1, c0, c1):
    x, D = X
    # Se usa x**(1/3) para el modelo de tercio
    return (b0 + b1 * D) * (x ** (1/3)) + (c0 + c1 * D)
#modelo potencia sin constante, exponente fijo 1/4
def model_M1_nc(X, b0, b1):
    x, D = X
    return (b0 + b1 * D) * (x ** 0.25)
#modelo potencia sin constante, exponente libre compartido
def model_M2_nc(X, a, b0, b1):
    x, D = X
    return (b0 + b1 * D) * (x ** a)
#modelo potencia sin constante, exponente libre por grupo
def model_M3_nc(X, a0, a1, b0, b1):
    x, D = X
    return (b0 + b1 * D) * (x ** (a0 + a1 * D))
def model_tercio_dummy_nc(X, b0, b1):
    x, D = X
    # Se usa x**(1/3) para el modelo de tercio
    return (b0 + b1 * D) * (x ** (1/3)) 

MODELS = {

    # ============================================================
    # BASE MODELS
    # ============================================================

    "M1": {
        "name": "Power",
        "description": "Power model",
        "function": "mod_pot",
        "equation": r"$y = b x^a$",
        "equation_number": 1,
        "initial_params": [0.3, 1.0],
        "param_names": ["a", "b"],
    },

    "M2": {
        "name": "Quarter",
        "description": "Quarter-power model",
        "function": "mod_quarter",
        "equation": r"$y = b x^{1/4}$",
        "equation_number": 2,
        "initial_params": [1.0],
        "param_names": ["b"],
    },

    "M3": {
        "name": "Third",
        "description": "Third-power model",
        "function": "mod_third",
        "equation": r"$y = b x^{1/3}$",
        "equation_number": 3,
        "initial_params": [1.0],
        "param_names": ["b"],
    },

    "M4": {
        "name": "Power + c",
        "description": "Power model with constant",
        "function": "mod_pot_const",
        "equation": r"$y = b x^a + c$",
        "equation_number": 4,
        "initial_params": [0.3, 1.0, 0.0],
        "param_names": ["a", "b", "c"],
    },

    "M5": {
        "name": "Quarter + c",
        "description": "Quarter-power model with constant",
        "function": "mod_quarter_const",
        "equation": r"$y = b x^{1/4} + c$",
        "equation_number": 5,
        "initial_params": [1.0, 0.0],
        "param_names": ["b", "c"],
    },

    "M6": {
        "name": "Third + c",
        "description": "Third-power model with constant",
        "function": "mod_third_const",
        "equation": r"$y = b x^{1/3} + c$",
        "equation_number": 6,
        "initial_params": [1.0, 0.0],
        "param_names": ["b", "c"],
    },

    "M7": {
        "name": "Logarithmic",
        "description": "Logarithmic model",
        "function": "mod_log",
        "equation": r"$y = b \ln(x) + c$",
        "equation_number": 7,
        "initial_params": [10.0, 0.0],
        "param_names": ["b", "c"],
    },

    # ============================================================
    # JOINT MODELS — WITH CONSTANT
    # ============================================================

    "M8": {
        "name": "Logarithmic",
        "description": "Logarithmic model with species dummy",
        "function": "model_M_log",
        "equation": r"$y = (b_0+b_1D)\ln(x)+(c_0+c_1D)$",
        "equation_number": 8,
        "initial_params": [1.0, 0.0, 0.0, 0.0],
        "param_names": ["b₀", "b₁", "c₀", "c₁"],
        "dummy_indices": [1, 3],  # b₁ y c₁ son los coeficientes dummy
    },

    "M9": {
        "name": "Power (quarter) + c",
        "description": "Quarter-power model with species dummy",
        "function": "model_M1",
        "equation": r"$y = (b_0+b_1D)x^{1/4}+(c_0+c_1D)$",
        "equation_number": 9,
        "initial_params": [1.0, 0.0, 0.0, 0.0],
        "param_names": ["b₀", "b₁", "c₀", "c₁"],
        "dummy_indices": [1, 3],
    },

    "M10": {
        "name": "Power (shared) + c",
        "description": "Power model with shared exponent and species dummy",
        "function": "model_M2",
        "equation": r"$y = (b_0+b_1D)x^a+(c_0+c_1D)$",
        "equation_number": 10,
        "initial_params": [0.25, 1.0, 0.0, 0.0, 0.0],
        "param_names": ["a₀", "b₀", "b₁", "c₀", "c₁"],
        "dummy_indices": [2, 4],  # b₁ y c₁
    },

    "M11": {
        "name": "Power (free) + c",
        "description": "Power model with species-specific exponent",
        "function": "model_M3",
        "equation": r"$y = (b_0+b_1D)x^{a_0+a_1D}+(c_0+c_1D)$",
        "equation_number": 11,
        "initial_params": [0.25, 0.0, 1.0, 0.0, 0.0, 0.0],
        "param_names": ["a₀", "a₁", "b₀", "b₁", "c₀", "c₁"],
        "dummy_indices": [1, 3, 5],  # a₁, b₁, c₁
    },
    "M12": {
        "name": "Third-power + c",
        "description": "Third-root model with dummy variable",
        "function": "model_tercio_dummy",
        "equation": r"$y = (b_0+b_1D)x^{1/3}+(c_0+c_1D)$",
        "equation_number": 10,
        "initial_params": [0.25, 0.0, 0.0, 0.0],
        "param_names": ["b₀", "b₁", "c₀", "c₁"],
        "dummy_indices": [1, 3],
    },
   

    # ============================================================
    # JOINT MODELS — WITHOUT CONSTANT
    # ============================================================

    "M13": {
        "name": "Third-power no constant",
        "description": "Third-root model no constant with dummy variable",
        "function": "model_tercio_dummy_nc",
        "equation": r"$y = (b_0+b_1D)x^{1/3}$",
        "equation_number": 11,
        "initial_params": [0.25, 0.0],
        "param_names": ["b₀", "b₁"],
        "dummy_indices": [1],
    },
    
    "M14": {
        "name": "Power (quarter)",
        "description": "Quarter-power model with species dummy, no constant",
        "function": "model_M1_nc",
        "equation": r"$y = (b_0+b_1D)x^{1/4}$",
        "equation_number": 12,
        "initial_params": [1.0, 0.0],
        "param_names": ["b₀", "b₁"],
        "dummy_indices": [1],
    },

    "M15": {
        "name": "Power (shared)",
        "description": "Power model with shared exponent and species dummy, no constant",
        "function": "model_M2_nc",
        "equation": r"$y = (b_0+b_1D)x^a$",
        "equation_number": 13,
        "initial_params": [0.25, 1.0, 0.0],
        "param_names": ["a₀", "b₀", "b₁"],
        "dummy_indices": [2],
    },

    "M16": {
        "name": "Power (free)",
        "description": "Power model with species-specific exponent, no constant",
        "function": "model_M3_nc",
        "equation": r"$y = (b_0+b_1D)x^{a_0+a_1D}$",
        "equation_number": 14,
        "initial_params": [0.25, 0.0, 1.0, 0.0],
        "param_names": ["a₀", "a₁", "b₀", "b₁"],
        "dummy_indices": [1, 3],
    },
}

 # Paleta personalizada

colors = {
    'Human': '#67ba6a',
    'Mouse': '#42a5f5',
    'Mouse_O':"#04AF98",
    'Mouse_WO':"#7434DB",
    'Brain': '#ffca28',  # ejemplo
    'Rat': '#ef5351',
    'Body': '#ab47bb'
    
}

# Export settings
TIFF_DPI = 300

# Font sizes for figures
FS_TITLE  = 23
FS_LABEL  = 20
FS_LEGEND = 20
FS_TICK   = 20
FS_PANEL  = 20

# Shared configuration for subplot letter annotations across panels.
panel_subplot_letters = {
    'labels': list('abcdefghijklmnopqrstuvwxyz'),
    'x': -0.11,
    'y': 1.03,
    'fontsize': 11,
    'fontweight': 'bold',
    'ha': 'left',
    'va': 'bottom',
}

params_quarter_plus_c = {
    "rat": {
        "b": 10.4042,
        "c": -12.526
    },
    "mouse": {
        "b": 8.7156,
        "c": -9.5489
    }
}

 





