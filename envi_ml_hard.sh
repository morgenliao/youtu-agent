#!/usr/bin/env bash
ENV_BIN=/root/LANG/conda/envs/envi_ml/bin   # ← 1. 确认这一行
export PATH="$ENV_BIN:$PATH"
echo "Python 现在：$(which python)"
exec "$@"
