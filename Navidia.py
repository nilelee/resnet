
import torch
# 检查CUDA是否可用
if torch.cuda.is_available():
    try:
        # 尝试执行GPU相关代码
        device = torch.device("cuda")
        x = torch.tensor([1.0, 2.0, 3.0], device=device)
        y = torch.tensor([4.0, 5.0, 6.0], device=device)
        z = x + y
        print(z)
    except RuntimeError as e:
        if "cudnn64_7.dll" in str(e):
            # 发生cudnn64_7.dll not found错误时的处理
            print("Error: cudnn64_7.dll not found, please check CUDA and cuDNN installation.")
        else:
            # 其他运行时错误的处理
            print("RuntimeError:", e)
else:
    print("CUDA is not available.")

print(torch.cuda.device)