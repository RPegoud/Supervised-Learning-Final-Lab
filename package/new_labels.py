import torch

new_labels = {}
for idx in range(9):
    new_labels[idx] = 0 # speed limitation
for idx in range(18, 32):
    new_labels[idx] = 1 # danger
for idx in range(33, 41):
    new_labels[idx] = 2 # change in direction
for idx in [32, 41, 42]:
    new_labels[idx] = 3 # end of limitations
for idx in [9, 10, 15, 16, 17]:
    new_labels[idx] = 4 # no circulation
for idx in range(11, 14):
    new_labels[idx] = 5 # priority
new_labels[14] = 6 # stop

new_labels_to_category = {
    0:'Speed limitation',
    1:'Danger',
    2:'Change in direction',
    3:'End of limitations',
    4:'No circulation',
    5:'Priority',
    6:'Stop'
}

def convert_labels(label_batch):
    """
    input: label_batch (torch.Tensor), a sequence of original labels
    output: (torch.Tensor) a sequence of labels corresponding to the new classes
    """
    assert torch.is_tensor(label_batch), "the input batch sequence is not a torch tensor"
    new_labels_batch = torch.tensor([new_labels.get(i) for i in label_batch.numpy()])
    # print(f'input length:{len(label_batch)}, output length:{len(new_labels_batch)}  ')
    return new_labels_batch

