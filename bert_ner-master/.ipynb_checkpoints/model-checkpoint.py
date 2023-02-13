import torch
import torch.nn as nn
# from pytorch_pretrained_bert import BertModel
import sys
sys.path.append('../')
from modeling import BertModel
from torchcrf import CRF

class Net(nn.Module):
    def __init__(self, model_dir, top_rnns=False, vocab_size=None, entity_num=0, device='cpu', finetuning=False):
        super(Net, self).__init__()
        # print(entity_num)
        self.bert = BertModel.from_pretrained(model_dir, entity_num=entity_num)
        self.hidden_dim = self.bert.config.hidden_size
        # print(self.hidden_dim)
        self.top_rnns=top_rnns
        # if top_rnns:
        self.rnn = nn.LSTM(bidirectional=True, num_layers=2, input_size=self.hidden_dim, hidden_size=self.hidden_dim//2, batch_first=True)
        self.crf1 = CRF(768, batch_first=True)
        self.crf2 = CRF(31, batch_first=True)
        self.fc = nn.Linear(self.hidden_dim, vocab_size)
        # self.dropout = nn.Dropout(0.3)
        
        self.device = device
        self.finetuning = finetuning

        self._param_init(self.fc)

    def _param_init(self, module):
        classname = module.__class__.__name__
        if classname.find('Linear') != -1:
            nn.init.xavier_normal_(module.weight)
            nn.init.constant_(module.bias, 0.0)



    def forward(self, input_ids, input_tags, entity_label):
        '''
        x: (N, T). int64
        y: (N, T). int64

        Returns
        enc: (N, T, VOCAB)
        '''
        input_mask = input_ids.gt(0)
        # print(input_mask)
        input_ids = input_ids.to(self.device)
        input_tags = input_tags.to(self.device)
        entity_label = entity_label.to(self.device)
        input_mask =input_mask.to(self.device)
        mask = input_ids != 1

        if self.training and self.finetuning:
            # print("->bert.train()")
            self.bert.train()
            encoded_layers, _ = self.bert(input_ids, entity_label=entity_label, attention_mask=input_mask)
            enc = encoded_layers[-1]
            # enc = self.crf(enc, input_ids, mask)
        else:
            self.bert.eval()
            with torch.no_grad():
                encoded_layers, _ = self.bert(input_ids, entity_label=entity_label, attention_mask=input_mask)
                enc = encoded_layers[-1]
                # enc = self.crf(enc, input_ids, mask)

        # if self.top_rnns:
        enc, _ = self.rnn(enc)
        # enc = self.dropout(enc)
        logits = self.fc(enc)
        # logits = self.crf(logits, input_ids, mask)
        
        
        
        
        y_hat = logits.argmax(-1)
        # print("**", logits)
        # print("##", y_hat)
        return logits, input_tags, y_hat

