#!/usr/bin/env python
# coding: utf-8

# # Código: URL em QR Code
# ### Autora: Carla Edila Silveira
# ### Contato: rosa.carla@pucpr.edu.br
# ### Finalidade: converter uma URL em um QR Code com uso do pacote qrcode do Python
# ### Data: 25/08/2022

# In[3]:


# Instala pacote qrcode
get_ipython().system('pip install -q qrcode')


# In[4]:


# Importa biblioteca qrcode
import qrcode


# In[5]:


# Converte em QR Code a URL passada por parâmetro e mostra a imagem na tela
qrcode.make('https://github.com/rosacarla')


# In[6]:


# Salva imagem do QR Code em um arquivo do tipo .png
image = qrcode.make('https://github.com/rosacarla')
image.save('github-rosacarla.png')


# In[11]:


# Cria objeto QR Code com alteração do tamanho
qr = qrcode.QRCode(version = 2, 
                   box_size = 12, 
                   border = 6) 
qr.add_data('https://www.atlassian.com/br/agile/devops')
qr.make(fit=True)

# Muda parâmetros de cores (1o. plano e plano de fundo)
qr.make_image(fill_color="navy", back_color="white")

