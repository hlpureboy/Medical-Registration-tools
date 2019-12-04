# 脑图像配准工具
使用说明:
安装tqdm库
```shell script
pip install tqdm
```
- DiffusionKit中reg_aladin
    - [x] DiffusionKit中的reg_aladin配准工具
    - [x] 中科院提供的BN_Atlas_246_1mm的配准文件
    - [x] 待配准数据集 ADNI
    
    eg
    ```shell script
    python registration.py -i D:\\peizhun\\input -o D:\\peizhun\\output -reg D:\\peizhun\\DiffusionKit\\reg_aladin.exe -ref D:\\peizhun\\alts\\BN_Atlas_246_1mm.nii
    ```

