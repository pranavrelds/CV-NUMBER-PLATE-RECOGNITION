import os
from pathlib import Path

list_of_files = [ 
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/prepare_base_model.py",
    f"src/components/model_trainer.py",
    f"src/components/model_pusher.py",
    f"src/config/__init__.py",
    f"src/constants/__init__.py",
    f"src/entity/__init__.py",
    f"src/exception/__init__.py",
    f"src/logger/__init__.py",
    f"src/utils/__init__.py",
    f"src/pipeline/__init__.py",
    "requirements.txt",
    "app.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir , file_name = os.path.split(file_path)
    
    if file_dir!= '':
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass # Create an empty file and do nothing

