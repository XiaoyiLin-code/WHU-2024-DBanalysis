#!/bin/bash
  
# 获取脚本所在的目录，确保在正确的目录下操作
SCRIPT_DIR=$(dirname "$0")

# 检查test.txt文件是否存在
if [ ! -f "${SCRIPT_DIR}/test.txt" ]; then
    echo "test.txt 文件不存在于 $SCRIPT_DIR!"
    exit 1
fi

# 从test.txt读取每一行
while IFS= read -r benchmark_file; do
    # 生成输出文件名，将可能存在的路径分隔符替换为下划线，并添加.txt后缀
    filename=$(echo "$benchmark_file" | tr '/' '_' | tr ' ' '_').txt

    # 构造完整的命令
    command_info="../build/release/benchmark/benchmark_runner $benchmark_file --info "
    command_query="../build/release/benchmark/benchmark_runner $benchmark_file --query"
    command_profile="../build/release/benchmark/benchmark_runner $benchmark_file --profile"
    command_default="../build/release/benchmark/benchmark_runner $benchmark_file "

    # 执行命令，并将输出重定向到文件，包括错误输出
    echo "正在运行: $command_info"
    $command_info > "${SCRIPT_DIR}/result/info-$filename" 2>&1
    echo "info已保存"
    echo "正在运行: $command_query"
    $command_query > "${SCRIPT_DIR}/result/query-$filename" 2>&1
    echo "query已保存"
    echo "正在运行: $command_profile"
    $command_profile > "${SCRIPT_DIR}/result/profile-$filename" 2>&1
    echo "profile已保存"
done < "${SCRIPT_DIR}/test.txt"

