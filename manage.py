from project import create_app

app = create_app()

# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时， if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)