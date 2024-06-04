from fastapi import UploadFile, APIRouter, status, Response
import os
from config import songs_file_path
from loguru import logger

router_file = APIRouter()


@router_file.post("/upload/", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile, response: Response):
    try:
        # 获取文件名
        filename = file.filename
        # 读取文件内容
        file_content = await file.read()
        
        # 确保保存目录存在
        if not os.path.exists(songs_file_path):
            os.makedirs(songs_file_path)
        
        # 构建文件的完整路径
        save_path = os.path.join(songs_file_path, filename)
        
        # 将文件内容写入到指定目录
        with open(save_path, "wb") as f:
            f.write(file_content)
            
        logger.info(f"文件 {filename} 上传成功")
        return {"filename": filename, "path": save_path}
    
    except Exception as e:
        logger.error(f"文件上传失败: {str(e)}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    