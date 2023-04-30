# Crack MD5 passwords of any strenght with nVidia's CUDA using a dictionary file

import hashlib
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def md5_hash(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

def crack_password(hash_value, words):
    mod = SourceModule('''
        __global__ void search(char *hash_value, char *words, int *result)
        {
            int idx = threadIdx.x + blockIdx.x * blockDim.x;
            int word_len = strlen(words);
            
            if (idx < word_len)
            {
                char md5_hash[33];
                strncpy(md5_hash, hash_value, 33);
                char *word = words[idx];
                char *hashed_word = md5_hash(word);
                int is_equal = strcmp(hashed_word, md5_hash);
                if (is_equal == 0)
                {
                    *result = idx;
                }
            }
        }
    ''')
    kernel = mod.get_function('search')
    hash_value_gpu = cuda.mem_alloc(len(hash_value))
    cuda.memcpy_htod(hash_value_gpu, hash_value.encode('utf-8'))
    words_gpu = cuda.mem_alloc(len(words))
    cuda.memcpy_htod(words_gpu, words.encode('utf-8'))
    result = [-1]
    result_gpu = cuda.mem_alloc(len(result) * 4)
    cuda.memcpy_htod(result_gpu, result)
    block_dim = 512
    grid_dim = (len(words) + block_dim - 1) // block_dim
    kernel(hash_value_gpu, words_gpu, result_gpu, block=block_dim, grid=grid_dim)
    cuda.memcpy_dtoh(result, result_gpu)
    if result[0] != -1:
        return words[result[0]]
    else:
        return None

if __name__ == '__main__':
    hash_value = 'INSERT_MD5_HASH_VALUE_HERE'
    words_file = 'path/to/wordlist.txt' # Dictionary file path
    words = load_words(words_file)
    password = crack_password(hash_value, words)
    if password is not None:
        print(f'The password is: {password}')
    else:
        print('Password not found in wordlist.')
