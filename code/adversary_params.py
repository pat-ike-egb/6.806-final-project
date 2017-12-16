from __future__ import print_function
# parameters for the adversary network


# cnn (encoder) network params
cnn_out_channels = 64
dropout = 0.3
delta = 1.0
forward_lr = 0.00001

save_encoder_path = '../saved_models/model_adversary_cnn_v1.pt'
load_encoder_path = ''


# android data params
andr_path = '../Android-master/'
andr_dev_pos_path = andr_path + 'dev.pos.txt'
andr_dev_neg_path = andr_path + 'dev.neg.txt'

andr_test_pos_path = andr_path + 'test.pos.txt'
andr_test_neg_path = andr_path + 'test.neg.txt'

andr_tokens_path = andr_path + 'corpus.tsv'


# embeddings params
glove_vecs_path = '../glove_vectors/glove.840B.300d.txt'
glove_vecs_n_channels = 300


# discriminator network params
neg_lr = -1.0 * forward_lr
discr_hidden_size = 200

save_discr_path = '../saved_models/model_adversary_discr_v1.pt'
load_discr_path = ''


# general training parameters
encoder_type = 'cnn'
n_epochs = 1
batch_size = 2
lambda_reg = 0.001 # the regularization parameter for loss2 when computing the total loss



debug = False
if debug: print('debug is True')