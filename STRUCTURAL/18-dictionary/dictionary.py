#list -> array, mengakses dengan menggunakan index

data_list = ['ucup', 'otong', 'dudung']
print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
#   'key':'value'
#   isi di dictionary bebas, bahkan kita bisa menambahkan dictionary di dalam dictionary
    'cp':'ucup',
    'tg':'otong',
    'dg':'dudung',
    'nmbr': 100,
    'list': data_list,
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])