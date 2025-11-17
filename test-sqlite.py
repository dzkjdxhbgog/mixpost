#!/usr/bin/env python3

import os
import sqlite3
import json

def test_database_connection():
    database_path = '/home/dan/F盘/mixpost/database/database.sqlite'
    
    print("Testing database connection...")
    print(f"Database path: {database_path}")
    
    # 检查文件是否存在
    if os.path.exists(database_path):
        print("✓ Database file exists")
        
        # 检查文件权限
        if os.access(database_path, os.R_OK) and os.access(database_path, os.W_OK):
            print("✓ Database file is readable and writable")
        else:
            print("✗ Database file permissions issue")
            print(f"  Readable: {os.access(database_path, os.R_OK)}")
            print(f"  Writable: {os.access(database_path, os.W_OK)}")
        
        # 检查目录权限
        dir_path = os.path.dirname(database_path)
        if os.access(dir_path, os.W_OK):
            print("✓ Database directory is writable")
        else:
            print("✗ Database directory is not writable")
            
    else:
        print("✗ Database file does not exist")
    
    # 测试 SQLite 连接
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        print("✓ SQLite connection successful")
        
        # 创建测试表
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
        conn.commit()
        print("✓ Test table created successfully")
        
        # 插入测试数据
        cursor.execute("INSERT INTO test (name) VALUES (?)", ("test_connection",))
        conn.commit()
        print("✓ Test data inserted successfully")
        
        # 查询测试数据
        cursor.execute("SELECT * FROM test LIMIT 1")
        row = cursor.fetchone()
        print(f"✓ Test data retrieved: id={row[0]}, name={row[1]}")
        
        # 清理测试表
        cursor.execute("DROP TABLE test")
        conn.commit()
        print("✓ Test table cleaned up")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"✗ SQLite connection failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    print("\nDatabase connection test completed.")

if __name__ == "__main__":
    test_database_connection()