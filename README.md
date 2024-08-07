
This repository is the sample code which achieved 5th place at KDD 2024 OAG-Challenge PST task. The techinical paper is available follows:
https://openreview.net/forum?id=Mi5T2wgySR&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DKDD.org%2F2024%2FWorkshop%2FOAG-Challenge_Cup%2FAuthors%23your-submissions)

## Prerequisites
- Linux System
- Python 3.10
- CUDA 12.0
- NVIDIA A100 80G

### Installation
Clone this repository.

```bash
git clone 
cd kddcup_oag-challenge-pst_rank6
```

Please install dependencies by

```bash
pip install -r requirements.txt
```

## PST Dataset
The dataset can be downloaded from [BaiduPan](https://pan.baidu.com/s/1I_HZXBx7U0UsRHJL5JJagw?pwd=bft3) with password bft3, [Aliyun](https://open-data-set.oss-cn-beijing.aliyuncs.com/oag-benchmark/kddcup-2024/PST/PST.zip) or [DropBox](https://www.dropbox.com/scl/fi/namx1n55xzqil4zbkd5sv/PST.zip?rlkey=impcbm2acqmqhurv2oj0xxysx&dl=1).
The paper XML files are generated by [Grobid](https://grobid.readthedocs.io/en/latest/Introduction/) APIs from paper pdfs.
And please download the DBLP-Citation-network V16 from [DBLP](https://open.aminer.cn/open/article?id=655db2202ab17a072284bc0c) and version OAG 3.1 from [OAG](https://open.aminer.cn/open/article?id=5965cf249ed5db41ed4f52bf), extract them, and place them in the data folder.


## Directory structure
```bash
--kddcup2024-oagpst-solution
	--script
		--...(some files)
	--data
    	--PST
    		--...(some files)
    		--paper-xml(load competition dataset)
```


![![Main Approch](https://github.com/piendata/kddcup_oag-challenge-pst_rank6/blob/main/figure.jpg "Main Approach")

## Figure of the Main approach

## description of the files
### 1_data_manipulation.ipynb
This notebook uses XML files and data from DBLP and OAG to extract the following information about academic papers and their references:

### 2_text_embedding.ipynb
Text embeddings are performed on the titles of papers and their references using `multilingual-e5-large`, and cosine similarity is calculated. Additionally, these embedding vectors are reduced to two dimensions using UMAP.

### 3_network_processing.ipynb
Features related to citation counts and page information for each author were created using data from sources like DBLP. Additionally, a network of references was built, and after creating embeddings for nodes using node2vec to capture the network relationships of papers from sources like DBLP, these embeddings were dimensionally reduced using UMAP and used as features.

### 4_createMLdataset_and_train.ipynb
The features generated above were used to conduct machine learning training and inference. Training was performed using LightGBM and CatBoost, with parameter optimization conducted using Optuna. Due to the very limited number of positive examples available, BorderlineSMOTE was used to perform oversampling to increase the data volume. The final output was produced by ensembling the prediction results of LightGBM and CatBoost.

### 5_inference.ipynb
Load the model with the highest score obtained during the training process and make predictions. Also, generate a submission file.

## note
The "make_submission_file.ipynb" notebook formats the output in the submission file format and includes titles. It is used for comparing prediction results, and the generated file is stored as "valid_submission_test.json" in the data folder.

If you have any questions, please contact me. Email:piendata@gmail.com