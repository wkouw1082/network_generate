import torch
import torch.nn as nn
from config import *

class Encoder_Loss(nn.Module):
    def __init__(self):
        super(Encoder_Loss, self).__init__()

    def forward(self, mu, sigma):
        # For train_seq_condition()
        # return -0.5 * (1+sigma-mu**2-torch.exp(sigma)).sum(axis=2).sum(axis=1)
        
        return -0.5 * torch.sum(1+sigma-mu**2-torch.exp(sigma))

