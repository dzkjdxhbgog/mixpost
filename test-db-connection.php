<?php

// 测试数据库连接
$databasePath = '/home/dan/F盘/mixpost/database/database.sqlite';

echo "Testing database connection...\n";
echo "Database path: $databasePath\n";

// 检查文件是否存在
if (file_exists($databasePath)) {
    echo "✓ Database file exists\n";
    
    // 检查文件权限
    if (is_readable($databasePath) && is_writable($databasePath)) {
        echo "✓ Database file is readable and writable\n";
    } else {
        echo "✗ Database file permissions issue\n";
        echo "  Readable: " . (is_readable($databasePath) ? 'Yes' : 'No') . "\n";
        echo "  Writable: " . (is_writable($databasePath) ? 'Yes' : 'No') . "\n";
    }
    
    // 检查目录权限
    $dir = dirname($databasePath);
    if (is_writable($dir)) {
        echo "✓ Database directory is writable\n";
    } else {
        echo "✗ Database directory is not writable\n";
    }
    
} else {
    echo "✗ Database file does not exist\n";
}

// 测试 SQLite 连接
try {
    $pdo = new PDO("sqlite:$databasePath");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    echo "✓ SQLite connection successful\n";
    
    // 创建测试表
    $pdo->exec("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)");
    echo "✓ Test table created successfully\n";
    
    // 插入测试数据
    $stmt = $pdo->prepare("INSERT INTO test (name) VALUES (:name)");
    $stmt->execute(['name' => 'test_connection']);
    echo "✓ Test data inserted successfully\n";
    
    // 查询测试数据
    $result = $pdo->query("SELECT * FROM test LIMIT 1");
    $row = $result->fetch(PDO::FETCH_ASSOC);
    echo "✓ Test data retrieved: " . json_encode($row) . "\n";
    
    // 清理测试表
    $pdo->exec("DROP TABLE test");
    echo "✓ Test table cleaned up\n";
    
} catch (PDOException $e) {
    echo "✗ SQLite connection failed: " . $e->getMessage() . "\n";
}

echo "\nDatabase connection test completed.\n";