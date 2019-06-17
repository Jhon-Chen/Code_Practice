<h2>Flask程序的基本结构如下：

|-flasky

    |-app/Flask程序一般都保存在名为app的包中
    
    |-templates/
    
    |-static/
    
    |-main/
    
        |-__init__.py
        
        |-errors.py
        
        |-forms.py
        
        |-views.py
        
    |-__init__.py
    
    |-email.py
    
    |-models.py
    
|-migrations/
和之前一样，migrations文件夹包含数据库迁移脚本

|-tests/
单元测试编写在tests包中

    |-__init__.py
    
    |-test*.py
    
|-venv/
venv文件夹包含Python虚拟环境

|-requirements.txt
列出了所有依赖包，便于在其他电脑中重新生成相同的虚拟环境

|-config.py
存储配置

|-manage.py
用于启动程序以及其他的程序任务