#!/usr/bin/env python3

import os
import sqlite3
import json

def check_environment():
    print("=== Mixpost Environment Diagnostics ===\n")
    
    # 检查 .env 文件
    env_file = '/home/dan/F盘/mixpost/.env'
    if os.path.exists(env_file):
        print("✓ .env file exists")
        with open(env_file, 'r') as f:
            env_content = f.read()
            
        # 检查关键配置
        required_configs = [
            'APP_KEY',
            'DB_CONNECTION',
            'DB_DATABASE',
            'CACHE_DRIVER',
            'SESSION_DRIVER',
            'QUEUE_CONNECTION'
        ]
        
        for config in required_configs:
            if config in env_content and not env_content.split(config + '=')[1].split('\n')[0].strip() == '':
                print(f"✓ {config} is configured")
            else:
                print(f"✗ {config} is missing or empty")
    else:
        print("✗ .env file does not exist")
    
    print()

def check_database():
    print("=== Database Check ===\n")
    
    database_path = '/home/dan/F盘/mixpost/database/database.sqlite'
    
    # 检查数据库文件
    if os.path.exists(database_path):
        print("✓ Database file exists")
        
        # 检查文件权限
        if os.access(database_path, os.R_OK) and os.access(database_path, os.W_OK):
            print("✓ Database file has correct permissions")
        else:
            print("✗ Database file permissions issue")
            
        # 测试数据库连接
        try:
            conn = sqlite3.connect(database_path)
            cursor = conn.cursor()
            
            # 检查是否能执行基本操作
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result and result[0] == 1:
                print("✓ Database connection test successful")
            else:
                print("✗ Database query test failed")
            
            conn.close()
        except sqlite3.Error as e:
            print(f"✗ Database connection failed: {e}")
    else:
        print("✗ Database file does not exist")
    
    print()

def check_directories():
    print("=== Directory Structure Check ===\n")
    
    required_dirs = [
        '/home/dan/F盘/mixpost',
        '/home/dan/F盘/mixpost/database',
        '/home/dan/F盘/mixpost/config',
        '/home/dan/F盘/mixpost/src',
        '/home/dan/F盘/mixpost/resources'
    ]
    
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✓ {dir_path} exists")
            if os.access(dir_path, os.W_OK):
                print(f"✓ {dir_path} is writable")
            else:
                print(f"✗ {dir_path} is not writable")
        else:
            print(f"✗ {dir_path} does not exist")
    
    print()

def check_config_files():
    print("=== Configuration Files Check ===\n")
    
    config_files = [
        '/home/dan/F盘/mixpost/config/mixpost.php',
        '/home/dan/F盘/mixpost/composer.json',
        '/home/dan/F盘/mixpost/.env'
    ]
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"✓ {config_file} exists")
            try:
                with open(config_file, 'r') as f:
                    content = f.read()
                    if len(content) > 0:
                        print(f"✓ {config_file} is not empty")
                    else:
                        print(f"✗ {config_file} is empty")
            except Exception as e:
                print(f"✗ Error reading {config_file}: {e}")
        else:
            print(f"✗ {config_file} does not exist")
    
    print()

def suggest_solutions():
    print("=== Suggested Solutions ===\n")
    
    suggestions = [
        "1. 确保所有必需的 PHP 扩展已安装：\n   sudo apt-get install php-sqlite3 php-mbstring php-xml php-curl php-json php-zip",
        
        "2. 如果使用 Laravel 框架，确保已运行：\n   php artisan key:generate\n   php artisan migrate\n   php artisan storage:link",
        
        "3. 检查 Web 服务器用户权限：\n   sudo chown -R www-data:www-data /home/dan/F盘/mixpost\n   sudo chmod -R 755 /home/dan/F盘/mixpost\n   sudo chmod -R 775 /home/dan/F盘/mixpost/database",
        
        "4. 确保 SQLite 已正确安装：\n   sqlite3 --version",
        
        "5. 检查 .env 文件中的所有配置是否正确，特别是数据库路径"
    ]
    
    for suggestion in suggestions:
        print(suggestion)
        print()

if __name__ == "__main__":
    check_environment()
    check_database()
    check_directories()
    check_config_files()
    suggest_solutions()