import torch
from monai.networks.nets import DenseNet121
from PIL import Image
import torchvision.transforms as transforms
list=['Tho',
 'Raa',
 'Phe',
 'Gam',
 'Che',
 'Tu',
 'He',
 'Gnam',
 'Dhoo',
 'Tham',
 'Sam',
 'Ve',
 'No',
 'Mu',
 'Bu',
 'DDO',
 'Dau',
 'Zoo',
 'Khee',
 'TTho',
 'Bhi',
 'Zai',
 'Ji',
 'Jo',
 'I',
 'Shoo',
 'TToo',
 'Soo',
 'Ane',
 'Ale',
 'Phee',
 'Tam',
 'Kho',
 'Naa',
 'Bho',
 'Sho',
 'Pam',
 'Tai',
 'Na',
 'Bo',
 'Yi',
 'Se',
 'Chhoo',
 'So',
 'Chhai',
 'Thau',
 'TTai',
 'Dhee',
 'Pai',
 'Ko',
 'DDhoo',
 'Kshi',
 'Dhu',
 'Gne',
 'Taa',
 'Ge',
 'Kham',
 'E',
 'Rai',
 'Yo',
 'Yee',
 'DDau',
 'Ra',
 'Mam',
 'Jaa',
 'Ta',
 'TThau',
 'Kam',
 'Pe',
 'Ghee',
 'TThai',
 'Gee',
 'Hai',
 'Da',
 'Phau',
 'Thi',
 'Lo',
 'Yam',
 'Ze',
 'SShoo',
 'Thoo',
 'SShe',
 'Dai',
 'TThoo',
 'Khe',
 'Lam',
 'Thee',
 'DDai',
 'Chha',
 'Va',
 'U',
 'Thaa',
 'DDhaa',
 'Ala',
 'Gnai',
 'DDee',
 'TTaa',
 'SShee',
 'Vai',
 'TThaa',
 'Sau',
 'Ro',
 'Jam',
 'Gnee',
 'Ghe',
 'Mo',
 'Chhau',
 'Du',
 'Anoo',
 'Kee',
 'Chhe',
 'Phoo',
 'Alaa',
 'Chhu',
 'Maa',
 'Ano',
 'Ghai',
 'Tau',
 'Be',
 'Moo',
 'Gnau',
 'Daa',
 'Loo',
 'Mau',
 'Mai',
 'Kshee',
 'TTee',
 'DDu',
 'Bee',
 'Yaa',
 'Nam',
 'Hu',
 'Pee',
 'Ne',
 'Dho',
 'Alau',
 'Kshau',
 'Zaa',
 'Su',
 'DDhee',
 'DDho',
 'Khau',
 'Ksha',
 'Shee',
 'Yau',
 'Pham',
 'Alai',
 'Vu',
 'DDi',
 'DDoo',
 'Khoo',
 'Ai',
 'Baa',
 'Aloo',
 'Phai',
 'Gu',
 'Gnu',
 'Gaa',
 'Ghaa',
 'Nu',
 'Koo',
 'Dee',
 'Khai',
 'Baa',
 'Anau',
 'Di',
 'Kha',
 'Gi',
 'Vam',
 'Dhau',
 'Doo',
 'Phaa',
 'To',
 'Chau',
 'Zu',
 'See',
 'Shai',
 'Khu',
 'Gni',
 'Ali',
 'Ri',
 'Phi',
 'Si',
 'Chi',
 'Yai',
 'Zi',
 'Za',
 'Ja',
 'Pha',
 'Bi',
 'Haa',
 'Noo',
 'Too',
 'Gho',
 'Ke',
 'Hee',
 'DDam',
 'TTha',
 'Anai',
 'Phu',
 'TThu',
 'Te',
 'SShau',
 'Chhee',
 'Goo',
 'Shaa',
 'Go',
 'Ya',
 'Pu',
 'Bha',
 'Saa',
 'Chai',
 'SShi',
 'Anam',
 'She',
 'TTam',
 'Anu',
 'Ba',
 'TTu',
 'Dhai',
 'Vee',
 'Rau',
 'TTo',
 'Gna',
 'A',
 'Shau',
 'Me',
 'Ma',
 'TThi',
 'DDhu',
 'Tha',
 'TTi',
 'Bam',
 'O',
 'Mi',
 'Ghoo',
 'Re',
 'Lee',
 'Mee',
 'Chham',
 'Alu',
 'Ani',
 'Bai',
 'Sham',
 'DDham',
 'Cho',
 'Po',
 'Ti',
 'Pau',
 'Bhu',
 'SSha',
 'Ai',
 'Voo',
 'Zee',
 'Jau',
 'Je',
 'Pa',
 'Jee',
 'Kaa',
 'Nee',
 'Ho',
 'DDhe',
 'Choo',
 'TTau',
 'Hoo',
 'Roo',
 'Li',
 'Ru',
 'Ksh',
 'Sha',
 'Yu',
 'Ksham',
 'Ghi',
 'Dam',
 'Nai',
 'Yoo',
 'Hau',
 'Do',
 'SShai',
 'Ga',
 'Anee',
 'TTa',
 'Gha',
 'Lau',
 'Vau',
 'Jai',
 'Au',
 'Boo',
 'Vo',
 'TThe',
 'TTe',
 'SShu',
 'SSham',
 'Ghau',
 'Vaa',
 'Lai',
 'Anaa',
 'DDaa',
 'Alo',
 'Tee',
 'Am',
 'Ham',
 'Ksho',
 'TTham',
 'Alee',
 'Lu',
 'Pi',
 'Kshai',
 'Poo',
 'Zau',
 'Shi',
 'Dham',
 'Cham',
 'Chee',
 'Gnaa',
 'AA',
 'Ku',
 'Bhoo',
 'Ni',
 'Chaa',
 'Shu',
 'Kshu',
 'OO',
 'Cha',
 'Bhe',
 'Zam',
 'Ana',
 'Vi',
 'Bhaa',
 'Le',
 'Bau',
 'De',
 'DDe',
 'SSh',
 'Aloo',
 'Bhau',
 'The',
 'Dhe',
 'Thu',
 'TThee',
 'Bhee',
 'Chhaa',
 'Gai',
 'Kshoo',
 'Sai',
 'Ki',
 'Ree',
 'Gau',
 'DDa',
 'Kau',
 'Alam',
 'Gno',
 'DDhi',
 'Thai',
 'Khaa',
 'Bham',
 'Kai',
 'Dhi',
 'Kshe',
 'Gham',
 'Hi',
 'Pho',
 'Ye',
 'Chho',
 'EE',
 'Nau',
 'Khi',
 'Ram',
 'Bhai',
 'Gnoo',
 'Ghu',
 'Chu',
 'Ka',
 'Paa',
 'Chhi',
 'DDha',
 'SSho',
 'La',
 'Ha',
 'Zo',
 'Joo',
 'Laa',
 'DDhau',
 'DDhai',
 'Sa']

def load_model(model_path, num_classes):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = DenseNet121(spatial_dims=2, in_channels=1, out_channels=num_classes).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()  # Ensure the model is in eval mode
    return model

def preprocess_image(image_path):
    # Ensure this matches your training preprocessing
    image = Image.open(image_path).convert('L')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485], std=[0.229])
    ])
    return transform(image)

def predict(model, image_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    image = preprocess_image(image_path).to(device)
    image = image.unsqueeze(0)
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return predicted.item()

# Usage
model_path = 'best_metric_model.pth'
num_classes = 385
model = load_model(model_path, num_classes)

# Test with multiple images
image_paths = ['Aiii.jpg', 'BAA.jpg','Aloo.jpg'] 
bais=0 # Add your image paths
for img_path in image_paths:
    prediction = predict(model, img_path) + bais
    print(f'Image: {img_path}, Predicted class: {list[prediction]}')
    bais+=1
